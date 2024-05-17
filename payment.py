import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import database_connection
from mysql.connector import Error

class PaymentDetailsForm(tk.Toplevel):
    def __init__(self, parent, reservation_id, total_cost):
        super().__init__(parent)
        self.configure_gui()
        self.reservation_id = reservation_id
        self.total_cost = total_cost
        self.create_widgets()
        self.card_number_label = None
        self.cvv_label = None
        self.expiry_date_label = None

    def configure_gui(self):
        self.title("Payment Details")
        self.geometry("400x300")

    def create_widgets(self):
        ttk.Label(self, text="Payment Method:").pack(pady=5)
        
        self.payment_method_var = tk.StringVar()
        self.payment_method_combo = ttk.Combobox(
            self, textvariable=self.payment_method_var, state="readonly",
            values=["Credit Card", "Debit Card", "Online Banking", "Cash"]
        )
        self.payment_method_combo.pack()
        self.payment_method_combo.bind("<<ComboboxSelected>>", self.toggle_payment_fields)

        # Fields for card details (hidden initially)
        self.card_number_entry = ttk.Entry(self, textvariable=tk.StringVar())
        self.cvv_entry = ttk.Entry(self, textvariable=tk.StringVar())
        self.expiry_date_entry = ttk.Entry(self, textvariable=tk.StringVar())

        # Submit button
        ttk.Button(self, text="Submit Payment", command=self.submit_payment).pack(pady=25)

    def toggle_payment_fields(self, event=None):
        if self.payment_method_var.get() in ["Credit Card", "Debit Card", "Online Banking"]:
            self.show_card_fields()
        else:
            self.hide_card_fields()

    def show_card_fields(self):
        # Create labels if they haven't been created yet
        if not self.card_number_label:
            self.card_number_label = ttk.Label(self, text="Card Number:")
            self.cvv_label = ttk.Label(self, text="CVV:")
            self.expiry_date_label = ttk.Label(self, text="Expiry Date (MM/YY):")

        # Pack labels and entry widgets
        self.card_number_label.pack(pady=(10, 0))
        self.card_number_entry.pack()
        self.cvv_label.pack(pady=(10, 0))
        self.cvv_entry.pack()
        self.expiry_date_label.pack(pady=(10, 0))
        self.expiry_date_entry.pack()

    def hide_card_fields(self):
        if self.card_number_label:
            self.card_number_label.pack_forget()
        self.card_number_entry.pack_forget()
        
        if self.cvv_label:
            self.cvv_label.pack_forget()
        self.cvv_entry.pack_forget()
        
        if self.expiry_date_label:
            self.expiry_date_label.pack_forget()
        self.expiry_date_entry.pack_forget()

    def submit_payment(self):
        if self.validate_payment_details():
            self.save_payment_details()

    def validate_payment_details(self):
        payment_method = self.payment_method_var.get()
        if payment_method in ["Credit Card", "Debit Card", "Online Banking"]:
            # Add your validation logic here, return False if validation fails
            pass
        return True

    def save_payment_details(self):
        try:
            with database_connection.get_connection() as connection:
                cursor = connection.cursor()
                sql = """
                INSERT INTO Payment_Details (Payment_method, Total_cost, Payment_date, Late_fee, Reservation_ID)
                VALUES (%s, %s, NOW(), %s, %s)
                """
                parameters = (self.payment_method_var.get(), self.total_cost, 0.00, self.reservation_id)
                cursor.execute(sql, parameters)
                connection.commit()
                messagebox.showinfo("Payment Successful", "Your payment has been processed successfully.")
                self.destroy()
        except Error as e:
            messagebox.showerror("Error", f"An error occurred while processing your payment: {e}")

if __name__ == "__main__":
    # Example usage:
    # root = tk.Tk()
    # payment_form = PaymentDetailsForm(root, reservation_id=123, total_cost=99.99)
    # payment_form.mainloop()
    pass
