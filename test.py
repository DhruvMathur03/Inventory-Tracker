from sqlite3 import IntegrityError
import unittest
from unittest.main import main
from urllib import response
from flask import Flask
from flask_testing import TestCase
import main_database

class Test(TestCase):

    def create_app(self):
        main_database.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        main_database.app.config['TESTING'] = True
        main_database.app.config['WTF_CSRF_ENABLED'] = False
        return main_database.app

    def setUp(self):
        main_database.db.create_all()
        inv_item = main_database.Inventory(Item_Name='Practice', Item_Description='Prac Desc', Quantity=23)
        ship_item = main_database.Shipments(Shipment_Description='Desc', Carrier='None', Tracking_Number='None', Is_Expedited=False)
        main_database.db.session.add_all([inv_item, ship_item])
        main_database.db.session.commit()
        
    def tearDown(self):
        main_database.db.session.remove()
        main_database.db.drop_all()

class FlaskTestInventory(Test):
     
    # Tests for Inventory Table
    # Creates an item in the inventory table and checks if its been added to the table
    def test_create(self):
        item = main_database.Inventory(Item_Name='Test1', Item_Description='Description', Quantity=43)
        main_database.db.session.add(item)
        main_database.db.session.commit()
        response = main_database.Inventory.query.all()
        self.assertGreaterEqual(len(response), 2)

    # Creates new item with non-unique ID, and checks if exception is raised
    def test_same_id(self):
        item = main_database.Inventory(ID=1, Item_Name='ID Test', Item_Description='Desc', Quantity=231)
        main_database.db.session.add(item)
        with self.assertRaises(Exception):
            main_database.db.session.commit()

    # Updates existing item, and checks if the database updated the item in 
    def test_update(self):
        main_database.Inventory.update(1, 'Item_Name', 'Test Update Successful')
        response = main_database.Inventory.query.get(1)
        self.assertEqual(response.Item_Name, 'Test Update Successful')
        
    # Updates item that isn't present in the table and checks if exception is raised    
    def test_absent_item_update(self):
        with self.assertRaises(Exception):
            main_database.Inventory.update(4, 'Item_Name', 'Test Update')
        
    # Deletes existing item from table, and checks if change has taken place in the database
    def test_delete(self):
        main_database.Inventory.query.filter_by(ID=1).delete()
        main_database.db.session.commit()
        resp = main_database.Inventory.query.all()
        self.assertEqual(len(resp), 0)
        
    # Deletes an item that isn't present in the table and checks if exception is raised    
    def test_absent_item_delete(self):
        with self.assertRaises(Exception):
            main_database.Inventory.query.get(103).delete()
            main_database.db.session.commit()

class FlaskTestShipment(Test):
     
    # Tests for Shipment Table
    # Creates a shipment in the shipments table and checks if its been added to the table
    def test_create(self):
        item = main_database.Inventory(Item_Name='Test1', Item_Description='Description', Quantity=43)
        main_database.db.session.add(item)
        main_database.db.session.commit()
        response = main_database.Inventory.query.all()
        self.assertGreaterEqual(len(response), 2)

    # Creates new item with non-unique ID, and checks if exception is raised
    def test_same_id(self):
        item = main_database.Inventory(ID=1, Item_Name='ID Test', Item_Description='Desc', Quantity=231)
        main_database.db.session.add(item)
        with self.assertRaises(Exception):
            main_database.db.session.commit()

    # Updates existing item, and checks if the database updated the item in 
    def test_update(self):
        main_database.Inventory.update(1, 'Item_Name', 'Test Update Successful')
        response = main_database.Inventory.query.get(1)
        self.assertEqual(response.Item_Name, 'Test Update Successful')
        
    # Updates item that isn't present in the table and checks if exception is raised    
    def test_absent_item_update(self):
        with self.assertRaises(Exception):
            main_database.Inventory.update(4, 'Item_Name', 'Test Update')
        
    # Deletes existing item from table, and checks if change has taken place in the database
    def test_delete(self):
        main_database.Inventory.query.filter_by(ID=1).delete()
        main_database.db.session.commit()
        resp = main_database.Inventory.query.all()
        self.assertEqual(len(resp), 0)
        
    # Deletes an item that isn't present in the table and checks if exception is raised    
    def test_absent_item_delete(self):
        with self.assertRaises(Exception):
            main_database.Inventory.query.get(103).delete()
            main_database.db.session.commit()



if __name__=='__main__':
    unittest.main()

    


