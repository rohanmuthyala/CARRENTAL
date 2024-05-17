import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import database_connection
from mysql.connector import Error
from dashboard import CustomerDashboard
from globals import set_logged_in_user_id



def validate_login(userName, password):
    try:
        connection = database_connection.get_connection()
        if connection is not None:
            cursor = connection.cursor(buffered=True)
            cursor.execute("SELECT Customer_ID FROM Customer_details WHERE Customer_firstName = %s AND Customer_password = %s", (userName, password,))
            account = cursor.fetchone()
            if account:
                return account[0]  # Return the Customer_ID
            return None
    except Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
    return None



    
def open_customer_dashboard(parent):
    
    # This function now creates an instance of the Dashboard class.
    dashboard_window = CustomerDashboard(parent)
    dashboard_window.grab_set()  # Make the dashboard window modal

class LoginForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.root = parent
        self.title("Login")
        self.geometry("300x200")
        self.configure(bg="#F5DEB3")  # Set the background color

        # Email Entry
        self.userName_label = ttk.Label(self, text="UserName:", background="#F5DEB3")
        self.userName_label.pack(pady=(20, 5))
        self.userName_entry = ttk.Entry(self)
        self.userName_entry.pack()

        # Password Entry
        self.password_label = ttk.Label(self, text="Password:", background="#F5DEB3")
        self.password_label.pack(pady=5)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack()

        # Login Button
        self.login_button = ttk.Button(self, text="Login", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        userName = self.userName_entry.get()
        password = self.password_entry.get()
        customer_id = validate_login(userName, password)
        if customer_id:
            set_logged_in_user_id(customer_id)
            messagebox.showinfo("Login Success", "You have successfully logged in.")
            self.destroy()  # Close the login window
            dashboard = CustomerDashboard()  # Create the dashboard as a top-level window
            dashboard.grab_set()  
        else:
            messagebox.showerror("Login Failed", "The username or password is incorrect.")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    login_form = LoginForm(root)
    login_form.mainloop()  # The mainloop should be called from here
