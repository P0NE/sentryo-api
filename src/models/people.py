from marshmallow import fields, Schema
import datetime
from . import db
from .vehicle import VehicleModel, VehicleSchema
from sqlalchemy import Column, Integer, ForeignKey


class PeopleModel(db.Model):
    """
    People Model
    """
    # table name
    __tablename__ = 'people'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    height = db.Column(db.String(128))
    mass = db.Column(db.String(128))
    hair_color = db.Column(db.String(128))
    skin_color = db.Column(db.String(128))
    eye_color = db.Column(db.String(128))
    birth_year = db.Column(db.String(128))
    gender = db.Column(db.String(128))
    homeworld = db.Column(db.String(128))
    created = db.Column(db.String(128))
    edited = db.Column(db.String(128))
    vehicles = db.relationship('VehicleModel', secondary='people_vehicles')

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.name = data.get('name')
        self.height = data.get('height')
        self.mass = data.get('mass')
        self.hair_color = data.get('hair_color')
        self.skin_color = data.get('skin_color')
        self.eye_color = data.get('eye_color')
        self.birth_year = data.get('birth_year')
        self.gender = data.get('gender')
        self.homeworld = data.get('homeworld')
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
    def get_all_peoples():
        return PeopleModel.query.all()

    @staticmethod
    def get_one_people(id):
        return PeopleModel.query.get(id)

    def __repr(self):
        return '<id {}>'.format(self.id)


class PeopleSchema(Schema):
    """
    People Schema
    """

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    height = fields.Str(required=True)
    mass = fields.Str(required=True)
    hair_color = fields.Str(required=True)
    skin_color = fields.Str(required=True)
    eye_color = fields.Str(required=True)
    birth_year = fields.Str(required=True)
    gender = fields.Str(required=True)
    homeworld = fields.Str(required=True)
    created = fields.Str(required=True)
    edited = fields.Str(required=True)
    vehicles = fields.Nested(VehicleSchema, many=True)


class PeopleVehiclesLink(db.Model):
    __tablename__ = 'people_vehicles'
    people = Column(Integer, ForeignKey('people.id'), primary_key=True)
    vehicles = Column(Integer, ForeignKey('vehicles.id'), primary_key=True)
