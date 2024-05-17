-- Drop tables in reverse order of dependencies to prevent foreign key constraint errors
DROP TABLE IF EXISTS Feedback;
DROP TABLE IF EXISTS Payment_Details;
DROP TABLE IF EXISTS Reservation;
DROP TABLE IF EXISTS Vehicle;
DROP TABLE IF EXISTS Customer_details;

-- Create the Customer_details table
CREATE TABLE IF NOT EXISTS Customer_details (
    Customer_ID INT AUTO_INCREMENT PRIMARY KEY,
    Customer_firstName VARCHAR(50) NOT NULL,
    Customer_lastName VARCHAR(50) NOT NULL,
    Customer_password VARCHAR(50) NOT NULL,
    Customer_gender CHAR(1) NOT NULL,
    Customer_DL_Number VARCHAR(20) NOT NULL,
    Customer_age INT NOT NULL,
    Customer_address VARCHAR(100) NOT NULL,
    Customer_phoneNumber VARCHAR(20) NOT NULL,
    Customer_emailID VARCHAR(50) NOT NULL
);


-- Sample records for Customer_details table
INSERT INTO Customer_details (Customer_firstName, Customer_lastName, Customer_password, Customer_gender, Customer_DL_Number, Customer_age, Customer_address, Customer_phoneNumber, Customer_emailID) VALUES
('Amit', 'Sharma', 'password123', 'M', 'DL0123456789', 35, '123 Main Street, Gachibowli, Telangana 110001', '9876543210', 'amit.sharma@email.com'),
('Riya', 'Gupta', 'pass456', 'F', 'DL9876543210', 28, '45 Race Course Road, Manikonda, Telangana 560001', '8765432109', 'riya.gupta@email.com'),
('Rahul', 'Singh', 'secret789', 'M', 'DL1234567890', 42, '67 Linking Road, Hanmakonda, Telangana 400063', '9012345678', 'rahul.singh@email.com'),
('Priya', 'Srivastava', 'password456', 'F', 'DL5678901234', 31, '89 M.G. Road, Kothapet, Telangana 411001', '8901234567', 'priya.srivastava@email.com'),
('Nitin', 'Desai', 'pass123', 'M', 'DL2345678901', 26, '12 Church Street, Moosapet, Telangana 700001', '7890123456', 'nitin.desai@email.com'),
('Anushka', 'Patel', 'secret456', 'F', 'DL6789012345', 38, '45 Brigade Road, Moosarambagh, Telangana 560001', '6789012345', 'anushka.patel@email.com'),
('Rohan', 'Jain', 'password789', 'M', 'DL3456789012', 29, '67 Haji Ali, Nampally, Telangana 400063', '5678901234', 'rohan.jain@email.com'),
('Neha', 'Malhotra', 'pass987', 'F', 'DL7890123456', 33, '23 Janpath, New Nampally, Telangana 110001', '4567890123', 'neha.malhotra@email.com'),
('Arjun', 'Kapoor', 'secret321', 'M', 'DL4567890123', 40, '89 Residency Road, Moosapet, Telangana 560025', '3456789012', 'arjun.kapoor@email.com'),
('Isha', 'Agarwal', 'password654', 'F', 'DL8901234567', 27, '12 Connaught Place, Manikonda, Telangana 110001', '2345678901', 'isha.agarwal@email.com'),
('Vivek', 'Mehta', 'pass789', 'M', 'DL5678901234', 36, '45 Juhu Tara Road, LB Nagar, Telangana 400049', '1234567890', 'vivek.mehta@email.com'),
('Pooja', 'Reddy', 'secret123', 'F', 'DL9012345678', 30, '67 Infantry Road, DSNR, Telangana 560001', '9087654321', 'pooja.reddy@email.com'),
('Aditya', 'Varma', 'password456', 'M', 'DL6789012345', 39, '23 M.G. Road, Chaitanya, Telangana 411001', '8976543210', 'aditya.varma@email.com'),
('Deepika', 'Rao', 'pass987', 'F', 'DL1234567890', 25, '89 Park Street, maruti nagar, Telangana 700016', '7865432109', 'deepika.rao@email.com'),
('Sanjay', 'Nair', 'secret654', 'M', 'DL7890123456', 44, '12 Brigade Road, sanat nagr, Telangana 560001', '6754321098', 'sanjay.nair@email.com'),
('Swati', 'Sharma', 'password321', 'F', 'DL2345678901', 32, '45 Haji Ali, Koti, Telangana 400063', '5643210987', 'swati.sharma@email.com'),
('Rohit', 'Patel', 'pass456', 'M', 'DL8901234567', 29, '67 Janpath, New Koti, Telangana 110001', '4532109876', 'rohit.patel@email.com'),
('Deepa', 'Rao', 'pass987', 'F', 'DL1234561760', 25, '89 Park Street, maruti nagar, Telangana 700016', '7865432109', 'deepa.rao@email.com'),
('Sonam', 'Kapoor', 'secret789', 'F', 'DL3456789012', 37, '23 Residency Road, king Koti, Telangana 560025', '3421098765', 'sonam.kapoor@email.com'),
('Amit', 'Sharma', 'password123', 'M', 'DL9012345678', 35, '123 Main Street, Nalagonda, Telangana 110001', '9876543210', 'amit.sharma@email.com'),
('Riya', 'Gupta', 'pass456', 'F', 'DL9876543210', 28, '45 Race Course Road, Hayath nagar, Telangana 560001', '8765432109', 'riya.gupta@email.com'),
('Rahul', 'Singh', 'secret789', 'M', 'DL1234567890', 42, '67 Linking Road,  LB Nagar, Telangana 400063', '9012345678', 'rahul.singh@email.com'),
('Priya', 'Srivastava', 'password456', 'F', 'DL5678901234', 31, '89 M.G. Road, West Koti, Telangana 411001', '8901234567', 'priya.srivastava@email.com'),
('Nitin', 'Desai', 'pass123', 'M', 'DL2345678901', 26, '12 Church Street, Dundigal, Telangana 700001', '7890123456', 'nitin.desai@email.com'),
('Anushka', 'Patel', 'secret456', 'F', 'DL6789012345', 38, '45 Brigade Road, Falaknama, Telangana 560001', '6789012345', 'anushka.patel@email.com'),
('Rohan', 'Jain', 'password789', 'M', 'DL3456789012', 29, '67 Haji Ali, Hafeez nagar, Telangana 400063', '5678901234', 'rohan.jain@email.com'),
('Neha', 'Malhotra', 'pass987', 'F', 'DL7890123456', 33, '23 Janpath, New malakpet, Telangana 110001', '4567890123', 'neha.malhotra@email.com'),
('Arjun', 'Kapoor', 'secret321', 'M', 'DL4567890123', 40, '89 Residency Road, NTR nagar, Telangana 560025', '3456789012', 'arjun.kapoor@email.com'),
('Isha', 'Agarwal', 'password654', 'F', 'DL8901234567', 27, '12 Connaught Place, New NTR, Telangana 110001', '2345678901', 'isha.agarwal@email.com'),
('Vivek', 'Mehta', 'pass789', 'M', 'DL5678901234', 36, '45 Juhu Tara Road, assembly, Telangana 400049', '1234567890', 'vivek.mehta@email.com');

-- Create the Vehicle table
CREATE TABLE IF NOT EXISTS Vehicle (
    Vehicle_ID INT AUTO_INCREMENT PRIMARY KEY,
    Vehicle_Make VARCHAR(50) NOT NULL,
    Vehicle_Model VARCHAR(50) NOT NULL,
    Vehicle_Color VARCHAR(20) NOT NULL,
    Vehicle_insurance_Number VARCHAR(30) NOT NULL,
    Vehicle_license_Number VARCHAR(20) NOT NULL,
    Rate_per_day DECIMAL(10, 2) NOT NULL,
    Vehicle_Status VARCHAR(20) NOT NULL
);


-- Sample records for Vehicle table
INSERT INTO Vehicle (Vehicle_Make, Vehicle_Model, Vehicle_Color, Vehicle_insurance_Number, Vehicle_license_Number, Rate_per_day, Vehicle_Status) VALUES
('Maruti Suzuki', 'Swift', 'Red', 'IN-123456789012', 'DL01AB1234', 1000.00, 'Available'),
('Hyundai', 'Creta', 'Blue', 'IN-987654321098', 'DL02CD5678', 1500.00, 'Rented'),
('Tata', 'Nexon', 'Silver', 'IN-567890123456', 'DL12EF9012', 1200.00, 'Available'),
('Maruti Suzuki', 'Baleno', 'White', 'IN-234567890123', 'DL03GH3456', 1100.00, 'Rented'),
('Hyundai', 'Verna', 'Grey', 'IN-890123456789', 'DL04IJ7890', 1400.00, 'Available'),
('Tata', 'Harrier', 'Black', 'IN-456789012345', 'DL05KL1234', 1800.00, 'Rented'),
('Maruti Suzuki', 'Ertiga', 'Red', 'IN-789012345678', 'DL06MN5678', 1300.00, 'Available'),
('Hyundai', 'i20', 'Blue', 'IN-012345678901', 'DL07OP9012', 1100.00, 'Rented'),
('Tata', 'Tiago', 'White', 'IN-345678901234', 'DL08QR3456', 900.00, 'Available'),
('Maruti Suzuki', 'Ciaz', 'Grey', 'IN-678901234567', 'DL09ST7890', 1600.00, 'Rented'),
('Hyundai', 'Venue', 'Silver', 'IN-901234567890', 'DL10UV1234', 1200.00, 'Available'),
('Tata', 'Altroz', 'Red', 'IN-234567890123', 'DL11WX5678', 1100.00, 'Rented'),
('Maruti Suzuki', 'Brezza', 'Blue', 'IN-567890123456', 'DL12YZ9012', 1400.00, 'Available'),
('Hyundai', 'Santro', 'White', 'IN-890123456789', 'DL13AB3456', 900.00, 'Rented'),
('Tata', 'Tigor', 'Grey', 'IN-012345678901', 'DL14CD7890', 1000.00, 'Available'),
('Maruti Suzuki', 'Wagon R', 'Red', 'IN-345678901234', 'DL15EF1234', 800.00, 'Rented'),
('Hyundai', 'Grand i10', 'Blue', 'IN-678901234567', 'DL16GH5678', 1000.00, 'Available'),
('Tata', 'Safari', 'Silver', 'IN-901234567890', 'DL17IJ9012', 2000.00, 'Rented'),
('Maruti Suzuki', 'S-Cross', 'White', 'IN-234567890123', 'DL18KL3456', 1500.00, 'Available'),
('Hyundai', 'Kona Electric', 'Grey', 'IN-567890123456', 'DL19MN7890', 2500.00, 'Rented'),
('Tata', 'Punch', 'Black', 'IN-890123456789', 'DL20OP1234', 1100.00, 'Available'),
('Maruti Suzuki', 'Ignis', 'Red', 'IN-012345678901', 'DL21QR5678', 1000.00, 'Rented'),
('Hyundai', 'Xcent', 'Blue', 'IN-345678901234', 'DL22ST9012', 1200.00, 'Available'),
('Tata', 'Zest', 'Silver', 'IN-678901234567', 'DL23UV3456', 1300.00, 'Rented'),
('Maruti Suzuki', 'Vitara Brezza', 'White', 'IN-901234567890', 'DL24WX7890', 1400.00, 'Available'),
('Hyundai', 'Elite i20', 'Grey', 'IN-234567890123', 'DL25YZ1234', 1100.00, 'Rented'),
('Tata', 'Hexa', 'Black', 'IN-567890123456', 'DL26AB5678', 1800.00, 'Available'),
('Maruti Suzuki', 'Celerio', 'Red', 'IN-890123456789', 'DL27CD9012', 900.00, 'Rented'),
('Hyundai', 'Elantra', 'Blue', 'IN-012345678901', 'DL28EF3456', 1700.00, 'Available'),
('Tata', 'Bolt', 'Silver', 'IN-345678901234', 'DL29GH7890', 1100.00, 'Rented');


-- Create the Reservation table
CREATE TABLE IF NOT EXISTS Reservation (
    Reservation_ID INT AUTO_INCREMENT PRIMARY KEY,
    Vehicle_ID INT NOT NULL,
    Customer_ID INT NOT NULL,
    Reservation_DateTime DATETIME NOT NULL,
    Pickup_Date_Time DATETIME NOT NULL,
    Actual_Return_DateTime DATETIME,
    Expected_Return_DateTime DATETIME NOT NULL,
    Pickup_location VARCHAR(100) NOT NULL,
    Total_cost DECIMAL(10, 2),
    Reservation_Status VARCHAR(20) NOT NULL,
    Reservation_Confirmation VARCHAR(50) NOT NULL,
    FOREIGN KEY (Vehicle_ID) REFERENCES Vehicle(Vehicle_ID),
    FOREIGN KEY (Customer_ID) REFERENCES Customer_details(Customer_ID)
);


-- Modified Sample records for Reservation table with Actual_Return_DateTime and Total_cost
INSERT INTO Reservation (Vehicle_ID, Customer_ID, Reservation_DateTime, Pickup_Date_Time,  Actual_Return_DateTime, Expected_Return_DateTime, Pickup_location, Total_cost, Reservation_Status, Reservation_Confirmation) VALUES
(8, 26, '2023-03-01 10:00:00', '2023-03-05 12:00:00', '2023-03-10 12:00:00', '2023-03-10 23:01:00', '123 Necklace Road, Hyderabad, Telangana 500003', 487.09, 'Completed', 'CONF123456'),
(21, 24, '2023-03-15 14:30:00', '2023-03-20 09:00:00', '2023-03-25 18:00:00', '2023-03-25 18:00:00', '45 Banjara Hills, Hyderabad, Telangana 500034', 0, 'Confirmed', 'CONF789012'),
(17, 6, '2023-04-01 16:00:00', '2023-04-05 10:00:00', '2023-04-10 16:00:00','2023-04-04 16:00:00', '67 Jubilee Hills, Hyderabad, Telangana 500033', 0, 'Pending', 'CONF345678'),
(7, 27, '2023-04-10 09:30:00', '2023-04-15 12:00:00', '2023-04-20 12:00:00','2023-03-20 14:00:00', '45 Hitec City, Hyderabad, Telangana 500081',521.5, 'Confirmed', 'CONF901234'),
(15, 30, '2023-04-20 14:00:00', '2023-04-25 09:00:00', '2023-04-30 18:00:00','2023-05-30 14:00:00', '32 Begumpet, Hyderabad, Telangana 500016', 235.4,'Pending', 'CONF567890'),
(18, 5, '2023-03-10 11:00:00', '2023-03-15 14:00:00', '2023-03-20 14:00:00','2023-06-09 16:00:00','21 Raj Bhavan Road, Hyderabad, Telangana 500004', 873.5,'Completed', 'CONF123789'),
(9, 12, '2023-03-25 15:30:00', '2023-03-30 10:00:00', '2023-04-04 16:00:00','2023-06-15 18:00:00', '18 Nampally, Hyderabad, Telangana 500001', 2533.3,'Confirmed', 'CONF456012'),
(20, 16, '2023-04-05 12:00:00', '2023-04-10 09:00:00', '2023-04-15 18:00:00','2023-06-25 12:00:00', '76 Somajiguda, Hyderabad, Telangana 500082',837.98, 'Pending', 'CONF789345'),
(2, 10, '2023-04-15 10:30:00', '2023-04-20 14:00:00', '2023-04-25 14:00:00','2023-05-10 12:00:00','18 Nampally, Hyderabad, Telangana 500001',3762.0, 'Confirmed', 'CONF012678'),
(4, 19, '2023-04-25 16:00:00', '2023-04-30 10:00:00', '2023-05-05 16:00:00','2023-05-20 18:00:00', '14 Ameerpet, Hyderabad, Telangana 500016',362.3, 'Pending', 'CONF345901'),
(14, 28, '2023-05-01 09:00:00', '2023-05-05 12:00:00', '2023-05-10 12:00:00','2023-07-05 18:00:00', '67 Kondapur, Hyderabad, Telangana 500084',983.32, 'Confirmed', 'CONF678234'),
(22, 13, '2023-05-10 14:30:00', '2023-05-15 09:00:00', '2023-05-20 18:00:00','2023-05-20 18:00:00', '89 Kukatpally, Hyderabad, Telangana 500072',991.34, 'Pending', 'CONF901567'),
(1, 23, '2023-05-20 11:00:00', '2023-05-25 14:00:00', '2023-05-30 14:00:00','2023-05-30 14:00:00','12 Miyapur, Hyderabad, Telangana 500049',615.34, 'Confirmed', 'CONF234890'),
(3, 11, '2023-05-30 15:30:00', '2023-06-04 10:00:00', '2023-06-09 16:00:00','2023-07-05 18:00:00', '123 Main Street, New Malakpet, Telangana 110001',892.33, 'Pending', 'CONF567123'),
(29, 25, '2023-06-05 12:00:00', '2023-06-10 09:00:00', '2023-06-15 18:00:00','2023-06-15 18:00:00', '57 Khairatabad, Hyderabad, Telangana 500004',237.23, 'Confirmed', 'CONF890456'),
(25, 29, '2023-06-15 10:00:00', '2023-06-20 12:00:00', '2023-06-25 12:00:00','2023-06-25 12:00:00', '21 Raj Bhavan Road, Hyderabad, Telangana 500004',938.2, 'Pending', 'CONF123789'),
(11, 3, '2023-06-25 14:30:00', '2023-06-30 09:00:00', '2023-07-05 18:00:00','2023-07-05 18:00:00', '57 Khairatabad, Hyderabad, Telangana 500004',736.2, 'Confirmed', 'CONF456012'),
(23, 1, '2023-07-01 16:00:00', '2023-07-05 10:00:00', '2023-07-10 16:00:00','2023-07-10 16:00:00', '66 Tarnaka, Hyderabad, Telangana 500017',9272.3, 'Pending',  'CONF789345'),
(13, 22, '2023-07-10 09:30:00', '2023-07-15 12:00:00', '2023-07-20 12:00:00','2023-07-20 12:00:00', '31 Uppal, Hyderabad, Telangana 500039',62636.43, 'Confirmed', 'CONF012678'),
(28, 14, '2023-07-20 14:00:00', '2023-07-25 09:00:00', '2023-07-30 18:00:00','2023-07-30 18:00:00', '57 Khairatabad, Hyderabad, Telangana 500004',673.32, 'Pending', 'CONF345901'),
(19, 4, '2023-05-01 09:00:00', '2023-05-05 12:00:00', '2023-05-10 12:00:00','2023-05-10 12:00:00', '67 Kondapur, Hyderabad, Telangana 500084',9372.33, 'Confirmed', 'CONF678234'),
(10, 2, '2023-05-10 14:30:00', '2023-05-15 09:00:00', '2023-05-20 18:00:00','2023-05-20 18:00:00', '89 Kukatpally, Hyderabad, Telangana 500072',83628.3, 'Pending', 'CONF901567'),
(16, 20, '2023-06-25 14:30:00', '2023-06-30 09:00:00', '2023-07-05 18:00:00','2023-07-05 18:00:00', '57 Khairatabad, Hyderabad, Telangana 500004',7362.34, 'Confirmed', 'CONF456012'),
(12, 18, '2023-07-10 09:30:00', '2023-07-15 12:00:00', '2023-07-20 12:00:00','2023-07-29 14:00:00', '31 Uppal, Hyderabad, Telangana 500039',287.43, 'Confirmed', 'CONF012678'),
(5, 9, '2023-05-01 09:00:00', '2023-05-05 12:00:00', '2023-05-10 12:00:00','2023-05-05 18:00:00', '67 Kondapur, Hyderabad, Telangana 500084',6536.33, 'Confirmed', 'CONF678234'),
(30, 15, '2023-07-20 14:00:00', '2023-07-25 09:00:00', '2023-07-30 18:00:00','2023-07-20 18:00:00', '57 Khairatabad, Hyderabad, Telangana 500004',8636.43, 'Pending', 'CONF345901'),
(27, 7, '2023-04-25 16:00:00', '2023-04-30 10:00:00', '2023-05-05 16:00:00','2023-05-10 12:00:00', '14 Ameerpet, Hyderabad, Telangana 500016',836.43, 'Pending', 'CONF345901'),
(6, 21, '2023-05-01 09:00:00', '2023-05-05 12:00:00', '2023-05-10 12:00:00','2023-05-20 18:00:00', '67 Kondapur, Hyderabad, Telangana 500084',83762.45, 'Confirmed', 'CONF678234'),
(24, 17, '2023-05-10 14:30:00', '2023-05-15 09:00:00', '2023-05-20 18:00:00','2023-5-30 18:00:00', '89 Kukatpally, Hyderabad, Telangana 500072',937.34, 'Pending', 'CONF901567'),
(26, 8, '2023-05-20 11:00:00', '2023-05-25 14:00:00', '2023-05-30 14:00:00','2023-05-30 14:00:00', '12 Miyapur, Hyderabad, Telangana 500049',736474, 'Confirmed', 'CONF234890');



-- Create the Payment_Details table
CREATE TABLE IF NOT EXISTS Payment_Details (
    Payment_ID INT AUTO_INCREMENT PRIMARY KEY,
    Payment_method VARCHAR(20) NOT NULL,
    Total_cost DECIMAL(10, 2) NOT NULL,
    Payment_date DATE NOT NULL,
    Late_fee DECIMAL(10, 2),
    Reservation_ID INT NOT NULL,
    FOREIGN KEY (Reservation_ID) REFERENCES Reservation(Reservation_ID)
);


INSERT INTO Payment_Details (Payment_method, Total_cost, Payment_date, Late_fee, Reservation_ID) VALUES
('Credit Card', 5000.00, '2023-03-10', 0.00, 1),
('Debit Card', 7500.00, '2023-03-25', 500.00, 3),
('Online Banking', 6000.00, '2023-04-10', 0.00, 5),
('Credit Card', 8000.00, '2023-04-20', 0.00, 7),
('Debit Card', 7000.00, '2023-04-30', 1000.00, 9),
('Online Banking', 4500.00, '2023-03-20', 0.00, 2),
('Credit Card', 9000.00, '2023-04-04', 500.00, 4),
('Debit Card', 6500.00, '2023-04-15', 0.00, 6),
('Online Banking', 7000.00, '2023-04-25', 0.00, 8),
('Credit Card', 8500.00, '2023-05-05', 1500.00, 10),
('Debit Card', 6000.00, '2023-05-10', 0.00, 12),
('Online Banking', 9000.00, '2023-05-20', 500.00, 14),
('Credit Card', 5500.00, '2023-05-30', 0.00, 16),
('Debit Card', 8000.00, '2023-06-09', 1000.00, 18),
('Online Banking', 7500.00, '2023-06-15', 0.00, 20),
('Credit Card', 6000.00, '2023-06-25', 500.00, 22),
('Debit Card', 8500.00, '2023-07-05', 0.00, 24),
('Online Banking', 5000.00, '2023-07-10', 0.00, 26),
('Credit Card', 7000.00, '2023-07-20', 1000.00, 28),
('Debit Card', 6500.00, '2023-07-30', 0.00, 30),
('Online Banking', 4000.00, '2023-03-20', 0.00, 2),
('Credit Card', 7500.00, '2023-04-04', 500.00, 4),
('Debit Card', 5500.00, '2023-04-15', 0.00, 6),
('Online Banking', 6000.00, '2023-04-25', 0.00, 8),
('Credit Card', 7000.00, '2023-05-05', 1000.00, 10),
('Debit Card', 5000.00, '2023-05-10', 0.00, 12),
('Online Banking', 8000.00, '2023-05-20', 500.00, 14),
('Credit Card', 4500.00, '2023-05-30', 0.00, 16),
('Debit Card', 7000.00, '2023-06-09', 1000.00, 18),
('Online Banking', 6500.00, '2023-06-15', 0.00, 20);




-- Create the Feedback table
CREATE TABLE IF NOT EXISTS Feedback (
    Feedback_ID INT AUTO_INCREMENT PRIMARY KEY,
    Content TEXT NOT NULL,
    Rating INT NOT NULL,
    Customer_ID INT NOT NULL,
    Reservation_ID INT NOT NULL,
    FOREIGN KEY (Customer_ID) REFERENCES Customer_details(Customer_ID),
    FOREIGN KEY (Reservation_ID) REFERENCES Reservation(Reservation_ID)
);


INSERT INTO Feedback (Content, Rating, Customer_ID, Reservation_ID) VALUES
('The car was clean and well-maintained. Excellent service!', 5, 2, 1),
('The pick-up process was a bit slow, but the car was in good condition.', 4, 5, 3),
('The vehicle had some minor scratches, but overall, a satisfactory experience.', 3, 8, 5),
('Prompt service and a smooth rental process. Highly recommended!', 5, 11, 7),
('The car was not very clean, and the customer service could have been better.', 2, 14, 9),
('The rental process was hassle-free, and the car was perfect for our trip.', 4, 3, 2),
('The vehicle had some issues with the brakes, which was concerning.', 2, 6, 4),
('The staff was friendly and accommodating. Great experience overall.', 5, 9, 6),
('The car was a bit outdated, but the pricing was reasonable.', 3, 12, 8),
('The rental process was smooth, but the car had some minor dents.', 4, 15, 10),
('The vehicle was well-maintained, and the customer service was excellent.', 5, 18, 12),
('The pick-up and drop-off locations were convenient, making the rental process easy.', 4, 21, 14),
('The car had some issues with the air conditioning, which was a bit disappointing.', 3, 24, 16),
('The rental experience was seamless from start to finish. Highly recommended!', 5, 27, 18),
('The vehicle was not very clean, and the customer service could have been better.', 2, 30, 20),
('The rental process was hassle-free, and the car was perfect for our trip.', 4, 2, 22),
('The vehicle had some minor scratches, but overall, a satisfactory experience.', 3, 5, 24),
('Prompt service and a smooth rental process. Highly recommended!', 5, 8, 26),
('The car was not very clean, and the customer service could have been better.', 2, 11, 28),
('The rental process was smooth, but the car had some minor dents.', 4, 14, 30),
('The vehicle was well-maintained, and the customer service was excellent.', 5, 3, 2),
('The pick-up and drop-off locations were convenient, making the rental process easy.', 4, 6, 4),
('The car had some issues with the air conditioning, which was a bit disappointing.', 3, 9, 6),
('The rental experience was seamless from start to finish. Highly recommended!', 5, 12, 8),
('The vehicle was not very clean, and the customer service could have been better.', 2, 15, 10),
('The rental process was hassle-free, and the car was perfect for our trip.', 4, 18, 12),
('The vehicle had some minor scratches, but overall, a satisfactory experience.', 3, 21, 14),
('Prompt service and a smooth rental process. Highly recommended!', 5, 24, 16),
('The car was not very clean, and the customer service could have been better.', 2, 27, 18),
('The rental process was smooth, but the car had some minor dents.', 4, 30, 20);