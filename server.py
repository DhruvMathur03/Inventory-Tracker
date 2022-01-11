from flask import Flask, render_template, request
import database
import user_side

app = Flask(__name__, template_folder='template')

db = database.DB('inventory_tracker.db')
user = user_side.User('inventory_tracker.db')

@app.route('/home', methods=['POST', 'GET'])

def home():
    inv_data = user.view_inventory()
    ship_data = user.view_shipments()
    ship_details_data = user.view_shipment_details()
    return render_template('home.html', Inventory=inv_data, Shipment=ship_data, Shipment_Details=ship_details_data)

def update_inventory():
    data = user.view_inventory()
    prev_ID = data[-1][0]
    item_name = request.form['Item Name']
    item_desc = request.form['Item Description']
    quantity = request.form['Quantity']
    user.create_item(prev_ID+1, item_name, item_desc, quantity)
    


if __name__ == "__main__":
    app.run(debug=True)
