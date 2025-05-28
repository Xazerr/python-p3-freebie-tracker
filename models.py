from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)

# Company model
class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    founding_year = Column(Integer())

    freebies = relationship("Freebie", back_populates="company")

    def __repr__(self):
        return f"<Company name='{self.name}' founded in {self.founding_year}>"

# Developer model
class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)

    freebies = relationship("Freebie", back_populates="dev")

    def __repr__(self):
        return f"<Dev name='{self.name}'>"

# Freebie model
class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String(), nullable=False)
    value = Column(Integer())
    company_id = Column(Integer(), ForeignKey('companies.id'))
    dev_id = Column(Integer(), ForeignKey('devs.id'))

    company = relationship("Company", back_populates="freebies")
    dev = relationship("Dev", back_populates="freebies")

    def __repr__(self):
        return f"<Freebie '{self.item_name}' worth ${self.value}>"


