import main_database

def add_to_inventory():
    item = main_database.Inventory(Item_Name='Test Item', Item_Description='Test Desc', Quantity=55)
    item2 = main_database.Inventory(Item_Name='Test Item 2', Item_Description='Test 2 Desc', Quantity=134)
    item3 = main_database.Inventory(Item_Name='Test Item 3', Item_Description='Test 3 Desc', Quantity=5)
    main_database.db.session.add_all([item, item2, item3])
    main_database.db.session.commit()

def add_to_shipments():
    shipment = main_database.Shipments(Shipment_Description='Test', Carrier='None', Tracking_Number='None', Is_Expedited=False)
    shipment2 = main_database.Shipments(Shipment_Description='Test 2', Carrier='CanadaPost', Tracking_Number='EFAF21', Is_Expedited=True)
    shipment3 = main_database.Shipments(Shipment_Description='Test 3', Carrier='UPS', Tracking_Number='WAJFL1357', Is_Expedited=True)
    main_database.db.session.add_all([shipment, shipment2, shipment3])
    main_database.db.session.commit()

def add_to_shipment_details():
    detail = main_database.Shipment_Details(Inventory_ID=1, Shipment_ID=1, Quantity=21)
    detail2 = main_database.Shipment_Details(Inventory_ID=2, Shipment_ID=3, Quantity=32)
    detail3 = main_database.Shipment_Details(Inventory_ID=2, Shipment_ID=2, Quantity=65)
    main_database.db.session.add_all([detail, detail2, detail3])
    main_database.db.session.commit()

add_to_inventory()
add_to_shipments()
add_to_shipment_details()









