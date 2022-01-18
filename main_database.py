from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inv_tracker.db'
db = SQLAlchemy(app)

class Inventory(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Item_Name = db.Column(db.String(256))
    Item_Description = db.Column(db.String(256))
    Quantity = db.Column(db.Integer)
    Created_At = db.Column(db.DateTime, default=date.today)
    Updated_At = db.Column(db.DateTime, default=None)
    ship_details = db.relationship('Shipment_Details', backref='inv_id', lazy=True)

    def __repr__(self):
        return f'{self.ID}, {self.Item_Name}, {self.Item_Description}, {self.Quantity}, {self.Created_At}, {self.Updated_At}'

    def update(id, column, value):
        item_to_update = Inventory.query.get(id)
        setattr(item_to_update, column, value)
        db.session.commit()

class Shipments(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Shipment_Description = db.Column(db.String(256))
    Carrier = db.Column(db.String(256))
    Tracking_Number = db.Column(db.String(256), unique=True)
    Is_Expedited = db.Column(db.Boolean)
    Created_At = db.Column(db.DateTime, default=date.today)
    Updated_At = db.Column(db.DateTime, default=None)
    ship_details = db.relationship('Shipment_Details', backref='ship_id', lazy=True)

    def __repr__(self):
        return f'{self.ID}, {self.Shipment_Description}, {self.Carrier}, {self.Tracking_Number}, {self.Created_At}, {self.Updated_At}'

class Shipment_Details(db.Model):
    Inventory_ID = db.Column(db.Integer, db.ForeignKey('inventory.ID'), unique=False)
    Shipment_ID = db.Column(db.Integer, db.ForeignKey('shipments.ID'), unique=False)
    Quantity = db.Column(db.Integer)
    Created_At = db.Column(db.DateTime, default=date.today)
    Updated_At = db.Column(db.DateTime, default=None)
    __table_args__ = (
        db.PrimaryKeyConstraint(Inventory_ID, Shipment_ID),
        {}, 
    )

    def __repr__(self):
        return f'{self.Inventory_ID}, {self.Shipment_ID}, {self.Quantity}, {self.Created_At}, {self.Updated_At}'