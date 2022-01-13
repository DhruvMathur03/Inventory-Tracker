from flask import Flask, render_template, request
import database
import user_side

app = Flask(__name__, template_folder='template')

db = database.DB('inventory_tracker.db')
user = user_side.User('inventory_tracker.db')

@app.route('/home', methods=['GET'])
def home():
    inv_data = user.view_inventory()
    inv_ids = map(lambda row: row[0], inv_data)
    ship_data = user.view_shipments()
    ship_details_data = user.view_shipment_details()
    return render_template('home.html', Inventory=inv_data, Shipment=ship_data, Shipment_Details=ship_details_data, IDs=list(inv_ids))

@app.route('/create-inv', methods=['POST'])
def create_inventory():
    data = user.view_inventory()
    if data == []:
        new_id = 1
    else:
        prev_ID = data[-1][0]
        new_id = prev_ID + 1
    item_name = request.form['name']
    item_desc = request.form['description']
    quantity = request.form['quantity']
    user.create_item(new_id, item_name, item_desc, quantity)
    return "succesfully created"

@app.route('/create-shipment', methods=['POST'])
def create_shipment():
    data = user.view_shipments()
    if data == []:
        new_id = 1
    else:
        prev_ID = data[-1][0]
        new_id = prev_ID + 1
    shipment_desc = request.form['desc']
    carrier = request.form['carrier']
    tracking_num = request.form['tracking']
    is_exp = request.form['is_exp']
    user.create_shipment(new_id, shipment_desc, carrier, tracking_num, is_exp)
    return "succesfully created"

@app.route('/shipment-details', methods=['POST'])
def shipment_details():
    inv_data = user.view_inventory()
    inv_id = request.form['inv_id']
    ship_id = request.form['ship_id']
    quantity = request.form['quantity']
    cur_quantity = inv_data[int(inv_id)-1][3]
    new_quantity = str(cur_quantity - int(quantity))
    user.shipment(inv_id, ship_id, quantity)
    user.update_inv(f'Quantity = {new_quantity}', f'ID = {inv_id}')
    return "succesfully added"

@app.route('/delete-inv', methods=['POST'])
def delete_inv():
    ID = request.form['id']
    db.delete('inventory', f'ID={ID}')
    return "succesfully deleted"

@app.route('/delete-shipment', methods=['POST'])
def delete_ship():
    ID = request.form['id']
    db.delete('shipments', f'ID={ID}')
    return "succesfully deleted"

@app.route('/delete-deet', methods=['POST'])
def delete_deet():
    inv_id = request.form['inv_id']
    ship_id = request.form['ship_id']
    db.delete('shipment_details', f'Inventory_ID = {inv_id} AND Shipment_ID = {ship_id}')
    return "succesfully deleted"

@app.route('/update-inv', methods=['POST'])
def update_inv():
    cur_id = request.form['id']
    data = request.form
    if data['name'] != '':
        name = data['name']
        user.update_inv(f'Item_Name="{name}"', f'ID={cur_id}')
    if data['description'] != '':
        desc = data['description']
        user.update_inv(f'Item_Description="{desc}"', f'ID={cur_id}')
    if data['quantity'] != '':
        quantity = data['quantity']
        user.update_inv(f'Quantity="{quantity}"', f'ID={cur_id}')
    return "succesfully updated"

@app.route('/update-ship', methods=['POST'])
def update_ship():
    cur_id = request.form['id']
    data = request.form
    if data['desc'] != '':
        desc = data['desc']
        user.update_ship(f'Shipment_Description="{desc}"', f'ID={cur_id}')
    if data['carrier'] != '':
        carrier = data['carrier']
        user.update_ship(f'Carrier="{carrier}"', f'ID={cur_id}')
    if data['tracking'] != '':
        tracking = data['tracking']
        user.update_ship(f'Tracking_Number="{tracking}"', f'ID={cur_id}')
    if data['is_exp'] != '':
        is_exp = data['is_exp']
        user.update_ship(f'Is_Expedited="{is_exp}"', f'ID={cur_id}')
    return "succesfully updated"
    
@app.route('/update-deet', methods=['POST'])
def update_deet():
    inv_data = user.view_inventory()
    inv_id = request.form['inv_id']
    ship_id = request.form['ship_id']
    cur_quantity = request.form['cur_q']
    data = request.form
    item_cur_quantity = inv_data[int(inv_id)-1][3]
    if data['quantity'] != '':
        new_quantity = data['quantity']
        diff_quantity = int(cur_quantity) - int(new_quantity) 
        user.update_details(f'Quantity="{new_quantity}"', f'Inventory_ID={inv_id} AND Shipment_ID={ship_id}')
        item_new_quantity = item_cur_quantity + diff_quantity
        user.update_inv(f'Quantity="{item_new_quantity}"', f'ID={inv_id}')
    return "succesfully updated"

if __name__ == "__main__":
    app.run(debug=True)
