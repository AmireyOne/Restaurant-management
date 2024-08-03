from sqlalchemy import   Column , Integer , String ,TEXT , create_engine ,NVARCHAR , VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from pyodbc import *
# from be.Setting import Setting
# conn=Setting().GetConnection()
engine=create_engine("mssql+pyodbc://amir:123@./Restaurant_Management?driver=ODBC+Driver+17+for+SQL+Server")
Base=declarative_base()


class Customer(Base):
    __tablename__='Customer'
    Id=Column(Integer , primary_key=True)
    NameCustomer=Column(NVARCHAR)
    FamilyCustomer=Column(NVARCHAR)
    PhoneCustomer=Column(VARCHAR)
    def __init__(self , Name="" , Family="" , Phone=0):
        self.NameCustomer=Name
        self.FamilyCustomer=Family
        self.PhoneCustomer=Phone


class Personnel(Base):
    __tablename__='Personnel'
    Id = Column(Integer, primary_key=True)
    NamePersonnel = Column(NVARCHAR)
    FamilyPersonnel = Column(NVARCHAR)
    AgePersonnel=Column(Integer)
    PhonePersonnel = Column(VARCHAR)
    SalaryPersonnel=Column(VARCHAR)
    def __init__(self, Name="", Family="",Age=0, Phone=0 , Salary=0):

        self.NamePersonnel = Name
        self.FamilyPersonnel = Family
        self.AgePersonnel=Age
        self.PhonePersonnel = Phone
        self.SalaryPersonnel=Salary

class Food(Base):
    __tablename__='Food'
    Id=Column(Integer , primary_key=True)
    NameFood=Column(NVARCHAR)
    PriceFood=Column(VARCHAR)

    def __init__(self , NameFood="" , Price=0 ):
        self.NameFood=NameFood
        self.PriceFood=Price


class Drink(Base):
    __tablename__ = 'Drink'
    Id = Column(Integer, primary_key=True)
    NameDrink = Column(NVARCHAR)
    PriceDrink = Column(VARCHAR)

    def __init__(self, NameDrink="", Price=0):
        self.NameDrink = NameDrink
        self.PriceDrink = Price


class Mokhalafat(Base):
    __tablename__ = 'Mokhalafat'
    Id = Column(Integer, primary_key=True)
    NameMokhalafat = Column(NVARCHAR)
    PriceMokhalafat = Column(VARCHAR)
    def __init__(self, NameMokhalafat="", Price=0):
        self.NameMokhalafat = NameMokhalafat
        self.PriceMokhalafat = Price




