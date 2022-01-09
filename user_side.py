import sqlite3 as sql
from datetime import date
import database

class User:
    db_name = None

    def __init__(self, db_name):
        self.db_name = db_name
    
    def view_inventory(self):
        data = self.db_name.view_all('inventory')
        return data
    
    def view_shipments(self):
        data = self.db_name.view_all('shipments')
        return data
    
    def view_shipment_details(self):
        data = self.db_name.view_all('shipment_details')
        return data
    
    def create_item(self, ID, item_name, item_desc, quantity):
        today = date.today()
        self.db_name.insert('inventory', {
            'ID':ID, 'Item_Name':item_name, 'Item_Description':item_desc,
            'Quantity':quantity, 'Created_At':today, 'Updated_At':None})
    
    def create_shipment(self, ID, shipment_desc, carrier, tracking_number, is_expedited):
        today = date.today()
        self.db_name.insert('shipments', {
            'ID':ID, 'Shipment_Description':shipment_desc, 'Carrier':carrier,
            'Tracking_Number':tracking_number, 'Is_Expedited':is_expedited,
            'Created_At':today, 'Updated_At':None})
        
    def shipment(self, inv_id, ship_id, quantity):
        today = date.today()
        self.db_name.insert('shipment_details', {
            'Inventory_ID':inv_id, 'Shipment_ID':ship_id, 'Quantity':quantity,
            'Created_At':today, 'Updated_At':None})
    



        

