# profile.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import database_connection
import globals
from mysql.connector import Error
from feedbackform import FeedbackForm



class CustomerProfile(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Customer Profile")
        self.geometry("800x600")
        self.user_id = globals.get_logged_in_user_id()  # Gets the logged-in user's ID
        user_details = self.get_user_details(self.user_id)
        if user_details:
            self.display_customer_details(user_details)
            self.populate_reservation_history(self.user_id)
            self.populate_feedback_history(self.user_id)
            
            

        
            
    def get_user_details(self, user_id):
        try:
            with database_connection.get_connection() as conn:
                with conn.cursor(dictionary=True) as cursor:
                    cursor.execute("SELECT * FROM Customer_details WHERE Customer_ID = %s", (user_id,))
                    return cursor.fetchone()  # Returns a dictionary of the user's details
        except Error as e:
            messagebox.showerror("Database Error", str(e))
            return None

            
    def populate_feedback_history(self, customer_id):
        
        feedback_list = ttk.Treeview(self, columns=("Feedback ID", "Content", "Rating"), show="headings")
        
        feedback_list.pack(pady=20)
        

        for col in feedback_list['columns']:
            feedback_list.heading(col, text=col)
        try:
            with database_connection.get_connection() as conn:
                with conn.cursor(dictionary=True) as cursor:
                    query = "SELECT Feedback_ID, Content, Rating FROM Feedback WHERE Customer_ID = %s"
                    cursor.execute(query, (customer_id,))
                    for row in cursor.fetchall():
                        feedback_list.insert("", tk.END, values=(row['Feedback_ID'], row['Content'], row['Rating']))
        except Error as e:
            messagebox.showerror("Database Error", str(e))


    def display_customer_details(self, customer_id):
        # Display customer details
        ttk.Label(self, text=f"Name: {customer_id['Customer_firstName']} {customer_id['Customer_lastName']}").pack()
        ttk.Label(self, text=f"Gender: {customer_id['Customer_gender']}").pack()
        ttk.Label(self, text=f"Driving License: {customer_id['Customer_DL_Number']}").pack()
        # Add more details as needed
        
  

    def on_reservation_select(self, event):
        selected_item = self.reservations_list.selection()[0]  # Get selected item
        selected_reservation = self.reservations_list.item(selected_item, 'values')
        reservation_id, *other_values, status = selected_reservation  # Unpack all the columns; assumes 'Status' is last
        if status == 'Completed':  # Only open FeedbackForm if the reservation is completed
            feedback_form = FeedbackForm(self, reservation_id)
            feedback_form.grab_set()  # This makes the feedback form modal
        else:
            messagebox.showinfo("Feedback", "Feedback can only be submitted for completed reservations.")

       

    def populate_reservation_history(self, customer_id):
        # Initialize Treeview widget if not already initialized
        self.reservations_list = ttk.Treeview(self, columns=("Reservation ID", "Pickup Date", "Return Date", "Total Cost", "Reservation_Status"), show="headings")
        self.reservations_list.bind('<Double-1>', self.on_reservation_select)
        self.reservations_list.pack(pady=20)
  


        for col in self.reservations_list['columns']:
            self.reservations_list.heading(col, text=col)

        # Fetch and populate reservation history
        try:
            with database_connection.get_connection() as conn:
                with conn.cursor(dictionary=True) as cursor:
                    query = """SELECT r.Reservation_ID, r.Pickup_Date_Time, r.Expected_Return_DateTime, r.Total_cost, r.Reservation_Status
                           FROM Reservation r
                           LEFT JOIN Feedback f ON r.Reservation_ID = f.Reservation_ID
                           WHERE r.Customer_ID = %s AND r.Reservation_Status = 'Completed' AND f.Feedback_ID IS NULL"""
                    cursor.execute(query, (customer_id,))
                   
                    for row in cursor.fetchall():
                        self.reservations_list.insert("", tk.END, values=(row['Reservation_ID'], row['Pickup_Date_Time'], row['Expected_Return_DateTime'], row['Total_cost'], row['Reservation_Status']))
        except Error as e:
            messagebox.showerror("Database Error", str(e))


