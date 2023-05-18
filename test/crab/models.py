from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from crab.utiles.models_logic import BaseModel

# All models inherit from BaseModel which contains 3 default fields: id, created_at, updated_at

class Addresses(BaseModel):
    __tablename__ = 'addresses'
    street = Column(String(50))
    city = Column(String(50))
    province = Column(String(50))
    zip_code = Column(String(10))
    residents_ids = relationship("Residents", backref="addresses")

class Residents(BaseModel):
    __tablename__ = 'residents'
    name = Column(String(50))
    age = Column(String(50))
    address_id = Column(Integer, ForeignKey('addresses.id'))
