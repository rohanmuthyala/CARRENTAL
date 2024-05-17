import tkinter as tk
from tkinter import ttk
from mysql.connector import connect, Error
from tkinter import messagebox

import database_connection



root = tk.Tk()
root.title("Car Rental Admin Dashboard")
root.geometry("1200x800")  # Set the initial window size

# Create a notebook widget to hold the different tabs
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Vehicle Management Tab
vehicle_tab = ttk.Frame(notebook)
notebook.add(vehicle_tab, text="Vehicle Management")




# Create a frame to hold the canvas and scrollbars
vehicle_frame = ttk.Frame(vehicle_tab)
vehicle_frame.pack(pady=10, fill=tk.BOTH, expand=True)

# Create a canvas to hold the treeview
vehicle_canvas = tk.Canvas(vehicle_frame)
vehicle_canvas.grid(row=0, column=0, sticky="nsew")

# Add vertical scrollbar to the canvas
v_scroll = ttk.Scrollbar(vehicle_frame, orient="vertical", command=vehicle_canvas.yview)
v_scroll.grid(row=0, column=1, sticky="ns")
vehicle_canvas.configure(yscrollcommand=v_scroll.set)

# Add horizontal scrollbar to the canvas
h_scroll = ttk.Scrollbar(vehicle_frame, orient="horizontal", command=vehicle_canvas.xview)
h_scroll.grid(row=1, column=0, sticky="ew")
vehicle_canvas.configure(xscrollcommand=h_scroll.set)

# Configure the grid layout for vehicle_frame to make scrollbars work
vehicle_frame.grid_rowconfigure(0, weight=1)
vehicle_frame.grid_columnconfigure(0, weight=1)

# Styling the Treeview
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview.Heading", font=('Calibri', 10, 'bold'))
style.configure("Treeview", font=('Calibri', 10), rowheight=25)



# Create a treeview frame to hold the treeview
treeview_frame = ttk.Frame(vehicle_canvas)

# Create the treeview inside the treeview frame
vehicle_tree = ttk.Treeview(treeview_frame, columns=("make", "model", "color", "insurance_number", "license_number", "rate_per_day", "status"), show="headings")

# Configure column headings
vehicle_tree.heading("make", text="Make")
vehicle_tree.heading("model", text="Model")
vehicle_tree.heading("color", text="Color")
vehicle_tree.heading("insurance_number", text="Insurance Number")
vehicle_tree.heading("license_number", text="License Number")
vehicle_tree.heading("rate_per_day", text="Rate Per Day")
vehicle_tree.heading("status", text="Status")


# Place the treeview inside the treeview frame
vehicle_tree.pack(fill="both", expand=True)

# Create a window inside the canvas for the treeview frame
vehicle_canvas.create_window((0, 0), window=treeview_frame, anchor="nw")

# Binding the frame's configuration event to resize the canvas's window
def on_frame_configure(event):
    vehicle_canvas.configure(scrollregion=vehicle_canvas.bbox("all"))

treeview_frame.bind("<Configure>", on_frame_configure)


def fetch_vehicles():
    # Clear the tree view
    for i in vehicle_tree.get_children():
        vehicle_tree.delete(i)
    
    # Establish database connection
    db = database_connection.get_connection()
    cursor = db.cursor()
    
    # Execute the SELECT query
    cursor.execute("SELECT * FROM Vehicle")
    vehicles = cursor.fetchall()
    
    # Insert fetched data into the tree view
    for vehicle in vehicles:
        vehicle_tree.insert("", "end", text=vehicle[0], values=(vehicle[1], vehicle[2], vehicle[3], vehicle[4], vehicle[5], vehicle[6], vehicle[7]))


# Function to add a new vehicle
def add_vehicle():
    add_vehicle_window = tk.Toplevel(root)
    add_vehicle_window.title("Add Vehicle")

    # Create input fields for vehicle details
    make_label = tk.Label(add_vehicle_window, text="Make:")
    make_label.pack()
    make_entry = tk.Entry(add_vehicle_window)
    make_entry.pack()   

    model_label = tk.Label(add_vehicle_window, text="Model:")
    model_label.pack()
    model_entry = tk.Entry(add_vehicle_window)
    model_entry.pack()

    color_label = tk.Label(add_vehicle_window, text="Color:")
    color_label.pack()
    color_entry = tk.Entry(add_vehicle_window)
    color_entry.pack()

    insurance_number_label = tk.Label(add_vehicle_window, text="Insurance Number:")
    insurance_number_label.pack()
    insurance_number_entry = tk.Entry(add_vehicle_window)
    insurance_number_entry.pack()

    license_number_label = tk.Label(add_vehicle_window, text="License Number:")
    license_number_label.pack()
    license_number_entry = tk.Entry(add_vehicle_window)
    license_number_entry.pack()

    rate_per_day_label = tk.Label(add_vehicle_window, text="Rate Per Day:")
    rate_per_day_label.pack()
    rate_per_day_entry = tk.Entry(add_vehicle_window)
    rate_per_day_entry.pack()

    status_label = tk.Label(add_vehicle_window, text="Status:")
    status_label.pack()
    status_entry = tk.Entry(add_vehicle_window)
    status_entry.pack()

    # Function to save the new vehicle
    def save_vehicle():
        db = database_connection.get_connection()
        cursor = db.cursor()
        query = "INSERT INTO Vehicle (Vehicle_Make, Vehicle_Model, Vehicle_Color, Vehicle_insurance_Number, Vehicle_license_Number, Rate_per_day, Vehicle_Status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (make_entry.get(), model_entry.get(), color_entry.get(), insurance_number_entry.get(), license_number_entry.get(), rate_per_day_entry.get(), status_entry.get())
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Vehicle added successfully.")
        add_vehicle_window.destroy()
        fetch_vehicles()

    save_button = tk.Button(add_vehicle_window, text="Save", command=save_vehicle)
    save_button.pack(pady=10)

# Function to edit vehicle information
def edit_vehicle():
    selected_item = vehicle_tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a vehicle to edit.")
        return

    vehicle_id = vehicle_tree.item(selected_item)["text"]

    edit_vehicle_window = tk.Toplevel(root)
    edit_vehicle_window.title("Edit Vehicle")

    db = database_connection.get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Vehicle WHERE Vehicle_ID = %s", (vehicle_id,))
    vehicle = cursor.fetchone()

    # Create input fields for vehicle details
    make_label = tk.Label(edit_vehicle_window, text="Make:")
    make_label.pack()
    make_entry = tk.Entry(edit_vehicle_window)
    make_entry.insert(0, vehicle[1])
    make_entry.pack()

    model_label = tk.Label(edit_vehicle_window, text="Model:")
    model_label.pack()
    model_entry = tk.Entry(edit_vehicle_window)
    model_entry.insert(0, vehicle[2])
    model_entry.pack()

    color_label = tk.Label(edit_vehicle_window, text="Color:")
    color_label.pack()
    color_entry = tk.Entry(edit_vehicle_window)
    color_entry.insert(0, vehicle[3])
    color_entry.pack()

    insurance_number_label = tk.Label(edit_vehicle_window, text="Insurance Number:")
    insurance_number_label.pack()
    insurance_number_entry = tk.Entry(edit_vehicle_window)
    insurance_number_entry.insert(0, vehicle[4])
    insurance_number_entry.pack()

    license_number_label = tk.Label(edit_vehicle_window, text="License Number:")
    license_number_label.pack()
    license_number_entry = tk.Entry(edit_vehicle_window)
    license_number_entry.insert(0, vehicle[5])
    license_number_entry.pack()

    rate_per_day_label = tk.Label(edit_vehicle_window, text="Rate Per Day:")
    rate_per_day_label.pack()
    rate_per_day_entry = tk.Entry(edit_vehicle_window)
    rate_per_day_entry.insert(0, vehicle[6])
    rate_per_day_entry.pack()

    status_label = tk.Label(edit_vehicle_window, text="Status:")
    status_label.pack()
    status_entry = tk.Entry(edit_vehicle_window)
    status_entry.insert(0, vehicle[7])
    status_entry.pack()

    # Function to save the edited vehicle
    def save_edited_vehicle():
        db = database_connection.get_connection()
        cursor = db.cursor()
        query = "UPDATE Vehicle SET Vehicle_Make = %s, Vehicle_Model = %s, Vehicle_Color = %s, Vehicle_insurance_Number = %s, Vehicle_license_Number = %s, Rate_per_day = %s, Vehicle_Status = %s WHERE Vehicle_ID = %s"
        values = (make_entry.get(), model_entry.get(), color_entry.get(), insurance_number_entry.get(), license_number_entry.get(), rate_per_day_entry.get(), status_entry.get(), vehicle_id)
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Vehicle updated successfully.")
        edit_vehicle_window.destroy()
        fetch_vehicles()

    save_button = tk.Button(edit_vehicle_window, text="Save", command=save_edited_vehicle)
    save_button.pack(pady=10)
# Call the fetch_vehicles function to populate the treeview
fetch_vehicles()
# Function to mark a vehicle as under maintenance
def mark_maintenance():
    selected_item = vehicle_tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a vehicle to mark as under maintenance.")
        return

    vehicle_id = vehicle_tree.item(selected_item)["text"]

    db = database_connection.get_connection()
    cursor = db.cursor()
    query = "UPDATE Vehicle SET Vehicle_Status = 'Under Maintenance' WHERE Vehicle_ID = %s"
    cursor.execute(query, (vehicle_id,))
    db.commit()
    messagebox.showinfo("Success", "Vehicle marked as under maintenance.")
    fetch_vehicles()
# Add buttons for vehicle management
add_vehicle_button = tk.Button(vehicle_tab, text="Add Vehicle", command=add_vehicle)
add_vehicle_button.pack(pady=10)

edit_vehicle_button = tk.Button(vehicle_tab, text="Edit Vehicle", command=edit_vehicle)
edit_vehicle_button.pack(pady=10)

mark_maintenance_button = tk.Button(vehicle_tab, text="Mark Under Maintenance", command=mark_maintenance)
mark_maintenance_button.pack(pady=10)
# Customer Management Tab
customer_tab = ttk.Frame(notebook)
notebook.add(customer_tab, text="Customer Management")

# Create a frame to hold the canvas and scrollbars
customer_frame = ttk.Frame(customer_tab)
customer_frame.pack(pady=10, fill=tk.BOTH, expand=True)

# Create a canvas to hold the treeview
customer_canvas = tk.Canvas(customer_frame)
customer_canvas.grid(row=0, column=0, sticky="nsew")

# Add vertical scrollbar to the canvas
customer_v_scroll = ttk.Scrollbar(customer_frame, orient="vertical", command=customer_canvas.yview)
customer_v_scroll.grid(row=0, column=1, sticky="ns")
customer_canvas.configure(yscrollcommand=customer_v_scroll.set)

# Add horizontal scrollbar to the canvas
customer_h_scroll = ttk.Scrollbar(customer_frame, orient="horizontal", command=customer_canvas.xview)
customer_h_scroll.grid(row=1, column=0, sticky="ew")
customer_canvas.configure(xscrollcommand=customer_h_scroll.set)

# Configure the grid layout for customer_frame to make scrollbars work
customer_frame.grid_rowconfigure(0, weight=1)
customer_frame.grid_columnconfigure(0, weight=1)


# Create the treeview inside the customer_treeview_frame
customer_tree = ttk.Treeview(customer_canvas, columns=("first_name", "last_name", "gender", "dl_number", "address", "phone_number", "email"), show="headings")

# Configure column headings
customer_tree.heading("first_name", text="First Name")
customer_tree.heading("last_name", text="Last Name")
customer_tree.heading("gender", text="Gender")
customer_tree.heading("dl_number", text="DL Number")
customer_tree.heading("address", text="Address")
customer_tree.heading("phone_number", text="Phone Number")
customer_tree.heading("email", text="Email")

# Place the treeview inside the customer_treeview_frame
customer_tree.pack(fill="both", expand=True)

# Place the treeview inside the canvas
customer_canvas.create_window((0, 0), window=customer_tree, anchor="nw")

# Binding the treeview's configuration event to update the scrollregion of the canvas
def on_treeview_configure(event):
    # Update the scroll region to encompass the treeview
    customer_canvas.configure(scrollregion=customer_canvas.bbox("all"))

customer_tree.bind("<Configure>", on_treeview_configure)



# Function to fetch customer data from the database
def fetch_customers():
    db = database_connection.get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Customer_details")
    customers = cursor.fetchall()
    print(customers[0])
    for customer in customers:
        customer_tree.insert("", "end", text=customer[0], values=(customer[1], customer[2], customer[4], customer[5], customer[7], customer[8], customer[9]))

# Call the fetch_customers function to populate the treeview
fetch_customers()



# Function to search for a customer
def search_customer():
    search_window = tk.Toplevel(root)
    search_window.title("Search Customer")

    search_label = tk.Label(search_window, text="Search by name or email:")
    search_label.pack()

    search_entry = tk.Entry(search_window)
    search_entry.pack()

    search_tree = ttk.Treeview(search_window, columns=("first_name", "last_name", "gender", "dl_number", "address", "phone_number", "email"))
    search_tree.heading("#0", text="ID")
    search_tree.heading("first_name", text="First Name")
    search_tree.heading("last_name", text="Last Name")
    search_tree.heading("gender", text="Gender")
    search_tree.heading("dl_number", text="DL Number")
    search_tree.heading("address", text="Address")
    search_tree.heading("phone_number", text="Phone Number")
    search_tree.heading("email", text="Email")
    search_tree.pack(pady=10)

    def perform_search():
        db = database_connection.get_connection()
        cursor = db.cursor()
        search_term = search_entry.get()
        query = "SELECT * FROM Customer_details WHERE Customer_firstName LIKE %s OR Customer_lastName LIKE %s OR Customer_emailID LIKE %s"
        cursor.execute(query, (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
        customers = cursor.fetchall()
        search_tree.delete(*search_tree.get_children())
        for customer in customers:
            search_tree.insert("", "end", text=customer[0], values=(customer[1], customer[2], customer[4], customer[5], customer[6], customer[7], customer[8]))

    search_button = tk.Button(search_window, text="Search", command=perform_search)
    search_button.pack(pady=10)

# Function to edit customer information
def edit_customer():
    selected_item = customer_tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a customer to edit.")
        return

    customer_id = customer_tree.item(selected_item)["text"]

    edit_customer_window = tk.Toplevel(root)
    edit_customer_window.title("Edit Customer")

    db = database_connection.get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Customer_details WHERE Customer_ID = %s", (customer_id,))
    customer = cursor.fetchone()

    # Create input fields for customer details
    first_name_label = tk.Label(edit_customer_window, text="First Name:")
    first_name_label.pack()
    first_name_entry = tk.Entry(edit_customer_window)
    first_name_entry.insert(0, customer[1])
    first_name_entry.pack()

    last_name_label = tk.Label(edit_customer_window, text="Last Name:")
    last_name_label.pack()
    last_name_entry = tk.Entry(edit_customer_window)
    last_name_entry.insert(0, customer[2])
    last_name_entry.pack()

    gender_label = tk.Label(edit_customer_window, text="Gender:")
    gender_label.pack()
    gender_entry = tk.Entry(edit_customer_window)
    gender_entry.insert(0, customer[4])
    gender_entry.pack()

    dl_number_label = tk.Label(edit_customer_window, text="DL Number:")
    dl_number_label.pack()
    dl_number_entry = tk.Entry(edit_customer_window)
    dl_number_entry.insert(0, customer[5])
    dl_number_entry.pack()

    address_label = tk.Label(edit_customer_window, text="Address:")
    address_label.pack()
    address_entry = tk.Entry(edit_customer_window)
    address_entry.insert(0, customer[7])
    address_entry.pack()

    phone_number_label = tk.Label(edit_customer_window, text="Phone Number:")
    phone_number_label.pack()
    phone_number_entry = tk.Entry(edit_customer_window)
    phone_number_entry.insert(0, customer[8])
    phone_number_entry.pack()

    email_label = tk.Label(edit_customer_window, text="Email:")
    email_label.pack()
    email_entry = tk.Entry(edit_customer_window)
    email_entry.insert(0, customer[9])
    email_entry.pack()

    # Function to save the edited customer
    def save_edited_customer():
        db = database_connection.get_connection()
        cursor = db.cursor()
        query = "UPDATE Customer_details SET Customer_firstName = %s, Customer_lastName = %s, Customer_gender = %s, Customer_DL_Number = %s, Customer_address = %s, Customer_phoneNumber = %s, Customer_emailID = %s WHERE Customer_ID = %s"
        values = (first_name_entry.get(), last_name_entry.get(), gender_entry.get(), dl_number_entry.get(), address_entry.get(), phone_number_entry.get(), email_entry.get(), customer_id)
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Customer updated successfully.")
        edit_customer_window.destroy()
        fetch_customers()

    save_button = tk.Button(edit_customer_window, text="Save", command=save_edited_customer)
    save_button.pack(pady=10)
def delete_customer():
    selected_item = customer_tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a customer to delete.")
        return

    customer_id = customer_tree.item(selected_item)["text"]

    if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this customer?"):
        try:
            db = database_connection.get_connection()
            cursor = db.cursor()
            cursor.execute("DELETE FROM Customer_details WHERE Customer_ID = %s", (customer_id,))
            db.commit()
            customer_tree.delete(selected_item)
            messagebox.showinfo("Success", "Customer deleted successfully.")
        except Error as e:
            messagebox.showerror("Database Error", str(e))




# Add buttons for customer management
search_customer_button = tk.Button(customer_tab, text="Search Customer", command=search_customer)
search_customer_button.pack(pady=10)

edit_customer_button = tk.Button(customer_tab, text="Edit Customer", command=edit_customer)
edit_customer_button.pack(pady=10)

delete_customer_button = tk.Button(customer_tab, text="Delete Customer", command=delete_customer)
delete_customer_button.pack(pady=10)



# Reservation Management Tab
reservation_tab = ttk.Frame(notebook)
notebook.add(reservation_tab, text="Reservation Management")

# Create a frame to hold the canvas and scrollbars
reservation_frame = ttk.Frame(reservation_tab)
reservation_frame.pack(pady=10, fill=tk.BOTH, expand=True)

# Create a canvas to hold the treeview
reservation_canvas = tk.Canvas(reservation_frame)
reservation_canvas.grid(row=0, column=0, sticky="nsew")

# Add vertical scrollbar to the canvas
reservation_v_scroll = ttk.Scrollbar(reservation_frame, orient="vertical", command=reservation_canvas.yview)
reservation_v_scroll.grid(row=0, column=1, sticky="ns")
reservation_canvas.configure(yscrollcommand=reservation_v_scroll.set)

# Add horizontal scrollbar to the canvas
reservation_h_scroll = ttk.Scrollbar(reservation_frame, orient="horizontal", command=reservation_canvas.xview)
reservation_h_scroll.grid(row=1, column=0, sticky="ew")
reservation_canvas.configure(xscrollcommand=reservation_h_scroll.set)

# Configure the grid layout for reservation_frame to make scrollbars work
reservation_frame.grid_rowconfigure(0, weight=1)
reservation_frame.grid_columnconfigure(0, weight=1)

# Create the treeview for reservation management
reservation_tree = ttk.Treeview(reservation_canvas, columns=("customer", "vehicle", "reservation_datetime", "pickup_datetime", "expected_return_datetime", "pickup_location", "total_cost", "status"), show="headings")
reservation_tree.heading("customer", text="Customer")
reservation_tree.heading("vehicle", text="Vehicle")
reservation_tree.heading("reservation_datetime", text="Reservation Date/Time")
reservation_tree.heading("pickup_datetime", text="Pickup Date/Time")
reservation_tree.heading("expected_return_datetime", text="Expected Return Date/Time")
reservation_tree.heading("pickup_location", text="Pickup Location")
reservation_tree.heading("total_cost", text="Total Cost")
reservation_tree.heading("status", text="Status")

# Create a window inside the canvas for the treeview
canvas_window = reservation_canvas.create_window((0, 0), window=reservation_tree, anchor="nw", tags="canvas_window")
# Function to update the scrollregion to encompass the treeview
def update_scrollregion(_):
    # Configure the canvas's scrollregion to fit the treeview's current size
    reservation_canvas.configure(scrollregion=reservation_canvas.bbox("all"))

# Bind the treeview's configure event to update the scrollregion of the canvas
reservation_tree.bind("<Configure>", update_scrollregion)


def resize_canvas_window_to_content():
    # Assuming each column's width is known or can be estimated
    total_columns_width = sum([reservation_tree.column(col_id, "width") for col_id in reservation_tree["columns"]])
    # Optionally, add some padding to the total width
    total_width_with_padding = total_columns_width + 20  # Adjust the padding as needed
    
    # Use the total width to configure the canvas window size
    reservation_canvas.itemconfigure(canvas_window, width=total_width_with_padding)

    # Now, update the canvas's scrollregion to encompass the new size of the treeview
    reservation_canvas.configure(scrollregion=reservation_canvas.bbox("all"))

# Call this function after setting up the treeview and its columns, and after populating it with data
resize_canvas_window_to_content()

# Bind the treeview's configuration event to ensure the canvas updates its scrollregion
reservation_tree.bind("<Configure>", lambda e: update_scrollregion)

# Bind the canvas's configuration event to adjust the width of the canvas window
reservation_canvas.bind("<Configure>", resize_canvas_window_to_content)





# Function to fetch reservation data from the database
def fetch_reservations():
    db = database_connection.get_connection()
    cursor = db.cursor()
    cursor.execute("""
        SELECT
            r.Reservation_ID,
            CONCAT(c.Customer_firstName, ' ', c.Customer_lastName) AS customer,
            CONCAT(v.Vehicle_Make, ' ', v.Vehicle_Model) AS vehicle,
            r.Reservation_DateTime,
            r.Pickup_Date_Time,
            r.Expected_Return_DateTime,
            r.Pickup_location,
            r.Total_cost,
            r.Reservation_Status
        FROM Reservation r
        JOIN Customer_details c ON r.Customer_ID = c.Customer_ID
        JOIN Vehicle v ON r.Vehicle_ID = v.Vehicle_ID
    """)
    reservations = cursor.fetchall()
    for reservation in reservations:
        reservation_tree.insert("", "end", text=reservation[0], values=(reservation[1], reservation[2], reservation[3], reservation[4], reservation[5], reservation[6], reservation[7], reservation[8]))

# Call the fetch_reservations function to populate the treeview
fetch_reservations()


def filter_reservations():
    filter_window = tk.Toplevel(root)
    filter_window.title("Filter Reservations")

    # Create a combobox to select the status to filter by
    status_label = tk.Label(filter_window, text="Select status to filter by:")
    status_label.pack()
    status_combo = ttk.Combobox(filter_window, values=["All", "Pending", "Approved", "Rejected", "Completed"])
    status_combo.pack()

    def perform_filter():
        selected_status = status_combo.get()
        if selected_status == "All":
            fetch_reservations()
        else:
            try:
                db = database_connection.get_connection()
                cursor = db.cursor(dictionary=True)
                query = "SELECT * FROM Reservation WHERE Reservation_Status = %s"
                cursor.execute(query, (selected_status,))
                reservations = cursor.fetchall()
                reservation_tree.delete(*reservation_tree.get_children())  # Clear the current view
                for reservation in reservations:
                    reservation_tree.insert("", "end", text=reservation["Reservation_ID"], values=(reservation["Customer_ID"], reservation["Vehicle_ID"], reservation["Reservation_DateTime"], reservation["Pickup_Date_Time"], reservation["Expected_Return_DateTime"], reservation["Pickup_location"], reservation["Total_cost"], reservation["Reservation_Status"]))
            except Error as e:
                messagebox.showerror("Database Error", str(e))

    filter_button = tk.Button(filter_window, text="Filter", command=perform_filter)
    filter_button.pack(pady=10)
def approve_reservation():
    selected_item = reservation_tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a reservation to approve.")
        return

    reservation_id = reservation_tree.item(selected_item)["text"]
    try:
        db = database_connection.get_connection()
        cursor = db.cursor()
        cursor.execute("UPDATE Reservation SET Reservation_Status = 'Approved' WHERE Reservation_ID = %s", (reservation_id,))
        db.commit()
        fetch_reservations()  # Refresh the reservations list
        messagebox.showinfo("Success", "Reservation approved successfully.")
    except Error as e:
        messagebox.showerror("Database Error", str(e))

def reject_reservation():
    selected_item = reservation_tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a reservation to reject.")
        return

    reservation_id = reservation_tree.item(selected_item)["text"]
    try:
        db = database_connection.get_connection()
        cursor = db.cursor()
        cursor.execute("UPDATE Reservation SET Reservation_Status = 'Rejected' WHERE Reservation_ID = %s", (reservation_id,))
        db.commit()
        fetch_reservations()  # Refresh the reservations list
        messagebox.showinfo("Success", "Reservation rejected successfully.")
    except Error as e:
        messagebox.showerror("Database Error", str(e))

def completed_reservation():
    selected_item = reservation_tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a reservation to Complete.")
        return

    reservation_id = reservation_tree.item(selected_item)["text"]
    try:
        db = database_connection.get_connection()
        cursor = db.cursor()
        cursor.execute("UPDATE Reservation SET Reservation_Status = 'Completed' WHERE Reservation_ID = %s", (reservation_id,))
        db.commit()
        fetch_reservations()  # Refresh the reservations list
        messagebox.showinfo("Success", "Reservation Completed successfully.")
    except Error as e:
        messagebox.showerror("Database Error", str(e))

# Add buttons for reservation management
filter_reservations_button = tk.Button(reservation_tab, text="Filter Reservations", command=filter_reservations)
filter_reservations_button.pack(pady=10)

approve_reservation_button = tk.Button(reservation_tab, text="Approve Reservation", command=approve_reservation)
approve_reservation_button.pack(pady=10)

reject_reservation_button = tk.Button(reservation_tab, text="Reject Reservation", command=reject_reservation)
reject_reservation_button.pack(pady=10)
reject_reservation_button = tk.Button(reservation_tab, text="Completed Reservation", command=completed_reservation)
reject_reservation_button.pack(pady=10)
# At the end of your script, add:
root.mainloop()

