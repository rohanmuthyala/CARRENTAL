import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import database_connection
import globals
from mysql.connector import Error


class FeedbackForm(tk.Toplevel):
    def __init__(self, parent, reservation_id):
        super().__init__(parent)
        self.parent = parent  # Store the reference to the parent
        self.reservation_id = reservation_id
        self.rating_var = tk.IntVar(value=1)  # Initialize with a default value of 1
        self.title("Feedback Form")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Rating (1-5):").pack(pady=(10, 0))  # Add some vertical padding
        rating_entry = ttk.Entry(self, textvariable=self.rating_var)
        rating_entry.pack(pady=(0, 10))  # Add some vertical padding

        ttk.Label(self, text="Feedback:").pack(pady=(10, 0))  # Add some vertical padding
        self.content_entry = tk.Text(self, width=40, height=10)  # Ensure it's 'tk.Text', not 'ttk.Text'
        self.content_entry.pack(pady=(0, 10))  # Add some vertical padding
        self.content_entry.focus_set()  # Set focus to the feedback entry

        submit_button = ttk.Button(self, text="Submit", command=self.submit_feedback)
        submit_button.pack(pady=(10, 0))  # Add some vertical padding
    def submit_feedback(self):
        rating = self.rating_var.get()
        # Access content_entry using self to refer to the instance attribute
        content = self.content_entry.get("1.0", tk.END)
        
        try:
            with database_connection.get_connection() as conn:
                with conn.cursor() as cursor:
                    query = "INSERT INTO Feedback (Content, Rating, Customer_ID, Reservation_ID) VALUES (%s, %s, (SELECT Customer_ID FROM Reservation WHERE Reservation_ID = %s), %s)"
                    cursor.execute(query, (content, rating, self.reservation_id, self.reservation_id))
                    conn.commit()
                    messagebox.showinfo("Success", "Feedback submitted successfully")
                    if hasattr(self.parent, 'refresh_history'):
                        self.parent.refresh_history()  # Call to refresh method in the parent
        except Error as e:
            messagebox.showerror("Database Error", str(e))

        self.destroy()  # Close the feedback form after submission