from ast import In
from datetime import date
from operator import and_, inv
from tty import setraw
from unittest.main import main
from webbrowser import MacOSX
from flask import render_template, request
import main_database

app = main_database.app

@app.route('/home', methods=['GET'])
def home():
    inv_data = main_database.Inventory.query.all()
    ship_data = main_database.Shipments.query.all()
    ship_details_data = main_database.Shipment_Details.query.all()
    return render_template('home.html', Inventory=inv_data, Shipment=ship_data, Shipment_Details=ship_details_data)

@app.route('/create-inv', methods=['POST'])
def create_inventory():
    item_name = request.form['name']
    item_desc = request.form['description']
    quantity = request.form['quantity']
    item = main_database.Inventory(Item_Name=item_name, Item_Description=item_desc, Quantity=quantity)
    main_database.db.session.add(item)
    main_database.db.session.commit()
    return "succesfully created"

@app.route('/create-shipment', methods=['POST'])
def create_shipment():
    shipment_desc = request.form['desc']
    carrier = request.form['carrier']
    tracking_num = request.form['tracking']
    is_exp = request.form['is_exp']
    shipment = main_database.Shipments(Shipment_Description=shipment_desc, Carrier=carrier, Tracking_Number=tracking_num, Is_Expedited=is_exp=='True')
    main_database.db.session.add(shipment)
    main_database.db.session.commit()
    return "succesfully created"

@app.route('/shipment-details', methods=['POST'])
def shipment_details():
    inv_id = request.form['inv_id']
    ship_id = request.form['ship_id']
    quantity = request.form['quantity']
    inv_data = main_database.Inventory.query.get(inv_id)
    if main_database.Inventory.query.get(inv_id) == None or main_database.Shipments.query.get(ship_id) == None:
        return "Item or Shipment doesn't exist"
    elif main_database.Inventory.query.get(inv_id).Quantity == 0 or main_database.Inventory.query.get(inv_id).State == 'Deleted':
        return "Item is out of stock"
    else:
        cur_quantity = inv_data.Quantity
        new_quantity = str(cur_quantity - int(quantity))
        detail = main_database.Shipment_Details(Inventory_ID=inv_id, Shipment_ID=ship_id, Quantity=quantity)
        main_database.db.session.add(detail)
        main_database.Inventory.update(inv_id, 'Quantity', new_quantity)
        return "succesfully added"

@app.route('/delete-inv', methods=['POST'])
def delete_inv():
    ID = request.form['id']
    main_database.Inventory.update(ID, 'State', 'Deleted')
    return "succesfully deleted"

@app.route('/delete-shipment', methods=['POST'])
def delete_ship():
    ID = request.form['id']
    main_database.Shipments.query.filter_by(ID=f'{ID}').delete()
    main_database.db.session.commit()
    return "succesfully deleted"

@app.route('/delete-deet', methods=['POST'])
def delete_deet():
    inv_id = request.form['inv_id']
    ship_id = request.form['ship_id']
    cur_quantity = main_database.Inventory.query.get(inv_id).Quantity
    shipment = main_database.Shipment_Details.query.filter_by(Inventory_ID=f'{inv_id}').filter_by(Shipment_ID=f'{ship_id}')
    main_database.Inventory.update(inv_id, 'Quantity', cur_quantity+shipment.Quantity)
    main_database.db.session.delete(shipment)
    main_database.db.session.commit()
    return "succesfully deleted"

@app.route('/update-inv', methods=['POST'])
def update_inv():
    cur_id = request.form['id']
    row = main_database.Inventory.query.get(cur_id)
    data = request.form
    if data['name'] != '':
        name = data['name']
        main_database.Inventory.update(cur_id, 'Item_Name', name)
    if data['description'] != '':
        desc = data['description']
        main_database.Inventory.update(cur_id, 'Item_Description', desc)
    if data['quantity'] != '':
        quantity = data['quantity']
        main_database.Inventory.update(cur_id, 'Quantity', quantity)
        if quantity == "0":
            main_database.Inventory.update(cur_id, 'State', 'Out of Stock')
        if row.State == 'Out of Stock' and int(quantity) > 0:
            main_database.Inventory.update(cur_id, 'State', 'In Stock')
    main_database.Inventory.update(cur_id, 'Updated_At', date.today())
    return "succesfully updated"

@app.route('/update-ship', methods=['POST'])
def update_ship():
    cur_id = request.form['id']
    data = request.form
    shipment = main_database.Shipments.query.get(cur_id)
    if data['desc'] != '':
        desc = data['desc']
        setattr(shipment, 'Shipment_Description', desc)
        main_database.db.session.add(shipment)
    if data['carrier'] != '':
        carrier = data['carrier']
        setattr(shipment, 'Carrier', carrier)
        main_database.db.session.add(shipment)
    if data['tracking'] != '':
        tracking = data['tracking']
        setattr(shipment, 'Tracking_Number', tracking)
        main_database.db.session.add(shipment)
    if data['is_exp'] != '':
        is_exp = data['is_exp']
        setattr(shipment, 'Is_Expedited', is_exp=='True')
        main_database.db.session.add(shipment)
    setattr(shipment, 'Updated_At', date.today())
    main_database.db.session.commit()
    return "succesfully updated"
    
@app.route('/update-deet', methods=['POST'])
def update_deet():
    inv_id = request.form['inv_id']
    ship_id = request.form['ship_id']
    cur_quantity = request.form['cur_q']
    inv_data = main_database.Inventory.query.get(inv_id)
    data = request.form
    item_cur_quantity = inv_data.Quantity
    if data['quantity'] != '':
        new_quantity = data['quantity']
        diff_quantity = int(cur_quantity) - int(new_quantity) 
        detail = main_database.Shipment_Details.query.filter_by(Inventory_ID=inv_id).filter_by(Shipment_ID=ship_id)
        setattr(detail.first(), 'Quantity', new_quantity)
        main_database.db.session.commit()
        setattr(detail.first(), 'Updated_At', date.today())
        main_database.db.session.commit()
        item_new_quantity = item_cur_quantity + diff_quantity
        main_database.Inventory.update(inv_id, 'Quantity', item_new_quantity)
        main_database.Inventory.update(inv_id, 'Updated_At', date.today())
    return "succesfully updated"

if __name__ == "__main__":
    app.run(debug=True)
