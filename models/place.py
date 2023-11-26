#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id =Column(String(60), ForeignKey('cities.id') nullable=False) 
    user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Interger, default=0, nullable=False)
    number_bathrooms = Column(Interger, default=0, nullable=False )
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, default=0.0, nullable=False)
    longitude = Column(Float, default=0.0, nullable=False)
    amenity_ids = []
