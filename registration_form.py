import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import database_connection
from mysql.connector import Error

def insert_customer_details(first_name, last_name, password, gender, dl_number, age, address, phone, email):
    try:
        with database_connection.get_connection() as connection:
            cursor = connection.cursor()
            query = ("INSERT INTO Customer_details "
                     "(Customer_firstName, Customer_lastName, Customer_password, Customer_gender, Customer_DL_Number, Customer_age, Customer_address, Customer_phoneNumber, Customer_emailID) "
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
            cursor.execute(query, (first_name, last_name, password, gender, dl_number, age, address, phone, email))
            connection.commit()
            messagebox.showinfo("Registration Successful", "Registered successfully.")
    except Error as e:
        messagebox.showerror("Error", str(e))

class RegistrationForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Registration Form")
        self.geometry("400x600")
        self.configure(bg="#F5DEB3")
        
        self.create_widgets()
        self.grid_widgets()

    def create_widgets(self):
        self.entries = {}
        fields = [
            ("First Name", "first_name", False),
            ("Last Name", "last_name", False),
            ("Password", "password", True),
            ("Gender (M/F)", "gender", False),
            ("Driving License Number", "dl_number", False),
            ("Age", "age", False),
            ("Address", "address", False),
            ("Phone Number", "phone", False),
            ("Email", "email", False)
        ]
        for idx, (label, var, is_password) in enumerate(fields):
            label_widget = ttk.Label(self, text=f"{label}:", background="#F5DEB3")
            entry_var = tk.StringVar()
            entry_widget = ttk.Entry(self, textvariable=entry_var, show="*" if is_password else None)
            
            self.entries[var] = entry_var
            setattr(self, f"{var}_label", label_widget)
            setattr(self, f"{var}_entry", entry_widget)

        self.submit_button = ttk.Button(self, text="Submit", command=self.submit_form)

    def grid_widgets(self):
        row = 0
        for var in self.entries:
            label = getattr(self, f"{var}_label")
            entry = getattr(self, f"{var}_entry")
            label.grid(row=row, column=0, sticky=tk.W, padx=10, pady=5)
            entry.grid(row=row, column=1, sticky=tk.EW, padx=10, pady=5)
            row += 1
        
        self.submit_button.grid(row=row, column=0, columnspan=2, pady=20)

    def submit_form(self):
        data = {var: entry.get() for var, entry in self.entries.items()}
        data['age'] = int(data['age'])  # Convert age to integer
        
        try:
            insert_customer_details(**data)
            self.destroy()  # Close the registration form
        except ValueError as ve:
            messagebox.showerror("Input Error", f"Invalid input: {ve}")
        except Error as e:
            messagebox.showerror("Database Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationForm(root)
    app.mainloop()
