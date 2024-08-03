from sqlalchemy.orm import Session , sessionmaker
from sqlalchemy import create_engine
from tkinter import messagebox

engine=create_engine("mssql+pyodbc://amir:123@./Restaurant_Management?driver=ODBC+Driver+17+for+SQL+Server")
Sessions=sessionmaker(bind=engine)
session=Sessions()

class Repository():
    def Add(self , obj):
        session.add(obj)
        session.commit()
        return True


    def Read(self , obj):
        result=session.query(obj).all()
        return result

    def ReadForCustomer(self ,obj, name , family , phone):
        resualt=session.query(obj).filter(obj.NameCustomer==name and obj.FamilyCustomer==family and obj.PhoneCustomer==phone).first()
        return resualt

    def ReadForPersonnel(self ,obj, name , family ,age, phone , salary):
        resualt=session.query(obj).filter(obj.NamePersonnel==name and obj.FamilyPersonnel==family and obj.AgePersonnel==age and obj.PhonePersonnel==phone and obj.SalaryPersonnel==salary).first()
        return resualt

    def ReadForFood(self ,obj, name , price):
        resualt=session.query(obj).filter(obj.NameFood==name and obj.PriceFood==price).first()
        return resualt

    def ReadForDrink(self ,obj, name, price):
        resualt=session.query(obj).filter(obj.NameDrink==name and obj.PriceDrinke==price).first()
        return resualt

    def ReadForMokhalafat(self ,obj, name, price):
        resualt=session.query(obj).filter(obj.NameMokhalafat==name and obj.NameMokhalafat==price).first()
        return resualt

    def UpdateCustomer(self ,obj, objnew, name , family , phone ):
        resualt=self.ReadForCustomer(obj, name , family , phone)
        resualt.NameCustomer=objnew.NameCustomer
        resualt.FamilyCustomer=objnew.FamilyCustomer
        resualt.PhoneCustomer=objnew.PhoneCustomer
        session.commit()
        return True

    def UpdatePersonnel(self ,obj , objnew, name , family ,age, phone , salary):
        resualt = self.ReadForPersonnel(obj, name, family, age, phone , salary)
        resualt.NamePersonnel = objnew.NamePersonnel
        resualt.FamilyPersonnel = objnew.FamilyPersonnel
        resualt.AgePersonnel = objnew.AgePersonnel
        resualt.PhonePersonnel = objnew.PhonePersonnel
        resualt.SalaryPersonnel = objnew.SalaryPersonnel
        session.commit()
        return True



    def UpdateFood(self ,obj,objnew, name ,price , ):
        resualt=self.ReadForFood(obj, name , price  )
        resualt.NameFood=objnew.NameFood
        resualt.PriceFood=objnew.PriceFood
        session.commit()
        return True

    def UpdateDrink(self ,obj,objnew, name , price , ):
        resualt=self.ReadForDrink(obj, name , price , )
        resualt.NameDrink = objnew.NameDrink
        resualt.PriceDrink = objnew.PriceDrink
        session.commit()
        return True
    def UpdateMokhalafat(self ,obj,objnew, name , price , ):
        resualt=self.ReadForMokhalafat(obj, name , price , )
        resualt.NameMokhalafat = objnew.NameMokhalafat
        resualt.PriceMokhalafat = objnew.PriceMokhalafat
        session.commit()
        return True
    def Delete(self , obj ):
        resualt=messagebox.askyesno("هشدار" , "آیا از حذف این مورد اطمینان دارید؟")
        if resualt==True:
            session.delete(obj)
            session.commit()
            return True
        else:
            return False

