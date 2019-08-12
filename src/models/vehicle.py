from marshmallow import fields, Schema
import datetime
from . import db


class VehicleModel(db.Model):
    """
    Vehicle Model
    """
    # table name
    __tablename__ = 'vehicles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    model = db.Column(db.String(128))
    manufacturer = db.Column(db.String(128))
    cost_in_credits = db.Column(db.String(128))
    length = db.Column(db.String(128))
    max_atmosphering_speed = db.Column(db.String(128))
    crew = db.Column(db.String(128))
    passengers = db.Column(db.String(128))
    cargo_capacity = db.Column(db.String(128))
    vehicle_class = db.Column(db.String(128))
    created = db.Column(db.String(128))
    edited = db.Column(db.String(128))

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.name = data.get('name')
        self.model = data.get('model')
        self.manufacturer = data.get('manufacturer')
        self.cost_in_credits = data.get('cost_in_credits')
        self.length = data.get('length')
        self.max_atmosphering_speed = data.get('max_atmosphering_speed')
        self.crew = data.get('crew')
        self.passengers = data.get('passengers')
        self.cargo_capacity = data.get('cargo_capacity')
        self.vehicle_class = data.get('vehicle_class')
        self.created = datetime.datetime.utcnow()
        self.edited = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
            self.edited = datetime.datetime.utcnow()
            db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_vehicles():
        return VehicleModel.query.all()

    @staticmethod
    def get_one_vehicle(id):
        return VehicleModel.query.get(id)

    def __repr(self):
        return '<id {}>'.format(self.id)


class VehicleSchema(Schema):
    """
    Vehicle Schema
    """

    id = fields.Int(dump_only=True)
    model = fields.Str(required=True)
    manufacturer = fields.Str(required=True)
    cost_in_credits = fields.Str(required=True)
    length = fields.Str(required=True)
    max_atmosphering_speed = fields.Str(required=True)
    crew = fields.Str(required=True)
    passengers = fields.Str(required=True)
    cargo_capacity = fields.Str(required=True)
    vehicle_class = fields.Str(required=True)
    created = fields.Str(required=True)
    edited = fields.Str(required=True)
