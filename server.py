from flask import Flask, render_template, request
import database
import user_side

app = Flask(__name__, template_folder='template')

db = database.DB('inventory_tracker.db')
user = user_side.User('inventory_tracker.db')

@app.route('/home', methods=['GET'])
def home():
    inv_data = user.view_inventory()
    ship_data = user.view_shipments()
    ship_details_data = user.view_shipment_details()
    return render_template('home.html', Inventory=inv_data, Shipment=ship_data, Shipment_Details=ship_details_data)

@app.route('/create-inv', methods=['POST'])
def create_inventory():
    data = user.view_inventory()
    prev_ID = data[-1][0]
    item_name = request.form['name']
    item_desc = request.form['description']
    quantity = request.form['quantity']
    user.create_item(prev_ID+1, item_name, item_desc, quantity)
    return "succesfully created"

@app.route('/create-shipment', methods=['POST'])
def create_shipment():
    data = user.view_shipments()
    prev_ID = data[-1][0]
    shipment_desc = request.form['desc']
    carrier = request.form['carrier']
    tracking_num = request.form['tracking']
    is_exp = request.form['is_exp']
    user.create_shipment(prev_ID+1, shipment_desc, carrier, tracking_num, is_exp)
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
    return new_quantity

@app.route('/delete-inv', methods=['POST'])
def delete_inv():
    ID = request.form['ID']
    db.delete('inventory', f'ID={ID}')
    return "succesfully deleted"

@app.route('/delete-shipment', methods=['POST'])
def delete_ship():
    ID = request.form['ID']
    db.delete('shipment', f'ID={ID}')
    return "succesfully deleted"


    


if __name__ == "__main__":
    app.run(debug=True)
