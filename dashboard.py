import tkinter as tk
from tkinter import ttk
from mysql.connector import connect, Error
from tkinter import messagebox
import datetime
import database_connection
import globals
from profile_1 import CustomerProfile
from payment import PaymentDetailsForm
import datetime
import random
import string


def get_all_vehicles():
    try:
        connection = database_connection.get_connection()
        cursor = connection.cursor()
        # Execute SQL query to fetch all vehicles
        sql = "SELECT Vehicle_ID, Vehicle_Make, Vehicle_Model, Vehicle_Color, Rate_per_day, Vehicle_Status FROM Vehicle"
        cursor.execute(sql)
        vehicles = cursor.fetchall()
        return [{'id': vehicle[0], 'make': vehicle[1], 'model': vehicle[2], 'color': vehicle[3], 'rate_per_day': vehicle[4], 'status': vehicle[5]} for vehicle in vehicles]
    except Error as e:
        print(f"Error fetching vehicles: {e}")
    finally:
        if connection:
            connection.close()


def get_vehicles(criteria):
    try:
        connection = database_connection.get_connection()
        cursor = connection.cursor()
        # Execute SQL query to fetch vehicles based on criteria
        sql = "SELECT Vehicle_ID, Vehicle_Make, Vehicle_Model, Vehicle_Color, Rate_per_day, Vehicle_Status FROM Vehicle WHERE Vehicle_Make LIKE %s OR Vehicle_Model LIKE %s"
        wildcard_criteria = '%' + criteria + '%'
        cursor.execute(sql, (wildcard_criteria, wildcard_criteria))
        vehicles = cursor.fetchall()
        return [{'id': vehicle[0],'make': vehicle[1], 'model': vehicle[2], 'color': vehicle[3], 'rate_per_day': vehicle[4], 'status': vehicle[5]} for vehicle in vehicles]
    except Error as e:
        print(f"Error fetching vehicles: {e}")
    finally:
        if connection:
            connection.close()
            
def calculate_rental_cost(vehicle_id, start_date, end_date):
    try:
        connection = database_connection.get_connection()
        cursor = connection.cursor()
        sql = "SELECT Rate_per_day FROM Vehicle WHERE Vehicle_ID = %s"
        cursor.execute(sql, (vehicle_id,))
        rate = cursor.fetchone()  # Get the first row (or None if not found)

        if rate is None:
            # Handle the case where no vehicle is found
            print(f"Error: Vehicle ID {vehicle_id} not found in database.")
            return 0  # Or raise an exception if appropriate
        else:
            rate = rate[0]  # Access the rate value from the first row

        duration = (end_date - start_date).days
        cost = rate * duration
        return cost
    except Error as e:
        print(f"Error calculating rental cost: {e}")
    finally:
        if connection:
            connection.close()
def generate_confirmation_code(length=9):
    """Generate a random string of fixed length."""
    letters = string.ascii_uppercase + string.digits
    return 'CONF' + ''.join(random.choice(letters) for i in range(length))


def create_reservation(vehicle_id, customer_id, start_date, end_date, cost, pickup_location):
    try:
        
        connection = database_connection.get_connection()
        cursor = connection.cursor()
        # Execute SQL query to insert a new reservation with cost and pickup location
        #sql = "INSERT INTO Reservation (Vehicle_ID, Customer_ID, Reservation_DateTime, Pickup_Date_Time, Expected_Return_DateTime, Reservation_Status, Total_Cost, Pickup_Location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        #values = (vehicle_id, customer_id, datetime.datetime.now(), start_date, end_date, 'Pending', cost, pickup_location)
        sql = """ INSERT INTO Reservation (
    Vehicle_ID, Customer_ID, Reservation_DateTime, 
    Pickup_Date_Time, Actual_Return_DateTime, Expected_Return_DateTime, 
    Reservation_Status, Total_Cost, Pickup_Location, Reservation_Confirmation
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
        values = (
    vehicle_id, customer_id, datetime.datetime.now(), start_date, start_date, end_date, 
    'Pending', cost, pickup_location, generate_confirmation_code()
)
        cursor.execute(sql, values)
        reservation_id = cursor.lastrowid  # Get the last inserted id
        connection.commit()
        print("Reservation created successfully")
        print("Reservation created successfully with ID:", reservation_id)
        return reservation_id  # Return the ID of the new reservation
    except Error as e:
        print(f"Error creating reservation: {e}")
    finally:
        if connection:
            connection.close()

def get_customer_reservations(customer_id):
    try:
        connection = database_connection.get_connection()
        cursor = connection.cursor()
        # Execute SQL query to fetch customer reservations with available columns
        
        sql = "SELECT Reservation_ID, Pickup_Date_Time, Expected_Return_DateTime, Reservation_Status, Pickup_Location, Total_Cost FROM Reservation WHERE Customer_ID = %s"
        print(customer_id)
        cursor.execute(sql, (customer_id,))
        reservations = cursor.fetchall()
        return [{'id': reservation[0], 'pickup_datetime': reservation[1], 'expected_return_datetime': reservation[2], 'status': reservation[3], 'pickup_location': reservation[4], 'total_cost': reservation[5]} for reservation in reservations]
    except Error as e:
        print(f"Error fetching customer reservations: {e}")
    finally:
        if connection:
            connection.close()

class CustomerDashboard(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Customer Dashboard")
        self.geometry("800x600")
        self.customer_id = globals.get_logged_in_user_id()
        
        profile_button = ttk.Button(self, text="Customer Profile", command=self.open_customer_profile)
        profile_button.pack(pady=5)  # Adjust the padding and packing as needed

        # Search bar components
        
        
        search_frame = ttk.Frame(self)
        search_frame.pack(pady=5)
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side='left', padx=5)
        search_button = ttk.Button(search_frame, text="Search", command=self.search_vehicles)
        search_button.pack(side='left')

        # Vehicle list
        self.vehicle_list = ttk.Treeview(self, columns=('id','make', 'model', 'rate_per_day', 'color', 'status'), show='headings')
        self.vehicle_list.pack(pady=5, fill="both", expand=True)
        self.vehicle_list.heading('id', text='id')
        self.vehicle_list.heading('make', text='Make')
        self.vehicle_list.heading('model', text='Model')
        self.vehicle_list.heading('rate_per_day', text='rate_per_day')
        self.vehicle_list.heading('status', text='status')
        self.vehicle_list.heading('color', text='color')
        self.vehicle_list.bind('<<TreeviewSelect>>', self.show_vehicle_details)
        
        vehicles = get_all_vehicles()
        for vehicle in vehicles:
            values = (vehicle['id'], vehicle['make'], vehicle['model'], vehicle['rate_per_day'], vehicle['color'], vehicle['status'])
            self.vehicle_list.insert('', 'end', values=values)

        # Detailed vehicle information frame
        self.vehicle_details_frame = ttk.Frame(self)
        self.vehicle_details_frame.pack(pady=5, fill="both", expand=True)
        self.vehicle_details_label = ttk.Label(self.vehicle_details_frame, text="Vehicle Details")
        self.vehicle_details_label.pack(pady=5)

        # Reservation components
        reservation_frame = ttk.Frame(self)
        reservation_frame.pack(pady=5)
        pickup_label = ttk.Label(reservation_frame, text="Pickup Date/Time:")
        pickup_label.pack(side='left', padx=5)
        self.pickup_datetime = ttk.Entry(reservation_frame)
        self.pickup_datetime.pack(side='left')
        return_label = ttk.Label(reservation_frame, text="Return Date/Time:")
        return_label.pack(side='left', padx=5)
        self.return_datetime = ttk.Entry(reservation_frame)
        self.return_datetime.pack(side='left')
        pickup_location_label = ttk.Label(reservation_frame, text="Pickup Location:")
        pickup_location_label.pack(side='left', padx=5)
        self.pickup_location_var = tk.StringVar(value="Hyderabad")  # Replace 'Default Text' with the actual default value you want
        self.pickup_location = ttk.Entry(reservation_frame, textvariable=self.pickup_location_var)
        self.pickup_location.pack(side='left')
        self.reserve_button = ttk.Button(reservation_frame, text="Reserve", command=self.make_reservation)
        self.reserve_button.pack(side='left', padx=5)
    
    
        past_reservations_frame = ttk.Frame(self)
        past_reservations_frame.pack(pady=5, fill="both", expand=True)
        past_reservations_label = ttk.Label(past_reservations_frame, text="Reservation History")
        past_reservations_label.pack(pady=5)
        
        filter_frame = ttk.Frame(past_reservations_frame)
        filter_frame.pack(pady=5)
        all_button = ttk.Button(filter_frame, text="All", command=lambda: self.filter_reservations("All"))
        all_button.pack(side="left", padx=5)
        pending_button = ttk.Button(filter_frame, text="Pending", command=lambda: self.filter_reservations("Pending"))
        pending_button.pack(side="left", padx=5)
        completed_button = ttk.Button(filter_frame, text="Completed", command=lambda: self.filter_reservations("Completed"))
        completed_button.pack(side="left", padx=5)
        Rejected_button = ttk.Button(filter_frame, text="Rejected", command=lambda: self.filter_reservations("Rejected"))
        Rejected_button.pack(side="left", padx=5)
        
        
        
        
        
        
        
        self.past_reservations_list = ttk.Treeview(past_reservations_frame, columns=('id', 'pickup_datetime', 'expected_return_datetime', 'status', 'pickup_location', 'cost'), show='headings')
        self.past_reservations_list.pack(fill='both', expand=True)
        self.past_reservations_list.heading('id', text='ID')
        self.past_reservations_list.heading('pickup_datetime', text='Pickup Date/Time')
        self.past_reservations_list.heading('expected_return_datetime', text='Expected Return Date/Time')
        self.past_reservations_list.heading('status', text='Status')
        self.past_reservations_list.heading('pickup_location', text='Pickup Location')
        self.past_reservations_list.heading('cost', text='Cost')
        self.populate_past_reservations()
        
    def open_customer_profile(self):
        # This method will be called when the profile button is clicked
        # It creates and opens the CustomerProfile window
        customer_profile_window = CustomerProfile(self)
        customer_profile_window.grab_set()  # Make the profile window modal if you want

    def search_vehicles(self):
        criteria = self.search_var.get()
        if criteria:
            vehicles = get_vehicles(criteria)
        else:
            vehicles = get_all_vehicles()
        self.vehicle_list.delete(*self.vehicle_list.get_children())  # Clear the existing tree view
        for vehicle in vehicles:
            values = (vehicle['id'],vehicle['make'], vehicle['model'], vehicle['rate_per_day'],  vehicle['color'], vehicle['status'])
            self.vehicle_list.insert('', 'end', values=values)

    def show_vehicle_details(self, event):
        selected_item = self.vehicle_list.selection()[0]
        vehicle_id = self.vehicle_list.item(selected_item, 'values')[0]
        # Fetch vehicle details from the database using vehicle_id
        # Update the widgets in self.vehicle_details_frame with the fetched data

    def make_reservation(self):
        selected_item = self.vehicle_list.selection()[0]
        vehicle_id = self.vehicle_list.item(selected_item, 'values')[0]
        pickup = self.pickup_datetime.get()
        return_date = self.return_datetime.get()
        pickup_location = self.pickup_location.get()
        start_date = datetime.datetime.strptime(pickup, "%Y-%m-%d %H:%M:%S")
        end_date = datetime.datetime.strptime(return_date, "%Y-%m-%d %H:%M:%S")
        cost = calculate_rental_cost(vehicle_id, start_date, end_date)
        confirm = messagebox.askyesno("Confirm Reservation", f"The total cost for the reservation is ${cost:.2f}. Do you want to proceed?")
        if confirm:
            messagebox.showinfo("Reservation Confirmed", "Your reservation has been sent for approval.")
            self.populate_past_reservations()
            reservation_id = create_reservation(vehicle_id, self.customer_id, start_date, end_date, cost, pickup_location)
            print("Reservation_ID", reservation_id)
             # Ask for payment details
            PaymentDetailsForm(self, reservation_id, cost)  # Assuming this form collects and processes payment details

            
            
    def populate_past_reservations(self):
        reservations = get_customer_reservations(self.customer_id)
        self.past_reservations_list.delete(*self.past_reservations_list.get_children())
        if reservations is None:
            reservations = []
        for reservation in reservations:
            if reservation['status'] == 'Pending':
                status_value = 'Pending'
            elif reservation['status'] == 'Completed':
                status_value = 'Completed'
            elif reservation['status'] == 'Rejected':
                status_value = 'Rejected'
            else:
                status_value = reservation['status']  # Use the raw value if not recognized

            values = (reservation['id'], reservation['pickup_datetime'], reservation['expected_return_datetime'], status_value, reservation['pickup_location'], reservation['total_cost'])
            self.past_reservations_list.insert('', 'end', values=values)
            
        for child in self.past_reservations_list.get_children():
            self.past_reservations_list.reattach(child, '', 0)
            
            
    def filter_reservations(self, status):
        reservations = get_customer_reservations(self.customer_id)
        self.past_reservations_list.delete(*self.past_reservations_list.get_children())
        for reservation in reservations:
            if reservation['status'] == 'Pending':
                status_value = 'Pending'
            elif reservation['status'] == 'Completed':
                status_value = 'Completed'
            elif reservation['status'] == 'Rejected':
                status_value = 'Rejected'
            else:
                status_value = reservation['status']  # Use the raw value if not recognized

            if status == 'All' or status_value == status:
                values = (reservation['id'], reservation['pickup_datetime'], reservation['expected_return_datetime'], status_value, reservation['pickup_location'], reservation['total_cost'])
                self.past_reservations_list.insert('', 'end', values=values)

if __name__ == "__main__":
    root = tk.Tk()  # This should be tk.Tk(), not tk.Toplevel()
    root.withdraw()  # Optionally hide the root window; you can also set it up as your main application window
    
    # Now you can create your dashboard or profile based on the program's flow
    # For example, if CustomerDashboard is the first window you want to show, do it like this:
    dashboard = CustomerDashboard()  # This will be your top-level window
   
    dashboard.mainloop()  # Call mainloop() on the dashboard if it's your main application window
    
    # If CustomerProfile is opened later from within CustomerDashboard, you do not call mainloop() again.
    # Example (not to be included in the main block):
    # profile = CustomerProfile()  # This should be opened from an action inside CustomerDashboard
