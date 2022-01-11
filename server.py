from flask import Flask, render_template
import database
import user_side

app = Flask(__name__, template_folder='template')

db = database.DB('inventory_tracker.db')
user = user_side.User('inventory_tracker.db')

@app.route('/home')
def home():
    inv_data = user.view_inventory()
    ship_data = user.view_shipments()
    ship_details_data = user.view_shipment_details()
    return render_template('home.html', Inventory=inv_data[0], Shipment=ship_data[0])

if __name__ == "__main__":
    app.run(debug=True)
