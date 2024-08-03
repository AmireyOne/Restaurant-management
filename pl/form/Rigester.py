from tkinter import *
from tkinter import ttk
from be.ClassRestaurant import *
from dal.Repository import *




class App (Frame) :
    def __init__(self , screen):
        super().__init__(screen)
        self.master=screen
        self.CreateWedget()
        self.TakedataCustomer()
        self.TakedataPersonnel()
        self.TakedataFood()
        self.TakedataDrink()
        self.TakedataMokhalafat()

    def TakedataCustomer(self):
        rep = Repository()
        result = rep.Read(Customer)
        for item in result:
            listitem=[item.NameCustomer , item.FamilyCustomer , item.PhoneCustomer]
            self.insertCustomer(listitem)

    def TakedataPersonnel(self):


        rep=Repository()
        result=rep.Read(Personnel)
        for item in result:
            listitem = [item.NamePersonnel, item.FamilyPersonnel, item.AgePersonnel, item.PhonePersonnel, item.SalaryPersonnel]
            self.insertPersonnel(listitem)

    def TakedataFood(self):
        rep = Repository()
        result = rep.Read(Food)
        for item in result:
            listitem=[item.NameFood , item.PriceFood]
            self.insertServic(self.TblServiceFood,listitem)
            self.insertServic(self.TblframeFood , listitem)

    def TakedataDrink(self):
        rep = Repository()
        result = rep.Read(Drink)
        for item in result:
            listitem=[item.NameDrink , item.PriceDrink]
            self.insertServic(self.TblServiceDrink,listitem)
            self.insertServic(self.TblframeDrink, listitem)

    def TakedataMokhalafat(self):
        rep = Repository()
        result = rep.Read(Mokhalafat)
        for item in result:
            listitem=[item.NameMokhalafat , item.PriceMokhalafat]
            self.insertServic(self.TblServiceMokhalafat,listitem)
            self.insertServic(self.TblframeMokhalafat, listitem)






    def CreateWedget (self):
        #maghadir
        self.NameCustomerstr = StringVar()
        self.FamilyCustomerstr = StringVar()
        self.PhoneCustomerstr = StringVar()
        self.NamePersonnelstr = StringVar()
        self.FamilyPersonnelstr = StringVar()
        self.AgePersonnelstr = IntVar()
        self.PhonePersonnelstr = StringVar()
        self.SalaryPersonnelstr = IntVar()
        self.numfood=StringVar()
        self.numdrink=StringVar()
        self.nummok=StringVar()
        self.servicstr= StringVar()
        self.pricestr= StringVar()
        self.finalyprice=0
        #img
        self.bgscreen = PhotoImage(file='img/1.png')
        self.close = PhotoImage(file='img/close.png')
        self.bgservice=PhotoImage(file='img/bgservice.png')

        # background screen

        self.lblbgscreen = Label(self.master , image= self.bgscreen)
        self.lblbgscreen.place(x=0, y=-5)

        # menu

        self.Menubar=Menu(self.master)
        self.MenuCustomer=Menu(self.master , tearoff=0)
        self.Menubar.add_cascade(label=" مشتری " , foreground="yellow", menu=self.MenuCustomer , )
        self.MenuCustomer.add_command(label="خدمات مشتری" , command=self.OneClikShowFrameCustomer )


        self.MenuPersonel = Menu(self.master, tearoff=0)
        self.Menubar.add_cascade(label="پرسنل", foreground="yellow", menu=self.MenuPersonel)
        self.MenuPersonel.add_command(label="خدمات پرسنل" , command=self.OneClikShowPersonelfrm)


        self.MenuFood = Menu(self.master, tearoff=0)
        self.Menubar.add_cascade(label="سرویس ", foreground="yellow", menu=self.MenuFood)
        self.MenuFood.add_command(label="  سرویس ها " , command=self.OneClikShowServicefrm)



        self.master.config(menu=self.Menubar )

        #table
        col=("c1" , "c2" , "c3" , "c4")
        self.TblShowFactor=ttk.Treeview(self.master , columns=col , show="headings" , height=20 ,)
        self.TblShowFactor.place(x=1400 , y=40)

        self.TblShowFactor.column("#4" , width=150 , anchor=S ,)
        self.TblShowFactor.heading("#4"  ,text="محصول" )

        self.TblShowFactor.column("#3", width=60, anchor=S)
        self.TblShowFactor.heading("#3", text="تعداد")

        self.TblShowFactor.column("#2", width=120, anchor=S)
        self.TblShowFactor.heading("#2", text="فی")

        self.TblShowFactor.column("#1", width=150, anchor=S)
        self.TblShowFactor.heading("#1", text="قیمت")

        #btn



        self.btnAcceptFactor = Button(self.master, text="ثبت فاکتور", bg="#0DE842", width=25, height=2  , command=self.OneClikAcceptFactor)
        self.btnAcceptFactor.place(x=1650, y=480)

        self.btnDeleteFactor = Button(self.master, text="حذف سطر فاکتور", bg="#E70A0A", width=25, height=2 , command=self.OneClikDeletFactor)
        self.btnDeleteFactor.place(x=1400, y=480)

        self.btnFoodFactor = Button(self.master, text="نوشیدنی", bg="#7A5EEC", width=25, height=5 , command=self.OneClikShowFrameDrink)
        self.btnFoodFactor.place(x=1402, y=620)

        self.btnDrinkFactor = Button(self.master, text="غذا",command=self.OneClikShowFrameFood, bg="#16E3D4", width=25, height=11 , )
        self.btnDrinkFactor.place(x=1650, y=620)

        self.btnMokhalafatFactor = Button(self.master, text="مخلفات", bg="#EE4141", width=25, height=5 , command=self.OneClikShowFrameMokhalafat)
        self.btnMokhalafatFactor.place(x=1402, y=749)


        #frames
        # framefood

        self.frmFood=Frame(self.master , width=600 , height=750 , bg="#16E3D4")
        self.frmFood.place(x=750 , y=40)
        self.frmFood.place_forget()
        col1 = ("c1", "c2")
        self.TblframeFood = ttk.Treeview(self.frmFood, columns=col1, show="headings", height=20, )
        self.TblframeFood.place(x=76, y=80)

        self.TblframeFood.column("#2", width=230, anchor=S )
        self.TblframeFood.heading("#2", text="غذا")

        self.TblframeFood.column("#1", width=230, anchor=S)
        self.TblframeFood.heading("#1", text="قیمت")

        self.lblNumberFood=Label(self.frmFood , text="تعداد" ,font="baria 30 bold",pady=20 , padx=20 ,bg="#16E3D4").place(x=420 , y=520)
        self.entryNumberFood=Entry(self.frmFood , width=30 , justify="center" , textvariable=self.numfood)
        self.entryNumberFood.place(x=100 , y=550)

        self.btnSendFactorFood=Button(self.frmFood , text="ثبت در فاکتور" , bg="#06DB2C" , height=3 , width=50 , command=self.OneCkikSendFactorFood)
        self.btnSendFactorFood.place(x=80 , y=630)


        self.btnCloseFrame=Button(self.frmFood , text="*" , image=self.close , command=self.OneClikCloseFrameFood)
        self.btnCloseFrame.place(x=555,y=10)


        # frameDrink

        self.frmDrink = Frame(self.master, width=600, height=750, bg="#7A5EEC")
        self.frmDrink.place(x=750, y=40)
        self.frmDrink.place_forget()
        col1 = ("c1", "c2")
        self.TblframeDrink = ttk.Treeview(self.frmDrink, columns=col1, show="headings", height=20, )
        self.TblframeDrink.place(x=76, y=80)

        self.TblframeDrink.column("#2", width=230, anchor=S)
        self.TblframeDrink.heading("#2", text="نوشیدنی")

        self.TblframeDrink.column("#1", width=230, anchor=S)
        self.TblframeDrink.heading("#1", text="قیمت")

        self.lblNumberDrink = Label(self.frmDrink, text="تعداد", font="baria 30 bold", pady=20, padx=20, bg="#7A5EEC" ,).place(x=420, y=520)
        self.entryNumberDrink = Entry(self.frmDrink, width=30 , justify="center" , textvariable=self.numdrink)
        self.entryNumberDrink.place(x=100, y=550)

        self.btnSendFactorDrink = Button(self.frmDrink, text="ثبت در فاکتور", bg="#06DB2C", height=3, width=50 , command=self.OneCkikSendFactorDrink)
        self.btnSendFactorDrink.place(x=80, y=630)

        self.btnCloseFDrink = Button(self.frmDrink, text="*", image=self.close, command=self.OneClikCloseFrameDrink)
        self.btnCloseFDrink.place(x=555, y=10)

        # frameMokhalafat


        self.frmMokhalafat = Frame(self.master, width=600, height=750, bg="#EE4141")
        self.frmMokhalafat.place(x=750, y=40)
        self.frmMokhalafat.place_forget()
        col1 = ("c1", "c2")
        self.TblframeMokhalafat = ttk.Treeview(self.frmMokhalafat, columns=col1, show="headings", height=20, )
        self.TblframeMokhalafat.place(x=76, y=80)

        self.TblframeMokhalafat.column("#2", width=230, anchor=S)
        self.TblframeMokhalafat.heading("#2", text="مخلفات")

        self.TblframeMokhalafat.column("#1", width=230, anchor=S)
        self.TblframeMokhalafat.heading("#1", text="قیمت")

        self.lblNumberMokhalafat = Label(self.frmMokhalafat, text="تعداد", font="baria 30 bold", pady=20, padx=20,bg="#EE4141" , ).place(x=420, y=520)
        self.entryNumberMokhalafat = Entry(self.frmMokhalafat, width=30 , justify="center" , textvariable=self.nummok)
        self.entryNumberMokhalafat.place(x=100, y=550)

        self.btnSendFactorMokhalafat = Button(self.frmMokhalafat, text="ثبت در فاکتور", bg="#06DB2C", height=3, width=50 , command=self.OneCkikSendFactorMokhalafat)
        self.btnSendFactorMokhalafat.place(x=80, y=630)

        self.btnCloseFMokhalafat = Button(self.frmMokhalafat, text="*", image=self.close, command=self.OneClikCloseFrameMokhalafat)
        self.btnCloseFMokhalafat.place(x=555, y=10)

        #framecustomer

        self.frmCustomer=Frame(self.master ,  width=600, height=750 , bg="#81F295")
        self.frmCustomer.place(x=750, y=40)
        self.frmCustomer.place_forget()

        col2=("c1" , "c2" , "c3")
        self.TblCustomer=ttk.Treeview(self.frmCustomer , columns=col2 , show="headings" , height=12 , )
        self.TblCustomer.place(x=45 , y=50)

        self.TblCustomer.column("#3" , width=100 , anchor=S ,)
        self.TblCustomer.heading("#3" , text="نام")

        self.TblCustomer.column("#2", width=200, anchor=S)
        self.TblCustomer.heading("#2", text="نام خانوادگی")

        self.TblCustomer.column("#1", width=200, anchor=S)
        self.TblCustomer.heading("#1", text="شماره تلفن")

        self.TblCustomer.bind("<ButtonRelease-1>", self.getselectionCustomer)

        self.lblCustumerName=Label(self.frmCustomer , text="نام" ,font="baria 22 bold", pady=20, padx=20,bg="#81F295")
        self.lblCustumerName.place(x=440, y=320)

        self.lblCustumerFamily = Label(self.frmCustomer, text="نام خانوادگی", font="baria 22 bold", pady=20, padx=20,bg="#81F295")
        self.lblCustumerFamily.place(x=395, y=390)

        self.lblCustumerPhone = Label(self.frmCustomer, text="تلفن همراه", font="baria 22 bold", pady=20, padx=20 , bg="#81F295")
        self.lblCustumerPhone.place(x=405, y=460)

        self.EntryCustomerName=Entry(self.frmCustomer , width=30 ,justify="center" , textvariable=self.NameCustomerstr)
        self.EntryCustomerName.place(x=100 , y=345)

        self.EntryCustomerFamily = Entry(self.frmCustomer, width=30 , justify="center" , textvariable=self.FamilyCustomerstr)
        self.EntryCustomerFamily.place(x=100, y=415)

        self.EntryCustomerPhone = Entry(self.frmCustomer, width=30 , justify="center" , textvariable=self.PhoneCustomerstr)
        self.EntryCustomerPhone.place(x=100, y=485)




        self.btnCustomerAdd=Button(self.frmCustomer , text="افزودن مشتری" , width=40 , height=2 , bg="#34F409" , command=self.OneClikAddCustomer)
        self.btnCustomerAdd.place(x=120 , y=580)

        self.btnCustomerDelete = Button(self.frmCustomer, text="حذف مشتری", width=19, height=2 , bg="#981C08" , command=self.OneClikDeleteCustomer)
        self.btnCustomerDelete.place(x=120, y=650)

        self.btnCustomerUpdate = Button(self.frmCustomer, text="ویرایش مشتری", width=19, height=2,bg="#E5FC00" , command=self.OneClikUpCustumer )
        self.btnCustomerUpdate.place(x=310, y=650)

        self.btnCloseCustomerfrm = Button(self.frmCustomer, text="*", image=self.close,command=self.OneClikCloseCustomerfrm)
        self.btnCloseCustomerfrm.place(x=555, y=10)

        # framePersonnel

        self.frmPersonel = Frame(self.master, width=600, height=900, bg="#00B3FC")
        self.frmPersonel.place(x=750, y=40)
        self.frmPersonel.place_forget()

        col2 = ("c1", "c2", "c3" , "c4" , "c5")
        self.TblPersonel = ttk.Treeview(self.frmPersonel, columns=col2, show="headings", height=12)
        self.TblPersonel.place(x=15, y=60)

        self.TblPersonel.column("#5", width=100, anchor=S)
        self.TblPersonel.heading("#5", text="نام")

        self.TblPersonel.column("#4", width=170, anchor=S)
        self.TblPersonel.heading("#4", text="نام خانوادگی")

        self.TblPersonel.column("#3", width=50, anchor=S)
        self.TblPersonel.heading("#3", text="سن")

        self.TblPersonel.column("#2", width=130, anchor=S)
        self.TblPersonel.heading("#2", text="شماره تلفن")

        self.TblPersonel.column("#1", width=120, anchor=S)
        self.TblPersonel.heading("#1", text="حقوق ماهیانه")

        self.TblPersonel.bind("<ButtonRelease-1>", self.getselectionPersonnel)

        self.lblPersonelName = Label(self.frmPersonel, text="نام", font="baria 22 bold", pady=20, padx=20, bg="#00B3FC")
        self.lblPersonelName.place(x=440, y=340)

        self.lblPersonelFamily = Label(self.frmPersonel, text="نام خانوادگی", font="baria 22 bold", pady=20, padx=20, bg="#00B3FC")
        self.lblPersonelFamily.place(x=395, y=410)

        self.lblPersonelAge = Label(self.frmPersonel, text=" سن ", font="baria 22 bold", pady=20, padx=20,bg="#00B3FC")
        self.lblPersonelAge.place(x=435, y=480)

        self.lblPersonelPhone = Label(self.frmPersonel, text=" تلفن همراه ", font="baria 22 bold", pady=20, padx=20, bg="#00B3FC")
        self.lblPersonelPhone.place(x=405, y=550)

        self.lblPersonelSalary = Label(self.frmPersonel, text=" حقوق ماهیانه ", font="baria 22 bold", pady=20, padx=20,bg="#00B3FC")
        self.lblPersonelSalary.place(x=385, y=620)


        self.EntryPersonelName = Entry(self.frmPersonel, width=30, justify="center" , textvariable=self.NamePersonnelstr )
        self.EntryPersonelName.place(x=100, y=365)

        self.EntryPersonelFamily = Entry(self.frmPersonel, width=30, justify="center" , textvariable=self.FamilyPersonnelstr)
        self.EntryPersonelFamily.place(x=100, y=435)

        self.EntryPersonelAge = Entry(self.frmPersonel, width=30, justify="center" , textvariable=self.AgePersonnelstr)
        self.EntryPersonelAge.place(x=100, y=505)

        self.EntryPersonelPhone = Entry(self.frmPersonel, width=30, justify="center" , textvariable=self.PhonePersonnelstr)
        self.EntryPersonelPhone.place(x=100, y=575)

        self.EntryPersonelSalary = Entry(self.frmPersonel, width=30, justify="center" , textvariable=self.SalaryPersonnelstr)
        self.EntryPersonelSalary.place(x=100, y=645)

        self.btnPersonelAdd = Button(self.frmPersonel, text="افزودن پرسنل", width=40, height=2, bg="#34F409" , command=self.OneClikAddPersonel)
        self.btnPersonelAdd.place(x=120, y=730)

        self.btnPersonelDelete = Button(self.frmPersonel, text="حذف پرسنل", width=19, height=2, bg="#981C08" , command=self.OneClikDeletePersonnel)
        self.btnPersonelDelete.place(x=120, y=800)

        self.btnPersonelUpdate = Button(self.frmPersonel, text="ویرایش پرسنل", width=19, height=2, bg="#E5FC00" , command=self.OneClikUpPersonnel )
        self.btnPersonelUpdate.place(x=310, y=800)

        self.btnClosePersonelfrm = Button(self.frmPersonel, text="*", image=self.close,command=self.OneClikClosePersonelfrm)
        self.btnClosePersonelfrm.place(x=555, y=10)

        # frameService
        self.service=IntVar()
        self.frmService = Frame(self.master,width=1300, height=750 )
        self.frmService.place(x=50, y=40)
        self.frmService.place_forget()
        self.lblbgservice=Label(self.frmService , image=self.bgservice)
        self.lblbgservice.place(x=0 , y=0)

        self.lblFood=Label(self.frmService , text="غذا" , font="baria 22 bold" , bg="#91E7E1" ,width=8 , height=2 ,padx=20 )
        self.lblFood.place(x=1000, y=15)
        self.radioFood=Radiobutton(self.frmService, text="" , variable=self.service , value=1 , width=5 ,bg="#91E7E1" )
        self.radioFood.place(x=1000 , y=35)

        self.lblDrink = Label(self.frmService, text="نوشیدنی", font="baria 22 bold", bg="#0028C9", width=7, height=2 ,padx=55, fg="white")
        self.lblDrink.place(x=530, y=15)
        self.radioDrink = Radiobutton(self.frmService, text="", variable=self.service, value=2, width=5, bg="#0028C9")
        self.radioDrink.place(x=530, y=35)

        self.lblMokhalafat = Label(self.frmService, text="مخلفات", font="baria 22 bold", bg="#936539", width=7, height=2 ,padx=50,fg="white")
        self.lblMokhalafat.place(x=90, y=15)
        self.radioDrink = Radiobutton(self.frmService, text="", variable=self.service, value=3, width=5, bg="#936539")
        self.radioDrink.place(x=90, y=35)

        col2 = ("c1", "c2",)
        self.TblServiceMokhalafat = ttk.Treeview(self.frmService, columns=col2, show="headings", height=12)
        self.TblServiceMokhalafat.place(x=10, y=100)

        self.TblServiceMokhalafat.column("#2", width=200, anchor=S)
        self.TblServiceMokhalafat.heading("#2", text="نام مخلفات")

        self.TblServiceMokhalafat.column("#1", width=200, anchor=S)
        self.TblServiceMokhalafat.heading("#1", text="قیمت")


        self.TblServiceDrink = ttk.Treeview(self.frmService, columns=col2, show="headings", height=12)
        self.TblServiceDrink.place(x=440, y=100)

        self.TblServiceDrink.column("#2", width=200, anchor=S)
        self.TblServiceDrink.heading("#2", text="نام نوشیدنی")

        self.TblServiceDrink.column("#1", width=200, anchor=S)
        self.TblServiceDrink.heading("#1", text="قیمت")


        self.TblServiceFood = ttk.Treeview(self.frmService, columns=col2, show="headings", height=12)
        self.TblServiceFood.place(x=875, y=100)

        self.TblServiceFood.column("#2", width=200, anchor=S)
        self.TblServiceFood.heading("#2", text="نام غذا")

        self.TblServiceFood.column("#1", width=200, anchor=S)
        self.TblServiceFood.heading("#1", text="قیمت")

        self.TblServiceFood.bind("<ButtonRelease-1>" , self.getselectionFood)
        self.TblServiceDrink.bind("<ButtonRelease-1>" , self.getselectionDrink)
        self.TblServiceMokhalafat.bind("<ButtonRelease-1>" , self.getselectionMokhalafat)


        self.lblCustService = Label(self.frmService, text="نام سرویس", font="baria 22 bold", pady=20, padx=20,bg="#02B7F1" )
        self.lblCustService.place(x=800, y=380)

        self.lblCustumService = Label(self.frmService, text="قیمت", font="baria 22 bold", pady=20, padx=20,bg="#02B7F1" )
        self.lblCustumService.place(x=830, y=470)


        self.EntryServiceName = Entry(self.frmService, width=30, justify="center" , textvariable=self.servicstr)
        self.EntryServiceName.place(x=500, y=415)

        self.EntryServicePrice = Entry(self.frmService, width=30, justify="center",textvariable=self.pricestr)
        self.EntryServicePrice.place(x=500, y=485)





        self.btnServiceAdd = Button(self.frmService, text="افزودن سرویس", width=42, height=4, bg="#34F409" , command=self.OneClikAddservic)
        self.btnServiceAdd.place(x=850, y=580)

        self.btnServiceUpdate = Button(self.frmService, text="حذف سرویس", width=42, height=4, bg="#981C08" , command=self.OneClikDeleteservic)
        self.btnServiceUpdate.place(x=50, y=580)

        self.btnServiceDelete = Button(self.frmService, text="ویرایش سرویس", width=42, height=4, bg="#E5FC00", command=self.OneclikUpservic)
        self.btnServiceDelete.place(x=450, y=580)

        self.btnCloseServicefrm = Button(self.frmService, text="*", image=self.close,command=self.OneClikCloseServicefrm)
        self.btnCloseServicefrm.place(x=1250, y=10)






    #def



    def OneClikShowFrameFood (self):
        self.frmFood.place(x=750, y=40)
        self.frmDrink.place_forget()
        self.frmMokhalafat.place_forget()
        self.frmCustomer.place_forget()
        self.frmPersonel.place_forget()
        self.frmService.place_forget()

    def OneClikCloseFrameFood (self):
        self.frmFood.place_forget()

    def OneClikShowFrameDrink(self):
        self.frmDrink.place(x=750, y=40)
        self.frmMokhalafat.place_forget()
        self.frmFood.place_forget()
        self.frmCustomer.place_forget()
        self.frmPersonel.place_forget()
        self.frmService.place_forget()

    def OneClikCloseFrameDrink (self):
        self.frmDrink.place_forget()


    def OneClikShowFrameMokhalafat(self):
        self.frmMokhalafat.place(x=750, y=40)
        self.frmFood.place_forget()
        self.frmCustomer.place_forget()
        self.frmPersonel.place_forget()
        self.frmService.place_forget()
        self.frmDrink.place_forget()

    def OneClikCloseFrameMokhalafat (self):
        self.frmMokhalafat.place_forget()

    def OneClikShowFrameCustomer(self):
        self.frmCustomer.place(x=750, y=40)
        self.frmFood.place_forget()
        self.frmMokhalafat.place_forget()
        self.frmPersonel.place_forget()
        self.frmService.place_forget()
        self.frmDrink.place_forget()


    def OneClikCloseCustomerfrm (self):
        self.frmCustomer.place_forget()

    def  OneClikShowPersonelfrm(self):
        self.frmPersonel.place(x=750, y=40)
        self.frmFood.place_forget()
        self.frmMokhalafat.place_forget()
        self.frmCustomer.place_forget()
        self.frmService.place_forget()
        self.frmDrink.place_forget()

    def OneClikClosePersonelfrm(self):
        self.frmPersonel.place_forget()

    def OneClikCloseServicefrm(self):
        self.frmService.place_forget()

    def OneClikShowServicefrm(self):
        self.frmService.place(x=50, y=40)
        self.frmFood.place_forget()
        self.frmMokhalafat.place_forget()
        self.frmCustomer.place_forget()
        self.frmPersonel.place_forget()
        self.frmDrink.place_forget()

    def insertCustomer(self,value):
        self.TblCustomer.insert('', "end", text="1", value=[value[2], value[1], value[0]])

    def insertPersonnel(self, value):
        self.TblPersonel.insert('', "end", text="1", value=[value[4], value[3], value[2] , value[1] , value[0]])

    def insertServic(self,tblname, value):
        tblname.insert('', "end", text="1", value=[value[1], value[0]])

    def insertFactor(self , value):
        self.TblShowFactor.insert('', "end", text="1", value=[value[3], value[2], value[1] , value[0]])


 #crudCustomer
    def getselectionCustomer(self,event ):
        select_row = self.TblCustomer.selection()
        if select_row:
            select_item = self.TblCustomer.item(select_row)["values"]
            self.NameCustomerstr.set(select_item[2])
            self.FamilyCustomerstr.set(select_item[1])
            self.PhoneCustomerstr.set(select_item[0])

    def getselectionPersonnel(self, event):
        select_row = self.TblPersonel.selection()
        if select_row:
            select_item = self.TblPersonel.item(select_row)["values"]
            self.NamePersonnelstr.set(select_item[4])
            self.FamilyPersonnelstr.set(select_item[3])
            self.AgePersonnelstr.set(int(select_item[2]))
            self.PhonePersonnelstr.set(select_item[1])
            self.SalaryPersonnelstr.set(int(select_item[0]))

    def getselectionFood(self, event):
        self.entryNumberFood.focus()
        select_row = self.TblServiceFood.selection()

        if select_row != ():
            select_item = self.TblServiceFood.item(select_row)["values"]
            self.servicstr.set(select_item[1])
            self.pricestr.set(select_item[0])

    def getselectionDrink(self, event):
        select_row = self.TblServiceDrink.selection()
        self.entryNumberDrink.focus()
        if select_row:
            select_item = self.TblServiceDrink.item(select_row)["values"]
            self.servicstr.set(select_item[1])
            self.pricestr.set(select_item[0])

    def getselectionMokhalafat(self, event):
        select_row = self.TblServiceMokhalafat.selection()
        if select_row:
            select_item = self.TblServiceMokhalafat.item(select_row)["values"]
            self.servicstr.set(select_item[1])
            self.pricestr.set(select_item[0])

    def cleanCustomer(self):
        self.NameCustomerstr.set("")
        self.FamilyCustomerstr.set("")
        self.PhoneCustomerstr.set("")
        self.EntryCustomerName.focus()

    def cleanPersonnel(self):
        self.NamePersonnelstr.set("")
        self.FamilyPersonnelstr.set("")
        self.AgePersonnelstr.set(0)
        self.PhonePersonnelstr.set("")
        self.SalaryPersonnelstr.set(0)
        self.EntryPersonelName.focus()

    def cleanService(self):
        self.servicstr.set("")
        self.pricestr.set("")
        self.EntryServiceName.focus()

    def OneClikAddCustomer(self):
        if self.EntryCustomerName=="" or self.EntryCustomerFamily=="" or self.EntryCustomerPhone=="" :
            messagebox.showerror("خطا" , " لطفا فیلد ها را به صورت کامل پر کنید")
        else:
            listitem=[self.EntryCustomerName.get() , self.EntryCustomerFamily.get() , self.EntryCustomerPhone.get()]
            Cus=Customer(self.EntryCustomerName.get() , self.EntryCustomerFamily.get() , self.EntryCustomerPhone.get())
            Rej=Repository()
            resalt=Rej.Add(Cus)
            if resalt == True :
                self.insertCustomer(listitem)
                self.cleanCustomer()
                messagebox.showinfo("تایید" ,"مشتری جدید با موفقیت ثبت شد")

            else:
                messagebox.showerror("خطا" ,"ثبت مشتری جدید با خطا روبرو شد !")

    def OneClikDeleteCustomer(self ):
        select_row=self.TblCustomer.selection()
        if select_row!=():
            select_item=self.TblCustomer.item(select_row)["values"]
            rep=Repository()
            red=rep.ReadForCustomer(Customer ,  select_item[2] , select_item[1] , select_item[0])
            result=rep.Delete(red)
            if result == True:
                self.TblCustomer.delete(select_row)
                self.cleanCustomer()
                messagebox.showinfo("تایید", "مشتری با موفقیت حذف شد")
            else:
                messagebox.showerror("خطا", "حذف مشتری با خطا روبرو شد !")

    def OneClikUpCustumer(self):
        select_row = self.TblCustomer.selection()
        tblitem=self.TblCustomer.item(select_row)["values"]
        nameold=tblitem[2]
        familyold=tblitem[1]
        phoneold=tblitem[0]
        name=self.EntryCustomerName.get()
        family=self.EntryCustomerFamily.get()
        phone=self.EntryCustomerPhone.get()
        objn=Customer(name , family , phone)
        rep=Repository()
        result=rep.UpdateCustomer(Customer, objn, nameold , familyold , phoneold )


        if result==True:
            self.cleanCustomer()
            self.TblCustomer.item(select_row , values=[phone , family , name])
            messagebox.showinfo("تایید " , "ویرایش  با موفقیت انجام شد")
        else:
            messagebox.showerror("خطا " ,"ویرایش انجام نشد")

    def OneClikAddPersonel(self):
        if self.EntryPersonelName == "" or self.EntryPersonelFamily == "" or self.EntryPersonelAge == "" or self.EntryPersonelPhone == "" or self.EntryPersonelSalary == "":
            messagebox.showerror("خطا", " لطفا فیلد ها را به صورت کامل پر کنید")
        else:
            name = self.EntryPersonelName.get()
            family = self.EntryPersonelFamily.get()
            age = self.EntryPersonelAge.get()
            phone=self.EntryPersonelPhone.get()
            salary = self.EntryPersonelSalary.get()
            listitem = [name, family, age , phone , salary]
            Per=Personnel(name , family ,age , phone , salary)
            Rej=Repository()
            resualt=Rej.Add(Per)
            if resualt == True:
                self.insertPersonnel(listitem)
                self.cleanPersonnel()
                messagebox.showinfo("تایید", "پرسنل جدید با موفقیت ثبت شد")
            else:
                messagebox.showerror("خطا", "ثبت پرسنل جدید با خطا روبرو شد !")

    def OneClikDeletePersonnel(self):
        select_row = self.TblPersonel.selection()
        if select_row != ():
            select_item = self.TblPersonel.item(select_row)["values"]
            rep = Repository()
            red = rep.ReadForPersonnel(Personnel, select_item[4], select_item[3], select_item[2] , select_item[1] ,select_item[0])
            result = rep.Delete(red)
            if result == True:
                self.cleanPersonnel()
                self.TblPersonel.delete(select_row)
                messagebox.showinfo("تایید", "پرسنل با موفقیت حذف شد")
            else:
                messagebox.showerror("خطا", "حذف پرسنل با خطا روبرو شد !")

    def OneClikUpPersonnel(self):
        select_row = self.TblPersonel.selection()
        tblitem = self.TblPersonel.item(select_row)["values"]
        nameold = tblitem[4]
        familyold = tblitem[3]
        ageold = tblitem[2]
        phoneold= tblitem[1]
        salaryold = tblitem[0]


        name = self.EntryPersonelName.get()
        family = self.EntryPersonelFamily.get()
        phone = self.EntryPersonelPhone.get()
        age = self.EntryPersonelAge.get()
        salary = self.EntryPersonelSalary.get()
        objnew = Personnel(name, family, age , phone , salary)

        rep = Repository()
        result = rep.UpdatePersonnel(Personnel, objnew, nameold, familyold ,ageold , phoneold , salaryold)

        if result == True:
            self.cleanPersonnel()
            self.TblPersonel.item(select_row, values=[salary ,phone , age, family, name])
            messagebox.showinfo("تایید", "ویرایش  با موفقیت انجام شد")
        else:
            messagebox.showerror("خطا", " ویرایش انجام نشد")

    def OneClikAddservic(self):

        numberservic=self.service.get()

        name = self.EntryServiceName.get()
        price = self.EntryServicePrice.get()
        rep=Repository()
        listitem = [name, price]
        if self.EntryServiceName == "" or self.EntryServicePrice == "" :
            messagebox.showerror("خطا", " لطفا فیلد ها را به صورت کامل پر کنید")
        elif numberservic == 0 :
            messagebox.showerror("خطا", " لطفا نوع سرویس را مشخص کنید")
        else:
            if numberservic == 1:
                Fud = Food(name , price)
                resulat=rep.Add(Fud)
                if resulat == True:
                    self.service.set(0)
                    self.insertServic(self.TblframeFood, listitem)
                    self.insertServic(self.TblServiceFood,listitem)
                    self.cleanService()
                    messagebox.showinfo("تایید", "سرویس غذا جدید با موفقیت ثبت شد")
                else:
                    messagebox.showerror("خطا", "ثبت سرویس غذا جدید با خطا روبرو شد !")
            elif numberservic == 2 :
                dri = Drink(name, price)
                resulat = rep.Add(dri)
                if resulat == True:
                    self.service.set(0)
                    self.insertServic(self.TblServiceDrink, listitem)
                    self.insertServic(self.TblframeDrink, listitem)
                    self.cleanService()
                    messagebox.showinfo("تایید", "سرویس نوشیدنی جدید با موفقیت ثبت شد")
                else:
                    messagebox.showerror("خطا", "ثبت سرویس نوشیدنی جدید با خطا روبرو شد !")
            elif numberservic== 3:
                mok = Mokhalafat(name, price)
                resulat = rep.Add(mok)
                if resulat == True:
                    self.service.set(0)
                    self.insertServic(self.TblServiceMokhalafat, listitem)
                    self.insertServic(self.TblframeMokhalafat, listitem)
                    self.cleanService()
                    messagebox.showinfo("تایید", "سرویس مخلفات جدید با موفقیت ثبت شد")
                else:
                    messagebox.showerror("خطا", "ثبت سرویس مخلفات جدید با خطا روبرو شد !")

    def OneClikDeleteservic(self):
        numberservic = self.service.get()
        if numberservic == 0 :
            messagebox.showerror("خطا", " لطفا نوع سرویس را مشخص کنید")
        else:
            if numberservic == 1:
                select_row = self.TblServiceFood.selection()
                if select_row != ():
                    select_item = self.TblServiceFood.item(select_row)["values"]
                    rep = Repository()
                    red = rep.ReadForFood(Food, select_item[1], select_item[0])
                    result = rep.Delete(red)
                    if result == True:
                        self.service.set(0)
                        self.TblServiceFood.delete(select_row)
                        self.TblframeFood.delete(select_row)
                        self.cleanService()
                        messagebox.showinfo("تایید", "سرویس غذا با موفقیت حذف شد")

                    else:
                        messagebox.showerror("خطا", "حذف سرویس غذا با خطا روبرو شد !")
            elif numberservic == 2:
                select_row = self.TblServiceDrink.selection()
                if select_row != ():
                    select_item = self.TblServiceDrink.item(select_row)["values"]
                    rep = Repository()
                    red = rep.ReadForDrink(Drink, select_item[1], select_item[0])
                    result = rep.Delete(red)
                    if result == True:
                        self.service.set(0)
                        self.TblServiceDrink.delete(select_row)
                        self.TblframeDrink.delete(select_row)
                        self.cleanService()
                        messagebox.showinfo("تایید", "سرویس نوشیدنی با موفقیت حذف شد")
                    else:
                        messagebox.showerror("خطا", "حذف سرویس نوشیدنی با خطا روبرو شد !")
            elif numberservic == 3:

                select_row = self.TblServiceMokhalafat.selection()
                if select_row != ():
                    select_item = self.TblServiceMokhalafat.item(select_row)["values"]
                    rep = Repository()
                    red = rep.ReadForMokhalafat(Mokhalafat, select_item[1], select_item[0])
                    result = rep.Delete(red)
                    if result == True:
                        self.service.set(0)
                        self.TblServiceMokhalafat.delete(select_row)
                        self.TblframeMokhalafat.delete(select_row)
                        self.cleanService()
                        messagebox.showinfo("تایید", "سرویس مخلفات با موفقیت حذف شد")
                    else:
                        messagebox.showerror("خطا", "حذف سرویس مخلفات با خطا روبرو شد !")

    def OneclikUpservic(self):
        self.numberservic = self.service.get()
        if self.numberservic == 0:
            messagebox.showerror("خطا", " لطفا نوع سرویس را مشخص کنید")
        else:
            if self.numberservic == 1:
                select_row = self.TblServiceFood.selection()
                tblitem = self.TblServiceFood.item(select_row)["values"]
                nameold = tblitem[1]
                priceyold = tblitem[0]
                name=self.EntryServiceName.get()
                price=self.EntryServicePrice.get()
                objnew=Food(name , price)
                rep = Repository()
                result = rep.UpdateFood(Food, objnew, nameold, priceyold )
                if result == True:
                    self.service.set(0)
                    self.TblServiceFood.item(select_row, values=[price , name])
                    self.TblframeFood.item(select_row, values=[price , name])
                    self.cleanService()
                    messagebox.showinfo("تایید ", "ویرایش  با موفقیت انجام شد")
                else:
                    messagebox.showerror("خطا", " ویرایش انجام نشد")
            elif self.numberservic == 2:
                select_row = self.TblServiceDrink.selection()
                tblitem = self.TblServiceDrink.item(select_row)["values"]
                nameold = tblitem[1]
                priceyold = tblitem[0]
                name = self.EntryServiceName.get()
                price = self.EntryServicePrice.get()
                objnew = Drink(name, price)
                rep = Repository()
                result = rep.UpdateDrink(Drink, objnew, nameold, priceyold)
                if result == True:
                    self.service.set(0)
                    self.TblServiceDrink.item(select_row, values=[price, name])
                    self.TblframeDrink.item(select_row, values=[price, name])
                    self.cleanService()
                    messagebox.showinfo("تایید", "ویرایش  با موفقیت انجام شد")
                else:
                    messagebox.showerror("خطا", " ویرایش انجام نشد")

            elif self.numberservic == 3:
                select_row = self.TblServiceMokhalafat.selection()
                tblitem = self.TblServiceMokhalafat.item(select_row)["values"]
                nameold = tblitem[1]
                priceyold = tblitem[0]
                name = self.EntryServiceName.get()
                price = self.EntryServicePrice.get()
                objnew = Mokhalafat(name, price)
                rep = Repository()
                result = rep.UpdateMokhalafat(Mokhalafat, objnew, nameold, priceyold)
                if result == True:
                    self.service.set(0)
                    self.TblServiceMokhalafat.item(select_row, values=[price, name])
                    self.TblframeMokhalafat.item(select_row, values=[price, name])
                    self.cleanService()
                    messagebox.showinfo("تایید", "ویرایش  با موفقیت انجام شد")
                else:
                    messagebox.showerror("خطا", "ویرایش انجام نشد")

    def OneCkikSendFactorFood(self):
        select_row = self.TblframeFood.selection()
        self.entryNumberFood.focus()
        if select_row:
            select_item = self.TblframeFood.item(select_row)["values"]
            name=select_item[1]
            price=select_item[0]
            number=self.entryNumberFood.get()
            finalynumber=price*int(number)
            obj=[name , number , price , finalynumber]
            self.insertFactor(obj)
            self.finalyprice += obj[3]
            self.numfood.set("")

    def OneCkikSendFactorDrink(self):
        select_row = self.TblframeDrink.selection()
        self.entryNumberDrink.focus()
        if select_row:
            select_item = self.TblframeDrink.item(select_row)["values"]
            name=select_item[1]
            price=select_item[0]
            number=self.entryNumberDrink.get()
            finalynumber=price*int(number)
            obj=[name , number , price , finalynumber]
            self.insertFactor(obj)
            self.finalyprice += obj[3]
            self.numdrink.set("")
    def OneCkikSendFactorMokhalafat(self):
        select_row = self.TblframeMokhalafat.selection()
        self.entryNumberMokhalafat.focus()

        if select_row:
            select_item = self.TblframeMokhalafat.item(select_row)["values"]
            name=select_item[1]
            price=select_item[0]
            number=self.entryNumberMokhalafat.get()
            finalynumber=price*int(number)
            obj=[name , number , price , finalynumber]
            self.insertFactor(obj)
            self.finalyprice += obj[3]
            self.nummok.set("")
    def OneClikAcceptFactor(self):
        self.frmFood.place_forget()
        self.frmMokhalafat.place_forget()
        self.frmDrink.place_forget()
        messagebox.showinfo("تایید","' فاکتور شما به مبلغ "+str(self.finalyprice) +" صادر شد '")

        self.finalyprice=0
        for item in self.TblShowFactor.get_children():
            self.TblShowFactor.delete((item))

    def OneClikDeletFactor(self):
        select_row = self.TblShowFactor.selection()
        if select_row != ():

            select_item = self.TblShowFactor.item(select_row)["values"]
            pricedelete = select_item[0]
            self.finalyprice -= pricedelete
            self.TblShowFactor.delete(select_row)