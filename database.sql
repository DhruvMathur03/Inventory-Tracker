-- Create Table (inventory)
CREATE TABLE inventory (
    ID INT PRIMARY KEY, 
    Item_Name VARCHAR(256), 
    Item_Description VARCHAR(256), 
    Quantity INT,
    Created_At DATE,
    Updated_At DATE); 

-- Create Table (shipments)
CREATE TABLE shipments (
    ID INT PRIMARY KEY, 
    Shipment_Description VARCHAR(256), 
    Carrier VARCHAR(256),
    Tracking_Number VARCHAR(256) UNIQUE,
    Is_Expedited INT CHECK (0=Is_Expedited or Is_Expedited=1),
    Created_At DATE,
    Updated_At DATE);

-- Create Table (shipment_details)
CREATE TABLE shipment_details (
    Inventory_ID INT, 
    Shipment_ID INT,
    Quantity INT,  
    Created_At DATE,
    Updated_At DATE);

