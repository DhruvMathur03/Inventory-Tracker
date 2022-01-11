-- Add to Inventory
INSERT INTO 
    inventory(ID, Item_Name, Item_Description, Quantity, Created_At, Updated_At) 
    VALUES(1, "Pug", "smol puggo", 5, "2022-01-10", "None");

-- Add to Shipment
INSERT INTO 
    shipments(ID, Shipment_Description, Carrier, Is_Expedited, Created_At, Updated_At)
    VALUES(1, "Pug's Shipment", "CanadaPost", 0, "2022-01-10", "None");

-- Add to Shipment Details
INSERT INTO
    shipment_details(Inventory_ID, Shipment_ID, Quantity, Created_At, Updated_At)
    VALUES(1, 1, 3, "2022-01-10", "None");

