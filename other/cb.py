import os
from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox as ms
import sqlite3
from PIL import Image,ImageTk
import tempfile

Item4 = 0

with sqlite3.connect('Users.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEXT NOT NULL)')
c.execute('CREATE TABLE IF NOT EXISTS details (Receipt_Ref TEXT NOT NULL, DateofOrder TEXT NOT NULL,Taxi_No TEXT NOT NULL,Customer_Name TEXT NOT NULL,Address TEXT NOT NULL,Phone_Number TEXT NOT NULL,Pick_Up TEXT NOT NULL,Drop_Location TEXT NOT NULL,Pooling TEXT NOT NULL,Total TEXT NOT NULL)')
db.commit()
db.close()

# main Class
class user:
    def __init__(self, master):
        # Window 
        self.master = master
        # Some Usefull variables 
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        # Create Widgets
        self.widgets()

    # Login Function
    def login(self):
        # Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        # Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = "Welcome, " + self.username.get()
            self.head.configure(fg="white",bg="black")
            self.head.pack(fill=X)
            application = travel(root)

        else:
            ms.showerror('Oops!', '\nUsername Not Found.')

    def new_user(self):
        # Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        # Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user, [(self.username.get())])
        if c.fetchall():
            ms.showerror('Error!', '\nUsername Already Taken!')
        else:
            ms.showinfo('Success!', 'Account Created!')
            self.log()
        # Create New Account
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()

        # Frame Packing Methords

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    # Draw Widgets
    def widgets(self):
        self.head = Label(self.master, text='LOGIN', font=('', 35), pady=10)
        self.head.pack()

        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Login ', bd=3, font=('', 15), padx=5, pady=5, command=self.login).grid()
        Button(self.logf, text=' Create Account ', bd=3, font=('', 15), padx=5, pady=5, command=self.cr).grid(row=2,
                                                                                                              column=1)
        self.logf.pack()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.crf, text='Create Account', bd=3, font=('', 15), padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text=' Login', bd=3, font=('', 15), padx=5, pady=5, command=self.log).grid(row=2, column=1)


class travel:

    def __init__(self, root):
        self.root = root
        self.root.title("🚗BOOK CAB4me🚗")
        self.root.geometry(geometry)
        self.root.configure(background='black')

        ip=StringVar()
        DateofOrder = StringVar()
        DateofOrder.set(time.strftime(" %d / %m / %Y "))
        Receipt_Ref = StringVar()
        PaidTax = StringVar()
        SubTotal = StringVar()
        TotalCost = StringVar()

        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        journeyType = IntVar()
        carType = IntVar()

        varl1 = StringVar()
        varl2 = StringVar()
        varl3 = StringVar()
        reset_counter = 0

        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        Postcode = StringVar()
        Mobile = StringVar()
        Telephone = StringVar()
        Email = StringVar()

        TaxiTax = StringVar()
        Km = StringVar()
        Travel_Ins = StringVar()
        Luggage = StringVar()
        Receipt = StringVar()

        Standard = StringVar()
        PrimeSedan = StringVar()
        PremiumSedan = StringVar()

        TaxiTax.set("0")
        Km.set("0")
        Travel_Ins.set("0")
        Luggage.set("0")

        Standard.set("0")
        PrimeSedan.set("0")
        PremiumSedan.set("0")

        # ==========================================Define Functiom==================================================

        def iExit():
            iExit = ms.askyesno("Prompt!", "Do you want to Logout?")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            TaxiTax.set("0")
            Km.set("0")
            Travel_Ins.set("0")
            Luggage.set("0")

            Standard.set("0")
            PrimeSedan.set("0")
            PremiumSedan.set("0")

            Firstname.set("")
            Surname.set("")
            Address.set("")
            Postcode.set("")
            Mobile.set("")
            Telephone.set("")
            Email.set("")

            PaidTax.set("")
            SubTotal.set("")
            TotalCost.set("")
            self.txtReceipt1.delete("1.0", END)
            self.txtReceipt2.delete("1.0", END)

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            journeyType.set(0)
            carType.set(0)
            varl1.set("0")
            varl2.set("0")
            varl3.set("0")

            self.cboPickup.current(0)
            self.cboDrop.current(0)
            self.cboPooling.current(0)

            self.txtTaxiTax.configure(state=DISABLED)
            self.txtKm.configure(state=DISABLED)
            self.txtTravel_Ins.configure(state=DISABLED)
            self.txtLuggage.configure(state=DISABLED)

            self.txtStandard.configure(state=DISABLED)
            self.txtPrimeSedan.configure(state=DISABLED)
            self.txtPremiumSedan.configure(state=DISABLED)
            self.reset_counter = 1

        def Receiptt():
            if reset_counter is 0 and Firstname.get() != "" and Surname.get() != "" and Address.get() != "" and Postcode.get() != "" and Mobile.get() != "" and Telephone.get() != "" and Email.get() != "":
                if ((var1.get() == 1 and var2.get() == 1 and var3.get() == 1 or var4.get() == 1) and carType.get() != 0 and journeyType.get() != 0 and (varl1.get() != "" and varl2.get() != "")):
                    self.txtReceipt1.delete("1.0", END)
                    self.txtReceipt2.delete("1.0", END)
                    x = random.randint(10853, 500831)
                    randomRef = str(x)
                    Receipt_Ref.set(randomRef)

                    self.txtReceipt1.insert(END, "Receipt Ref:\n")
                    self.txtReceipt2.insert(END, Receipt_Ref.get() + "\n")
                    self.txtReceipt1.insert(END, 'Date:\n')
                    self.txtReceipt2.insert(END, DateofOrder.get() + "\n")
                    self.txtReceipt1.insert(END, 'Taxi No:\n')
                    self.txtReceipt2.insert(END, 'TR ' + Receipt_Ref.get() + " BW\n")
                    self.txtReceipt1.insert(END, 'Firstname:\n')
                    self.txtReceipt2.insert(END, Firstname.get() + "\n")
                    self.txtReceipt1.insert(END, 'Surname:\n')
                    self.txtReceipt2.insert(END, Surname.get() + "\n")
                    self.txtReceipt1.insert(END, 'Address:\n')
                    self.txtReceipt2.insert(END, Address.get() + "\n")
                    self.txtReceipt1.insert(END, 'Postal Code:\n')
                    self.txtReceipt2.insert(END, Postcode.get() + "\n")
                    self.txtReceipt1.insert(END, 'Telephone:\n')
                    self.txtReceipt2.insert(END, Telephone.get() + "\n")
                    self.txtReceipt1.insert(END, 'Mobile:\n')
                    self.txtReceipt2.insert(END, Mobile.get() + "\n")
                    self.txtReceipt1.insert(END, 'Email:\n')
                    self.txtReceipt2.insert(END, Email.get() + "\n")
                    self.txtReceipt1.insert(END, 'From:\n')
                    self.txtReceipt2.insert(END, varl1.get() + "\n")
                    self.txtReceipt1.insert(END, 'To:\n')
                    self.txtReceipt2.insert(END, varl2.get() + "\n")
                    self.txtReceipt1.insert(END, 'Pooling:\n')
                    self.txtReceipt2.insert(END, varl3.get() + "\n")
                    self.txtReceipt1.insert(END, 'Bike:\n')
                    self.txtReceipt2.insert(END, Standard.get() + "\n")
                    self.txtReceipt1.insert(END, 'Auto:\n')
                    self.txtReceipt2.insert(END, PrimeSedan.get() + "\n")
                    self.txtReceipt1.insert(END, 'Car:\n')
                    self.txtReceipt2.insert(END, PremiumSedan.get() + "\n")
                    self.txtReceipt1.insert(END, 'Paid:\n')
                    self.txtReceipt2.insert(END, PaidTax.get() + "\n")
                    self.txtReceipt1.insert(END, 'SubTotal:\n')
                    self.txtReceipt2.insert(END, str(SubTotal.get()) + "\n")
                    self.txtReceipt1.insert(END, 'Total Cost:\n')
                    self.txtReceipt2.insert(END, str(TotalCost.get()))

                else:
                    self.txtReceipt1.delete("1.0", END)
                    self.txtReceipt2.delete("1.0", END)
                    self.txtReceipt1.insert(END, "\nNo Input")

        def Taxi_Tax():
            global Item1
            if var1.get() == 1:
                self.txtTaxiTax.configure(state=NORMAL)
                Item1 = float(50)
                TaxiTax.set("Rs " + str(Item1))
            elif var1.get() == 0:
                self.txtTaxiTax.configure(state=DISABLED)
                TaxiTax.set("0")
                Item1 = 0

        def Kilo():
            if var2.get() == 0:
                self.txtKm.configure(state=DISABLED)
                Km.set("0")
            elif var2.get() == 1 and varl1.get() != "" and varl2.get() != "":
                self.txtKm.configure(state=NORMAL)
                if varl1.get() == "Swargate":
                    switch = {"ShaniwarWada": 10, "VIIT": 8, "Katraj": 6, "Swargate": 0}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "ShaniwarWada":
                    switch = {"ShaniwarWada": 0, "VIIT": 2, "Katraj": 5, "Swargate": 10}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "VIIT":
                    switch = {"ShaniwarWada": 2, "VIIT": 0, "Katraj": 3, "Swargate": 8}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Katraj":
                    switch = {"ShaniwarWada": 5, "VIIT": 3, "Katraj": 0, "Swargate": 6}
                    Km.set(switch[varl2.get()])

        def Travelling():
            global Item3
            if var3.get() == 1:
                self.txtTravel_Ins.configure(state=NORMAL)
                Item3 = float(10)
                Travel_Ins.set("Rs " + str(Item3))
            elif var3.get() == 0:
                self.txtTravel_Ins.configure(state=DISABLED)
                Travel_Ins.set("0")
                Item3 = 0

        def Lug():
            global Item4
            if (var4.get() == 1):
                self.txtLuggage.configure(state=NORMAL)
                Item4 = float(30)
                Luggage.set("Rs " + str(Item4))
            elif var4.get() == 0:
                self.txtLuggage.configure(state=DISABLED)
                Luggage.set("0")
                Item4 = 0

        def selectCar():
            global Item5
            if carType.get() == 1:
                self.txtPrimeSedan.configure(state=DISABLED)
                PrimeSedan.set("0")
                self.txtPremiumSedan.configure(state=DISABLED)
                PremiumSedan.set("0")
                self.txtStandard.configure(state=NORMAL)
                Item5 = float(8)
                Standard.set("Rs " + str(Item5))

            elif carType.get() == 2:
                self.txtStandard.configure(state=DISABLED)
                Standard.set("0")
                self.txtPremiumSedan.configure(state=DISABLED)
                PremiumSedan.set("0")
                self.txtPrimeSedan.configure(state=NORMAL)
                Item5 = float(10)
                PrimeSedan.set("Rs " + str(Item5))
            else:
                self.txtStandard.configure(state=DISABLED)
                Standard.set("0")
                self.txtPrimeSedan.configure(state=DISABLED)
                PrimeSedan.set("0")
                self.txtPremiumSedan.configure(state=NORMAL)
                Item5 = float(15)
                PremiumSedan.set("Rs " + str(Item5))

        def Total_Paid():
            if ((
                    var1.get() == 1 and var2.get() == 1 and var3.get() == 1 or var4.get() == 1) and carType.get() != 0 and journeyType.get() != 0 and (
                    varl1.get() != "" and varl2.get() != "")):
                if journeyType.get() == 1:
                    Item2 = Km.get()
                    Cost_of_fare = (Item1 + (float(Item2) * Item5) + Item3 + Item4)

                    Tax = "Rs " + str('%.2f' % ((Cost_of_fare) * 0.09))
                    ST = "Rs " + str('%.2f' % ((Cost_of_fare)))
                    TT = "Rs " + str('%.2f' % (Cost_of_fare + ((Cost_of_fare) * 0.9)))
                elif journeyType.get() == 2:
                    Item2 = Km.get()
                    Cost_of_fare = (Item1 + (float(Item2) * Item5) * 1.5 + Item3 + Item4)

                    Tax = "Rs " + str('%.2f' % ((Cost_of_fare) * 0.09))
                    ST = "Rs " + str('%.2f' % ((Cost_of_fare)))
                    TT = "Rs " + str('%.2f' % (Cost_of_fare + ((Cost_of_fare) * 0.9)))
                else:
                    Item2 = Km.get()
                    Cost_of_fare = (Item1 + (float(Item2) * Item5) * 2 + Item3 + Item4)

                    Tax = "Rs " + str('%.2f' % ((Cost_of_fare) * 0.09))
                    ST = "Rs " + str('%.2f' % ((Cost_of_fare)))
                    TT = "Rs " + str('%.2f' % (Cost_of_fare + ((Cost_of_fare) * 0.9)))

                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
            else:
                w = ms.showwarning("Error !", "Invalid Input\nPlease try again !!!")

        def nextpage():
            if(Firstname.get() == "" or Surname.get() == "" or Address.get() == "" or Postcode.get() == "" or Mobile.get() == "" or Email.get() == "" or var1.get() == 0 or var2.get() == 0 or var3.get() == 0 or self.cboPickup.current() == 0 or self.cboDrop.current() == 0 or self.cboPooling.current() == 0):
                ms.showerror("Error","Fields cannot be empty!Exception(Extra Luggage")
            else:
                if(Firstname.get().isdigit() == True or Surname.get().isdigit() == True or Postcode.get().isdigit() == False or Telephone.get().isdigit() == False or Mobile.get().isdigit() == False):
                    ms.showerror("Error", "Enter Valid Inputs!")
                else:
                    if(len(Mobile.get())!=10):
                        ms.showerror("Error", "Enter valid Mobile Number!")
                    else:
                        self.FrameDetails.pack_forget()
                        self.secondpage.pack(side=LEFT, fill=BOTH, expand=True)

        def back():
            self.secondpage.pack_forget()
            self.FrameDetails.pack(fill=BOTH, expand=True)

        def back2():
            self.thridpage.pack_forget()
            self.FrameDetails.pack(fill=BOTH, expand=True)

        def infopage():
            style=ttk.Style()
            style.configure("Treeview",
                            background="#00B5E2",
                            foreground="white",
                            rowheight=25,
                            fieldbackground="blue",
                            font=('arial', 10, 'bold')
                            )
            style.map("Treeview",
                      background=[('selected','black')]
                      )
            self.bgframe = LabelFrame(self.thridpage, width=1000, height=500, font=('arial', 30, 'bold'),
                                relief=RIDGE, padx=20, pady=10,bd=10)
            self.bgframe.place(x=10, y=100)
            with sqlite3.connect('Users.db') as db:
                c2 = db.cursor()

            data = ('SELECT * FROM details')
            c2.execute(data)
            rows=c2.fetchall()
            tree = ttk.Treeview(self.bgframe,columns=(1,2,3,4,5,6,7,8,9,10), show="headings", height=15)

            tree.column(1, width=100, anchor="c")
            tree.column(2, width=100, anchor="c")
            tree.column(3, width=100, anchor="c")
            tree.column(4, width=100, anchor="c")
            tree.column(5, width=100, anchor="c")
            tree.column(6, width=100, anchor="c")
            tree.column(7, width=100, anchor="c")
            tree.column(8, width=100, anchor="c")
            tree.column(9, width=100, anchor="c")
            tree.column(10, width=100, anchor="c")

            tree.heading(1, text="Receipt_Ref")
            tree.heading(2, text="DateofOrder")
            tree.heading(3, text="Taxi_No")
            tree.heading(4, text="Customer_Name")
            tree.heading(5, text="Address")
            tree.heading(6, text="Phone_Number")
            tree.heading(7, text="Pick_Up")
            tree.heading(8, text="Drop_Location")
            tree.heading(9, text="Pooling")
            tree.heading(10, text="Total")

            for i in rows:
                tree.insert("", 'end', values=i)
            tree.pack()

            self.FrameDetails.pack_forget()
            self.thridpage.pack(side=LEFT, fill=BOTH, expand=True)

        def details():
            with sqlite3.connect('Users.db') as db:
                c = db.cursor()

            inserting = 'INSERT INTO details(Receipt_Ref,DateofOrder,Taxi_No,Customer_Name,Address,Phone_Number,Pick_Up,Drop_Location,Pooling,Total) VALUES(?,?,?,?,?,?,?,?,?,?)'
            c.execute(inserting, [(Receipt_Ref.get()), (DateofOrder.get()), ('TR ' + Receipt_Ref.get() + " BW"), (Firstname.get()+Surname.get()), (Address.get()+Postcode.get()), (Mobile.get()), (varl1.get()), (varl2.get()), (varl3.get()), (TotalCost.get())])
            db.commit()
            Reset()

        def print_command(ip):
            li=["Receipt Ref:","Date:","Taxi No:","Firstname:","Surname:","Address:","Postal Code:","Telephone:","Mobile:","Email:","From:","To:","Pooling:","Bike:","Auto:","Car:","Paid:","SubTotal:","Total Cost:"]
            print_item=tempfile.mktemp('.txt')
            txt=''
            for i in range(len(li)):
                txt=txt+(li[i]+ip.get((str(i+1)+'.0'),(str(i+1+1)+'.0')))#((txt1.get(i,i+1))+(txt1.get(i,i+1)))
            open(print_item, 'w').write(txt)
            os.startfile(print_item,'print')
        # ========================================================================================================================

        MainFrame = Frame(self.root, bg="black")
        MainFrame.pack(fill=BOTH, expand=True)

        Tops = Frame(MainFrame, bg="yellow")  # width=1350,
        Tops.pack(fill=X)

        self.lblTitle = Label(Tops, font=('arial', 50, 'bold'), text="Cab Booking System", foreground="black",
                              bg="yellow",padx=250)
        self.lbldate = Label(Tops, font=('arial', 20, 'bold'), text=DateofOrder.get(), foreground="black", bg="yellow")
        self.btnExit = Button(Tops, padx=18, bd=7, font=('arial', 11, 'bold'), text='Logout',
                              command=iExit,bg="white")

        self.btnExit.grid(row=0, column=2,columnspan=1,sticky=E)
        self.lblTitle.grid(row=0, column=1)
        self.lbldate.grid(row=0, column=0)

        # ============================================================================================================

        self.FrameDetails = Frame(MainFrame,bg="white")
        self.FrameDetails.pack(side=LEFT,fill=BOTH,expand=True)

        img2 = Image.open("img_1.png")
        photo2 = ImageTk.PhotoImage(img2)
        imgbg = Label(self.FrameDetails, image=photo2)
        imgbg.grid(row=0, column=0)

        self.info = Button(self.FrameDetails, padx=18, bd=7, font=('arial', 15, 'bold'), text='Bookings',command=infopage).place(x=10,y=10)#grid(row=0, column=0,padx=10)

        Details = Frame(self.FrameDetails, bg="white",padx=30)
        Details.grid(row=0,column=1)

        CustomerName = LabelFrame(Details, width=150, height=250, font=('arial', 12, 'bold'),
                                  text="Customer Name")
        CustomerName.grid(row=0, column=0)

        TravelFrame = LabelFrame(Details, width=300, height=250, font=('arial', 12, 'bold'),
                                 text="Booking Detail")
        TravelFrame.grid(row=1, column=0)

        buttons = Frame(Details, bg="white")  # , width=880, height=400)
        buttons.grid(row=2, column=0)

        self.btnreset1 = Button(buttons, padx=18, bd=7, font=('arial', 15, 'bold'), width=2, text='Reset',command=Reset).grid(row=0, column=0,padx=10)
        self.btnnext = Button(buttons, padx=18, bd=7, font=('arial', 15, 'bold'), width=2, text='NEXT',command=nextpage).grid(row=0, column=1,padx=10)

        self.secondpage=Frame(MainFrame,bg="white")

        self.Receipt_BottonFrame = LabelFrame(self.secondpage, bd=10, width=600, height=1000, relief=RIDGE, padx=20, pady=20)
        self.Receipt_BottonFrame.place(x=950, y=60)

        ReceiptFrame = LabelFrame(self.Receipt_BottonFrame, width=600, height=1000, font=('arial', 20, 'bold'),
                                  text="Receipt", relief=RIDGE)
        ReceiptFrame.grid(row=0, column=0)

        ButtonFrame = LabelFrame(self.Receipt_BottonFrame, width=600, height=1000, relief=RIDGE)
        ButtonFrame.grid(row=1, column=0)

        self.txtReceipt1 = Text(ReceiptFrame, width=22, height=21, font=('arial', 10, 'bold'), borderwidth=0)
        self.txtReceipt1.grid(row=0, column=0, columnspan=2)
        self.txtReceipt2 = Text(ReceiptFrame, width=22, height=21, font=('arial', 10, 'bold'), borderwidth=0)
        self.txtReceipt2.grid(row=0, column=2, columnspan=2)

        self.btnnext2 = Button(ButtonFrame, padx=18, bd=7, font=('arial', 15, 'bold'), width=3, text='Save',
                               command=details).grid(row=0, column=2)#, padx=10, pady=10)
        self.btnReceipt = Button(ButtonFrame, padx=18, bd=7, font=('arial', 15, 'bold'), width=3, text='Receipt',
                                 command=Receiptt).grid(row=0, column=0)#, padx=10, pady=10)
        self.btnPrint = Button(ButtonFrame, padx=18, bd=7, font=('arial', 15, 'bold'), width=3, text='Print',
                                 command=lambda: print_command(self.txtReceipt2)).grid(row=0, column=1)#, padx=10, pady=10)

        self.btnnext = Button(self.secondpage, padx=18, bd=7, font=('arial', 15, 'bold'), width=2, text='Back',command=back).place(x=10,y=10)

        #temp=Frame(self.secondpage,width=1240,height=600,relief=RIDGE,bd=10).place(x=150,y=30)
        label =LabelFrame(self.secondpage, width=700,height=700, font=('arial',30,'bold'),text="Choose Vehicle", relief=RIDGE,padx=60,pady=20,bd=10) #Label(self.secondpage,text='Choose vehicle', font=('arial', 44, 'bold'), bg='yellow')
        label.place(x=200,y=50)
        photo = PhotoImage(file=r'rikshaw.png')
        pimg = photo.subsample(2, 2)
        p1hoto = PhotoImage(file=r'taxi-app-png.png')
        p1img = p1hoto.subsample(4, 4)
        photo1 = PhotoImage(file=r'taxicar.png')
        pimg1 = photo1.subsample(7, 7)
        b1 = Button(label, image=pimg, compound=LEFT, activebackground='black', height=102, width=150).grid(row=0,column=0,padx=10)
        b2 = Button(label, image=p1img, compound=LEFT, activebackground='black', height=102, width=150).grid(row=0,column=1,padx=10)
        b3 = Button(label, image=pimg1, compound=LEFT, activebackground='black', height=102, width=150).grid(row=0,column=2,padx=10)

        self.chkStandard = Radiobutton(label, text="Bike", value=1, variable=carType, font=('arial', 14, 'bold'),
                                       command=selectCar).grid(row=1, column=1, sticky=W)
        self.txtStandard = Label(label, font=('arial', 14, 'bold'), width=7, textvariable=Standard, bd=5,
                                 state=DISABLED, justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtStandard.grid(row=2, column=1)

        self.chkPrimeSedand = Radiobutton(label, text="Auto", value=2, variable=carType,
                                          font=('arial', 14, 'bold'), command=selectCar).grid(row=1, column=0, sticky=W)
        self.txtPrimeSedan = Label(label, font=('arial', 14, 'bold'), width=7, textvariable=PrimeSedan, bd=5,
                                   state=DISABLED, justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtPrimeSedan.grid(row=2, column=0)

        self.chkPremiumSedan = Radiobutton(label, text="Car", value=3, variable=carType,
                                           font=('arial', 14, 'bold'), command=selectCar).grid(row=1, column=2)
        self.txtPremiumSedan = Label(label, font=('arial', 14, 'bold'), width=7, textvariable=PremiumSedan, bd=5,
                                     state=DISABLED, justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtPremiumSedan.grid(row=2, column=2)

        self.chkSingle = Radiobutton(self.secondpage, text="Single", value=1, variable=journeyType,
                                     font=('arial', 14, 'bold')).place(x=200, y=350)
        self.chkReturn = Radiobutton(self.secondpage, text="Return", value=2, variable=journeyType,
                                     font=('arial', 14, 'bold')).place(x=200, y=400)
        self.chkSpecialsNeeds = Radiobutton(self.secondpage, text="SpecialNeeds", value=3, variable=journeyType,
                                            font=('arial', 14, 'bold')).place(x=200, y=450)

        label2 =LabelFrame(self.secondpage, width=700,height=700, font=('arial',30,'bold'),text="Total", relief=RIDGE,padx=20,pady=10,bd=10) #Label(self.secondpage,text='Choose vehicle', font=('arial', 44, 'bold'), bg='yellow')
        label2.place(x=380,y=340)

        self.lblPaidTax = Label(label2, font=('arial', 14, 'bold'), text="Paid Tax", bd=7)
        self.lblPaidTax.grid(row=0,column=0)
        self.txtPaidTax = Label(label2, font=('arial', 14, 'bold'), textvariable=PaidTax, bd=7, width=26,
                                justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtPaidTax.grid(row=0, column=1)

        self.lblSubTotal = Label(label2, font=('arial', 14, 'bold'), text="Sub Total", bd=7)
        self.lblSubTotal.grid(row=1,column=0)
        self.txtSubTotal = Label(label2, font=('arial', 14, 'bold'), textvariable=SubTotal, bd=7, width=26,
                                 justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtSubTotal.grid(row=1,column=1)

        self.lblTotalCost = Label(label2, font=('arial', 14, 'bold'), text="Total Cost", bd=7)
        self.lblTotalCost.grid(row=2,column=0)
        self.txtTotalCost = Label(label2, font=('arial', 14, 'bold'), textvariable=TotalCost, bd=7, width=26,
                                  justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtTotalCost.grid(row=2,column=1)


        self.btnTotal = Button(label2, padx=18, bd=7, font=('arial', 15, 'bold'), width=3, text='Total',
                               command=Total_Paid).grid(row=3, column=1,pady=10)
        self.btnReset = Button(label2, padx=18, bd=7, font=('arial', 15, 'bold'), width=3, text='Reset',
                               command=Reset).grid(row=3, column=0, padx=10, pady=10)
    #=================================================================================================================

 #===================================================================================================================================

        self.lblFirstname = Label(CustomerName, font=('arial', 14, 'bold'), text="Firstname", bd=7)
        self.lblFirstname.grid(row=0, column=0, sticky=W)
        self.txtFirstname = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Firstname, bd=7, insertwidth=2,
                                  justify=RIGHT)
        self.txtFirstname.grid(row=0, column=1)

        self.lblSurname = Label(CustomerName, font=('arial', 14, 'bold'), text="Surname", bd=7)
        self.lblSurname.grid(row=1, column=0, sticky=W)
        self.txtSurname = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Surname, bd=7, insertwidth=2,
                                justify=RIGHT)
        self.txtSurname.grid(row=1, column=1, sticky=W)

        self.lblAddress = Label(CustomerName, font=('arial', 14, 'bold'), text="Address", bd=7)
        self.lblAddress.grid(row=2, column=0, sticky=W)
        self.txtAddress = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Address, bd=7, insertwidth=2,
                                justify=RIGHT)
        self.txtAddress.grid(row=2, column=1)

        self.lblPostcode = Label(CustomerName, font=('arial', 14, 'bold'), text="Postcode", bd=7)
        self.lblPostcode.grid(row=3, column=0, sticky=W)
        self.txtPostcode = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Postcode, bd=7, insertwidth=2,
                                 justify=RIGHT)
        self.txtPostcode.grid(row=3, column=1)

        self.lblTelephone = Label(CustomerName, font=('arial', 14, 'bold'), text="Telephone", bd=7)
        self.lblTelephone.grid(row=4, column=0, sticky=W)
        self.txtTelephone = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Telephone, bd=7, insertwidth=2,
                                  justify=RIGHT)
        self.txtTelephone.grid(row=4, column=1)

        self.lblMobile = Label(CustomerName, font=('arial', 14, 'bold'), text="Mobile", bd=7)
        self.lblMobile.grid(row=5, column=0, sticky=W)
        self.txtMobile = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Mobile, bd=7, insertwidth=2,
                               justify=RIGHT)
        self.txtMobile.grid(row=5, column=1)

        self.lblEmail = Label(CustomerName, font=('arial', 14, 'bold'), text="Email", bd=7)
        self.lblEmail.grid(row=6, column=0, sticky=W)
        self.txtEmail = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Email, bd=7, insertwidth=2,
                              justify=RIGHT)
        self.txtEmail.grid(row=6, column=1)

        # ========================================================================================================
        self.lblPickup = Label(TravelFrame, font=('arial', 14, 'bold'), text="Pickup", bd=7)
        self.lblPickup.grid(row=0, column=0, sticky=W)

        self.cboPickup = ttk.Combobox(TravelFrame, textvariable=varl1, state='readonly', font=('arial', 20, 'bold'),
                                      width=14)
        self.cboPickup['value'] = ('', 'Swargate', 'Katraj', 'VIIT', 'ShaniwarWada')
        self.cboPickup.current(0)
        self.cboPickup.grid(row=0, column=1)

        self.lblDrop = Label(TravelFrame, font=('arial', 14, 'bold'), text="Drop", bd=7)
        self.lblDrop.grid(row=1, column=0, sticky=W)

        self.cboDrop = ttk.Combobox(TravelFrame, textvariable=varl2, state='readonly', font=('arial', 20, 'bold'),
                                    width=14)
        self.cboDrop['value'] = ('', 'ShaniwarWada', 'VIIT', 'Swargate', 'Katraj')
        self.cboDrop.current(0)
        self.cboDrop.grid(row=1, column=1)

        self.lblPooling = Label(TravelFrame, font=('arial', 14, 'bold'), text="Pooling", bd=7)
        self.lblPooling.grid(row=2, column=0, sticky=W)

        self.cboPooling = ttk.Combobox(TravelFrame, textvariable=varl3, state='readonly', font=('arial', 20, 'bold'),
                                       width=14)
        self.cboPooling['value'] = ('', '1', '2', '3', '4')
        self.cboPooling.current(1)
        self.cboPooling.grid(row=2, column=1)

        # =========================================================================================================

        self.chkTaxiTax = Checkbutton(TravelFrame, text="Taxi Tax(Base Charge) *", variable=var1, onvalue=1, offvalue=0,
                                      font=('arial', 16, 'bold'), command=Taxi_Tax).grid(row=3, column=0, sticky=W)
        self.txtTaxiTax = Label(TravelFrame, font=('arial', 14, 'bold'), textvariable=TaxiTax, bd=6, width=18,
                                bg="white", state=DISABLED, justify=RIGHT, relief=SUNKEN)
        self.txtTaxiTax.grid(row=3, column=1)

        self.chkKm = Checkbutton(TravelFrame, text="Distance(KMs) *", variable=var2, onvalue=1, offvalue=0,
                                 font=('arial', 16, 'bold'), command=Kilo).grid(row=4, column=0, sticky=W)
        self.txtKm = Label(TravelFrame, font=('arial', 14, 'bold'), textvariable=Km, bd=6, width=18, bg="white",
                           state=DISABLED, justify=RIGHT, relief=SUNKEN, highlightthickness=0)
        self.txtKm.grid(row=4, column=1)

        self.chkTravel_Ins = Checkbutton(TravelFrame, text="Travelling Insurance *", variable=var3, onvalue=1,
                                         offvalue=0, font=('arial', 16, 'bold'), command=Travelling).grid(row=5,
                                                                                                          column=0,
                                                                                                          sticky=W)
        self.txtTravel_Ins = Label(TravelFrame, font=('arial', 14, 'bold'), textvariable=Travel_Ins, bd=6, width=18,
                                   bg="white", state=DISABLED, justify=RIGHT, relief=SUNKEN)
        self.txtTravel_Ins.grid(row=5, column=1)

        self.chkLuggage = Checkbutton(TravelFrame, text="Extra Luggage", variable=var4, onvalue=1, offvalue=0,
                                      font=('arial', 16, 'bold'), command=Lug).grid(row=6, column=0, sticky=W)
        self.txtLuggage = Label(TravelFrame, font=('arial', 14, 'bold'), textvariable=Luggage, bd=6, width=18,
                                bg="white", state=DISABLED, justify=RIGHT, relief=SUNKEN)
        self.txtLuggage.grid(row=6, column=1)
        # ========================================================================================================
        self.thridpage = Frame(MainFrame, bg="white")

        self.btnnext2 = Button(self.thridpage, padx=18, bd=7, font=('arial', 15, 'bold'), width=2, text='Back',
                               command=back2)
        self.btnnext2.place(x=10, y=10)

        img3 = Image.open("2ndpage (1).jpg")
        photo3 = ImageTk.PhotoImage(img3)
        imgbg1 = Label(self.thridpage, image=photo3)
        imgbg1.place(x=1060, y=140)



        # ========================================================================================================
        self.lblPaidTax = Label(CostFrame, font=('arial', 14, 'bold'), text="Paid Tax", bd=7)
        self.lblPaidTax.grid(row=0, column=0)
        self.txtPaidTax = Label(CostFrame, font=('arial', 14, 'bold'), textvariable=PaidTax, bd=7, width=26,
                                justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtPaidTax.grid(row=0, column=1)

        self.lblSubTotal = Label(CostFrame, font=('arial', 14, 'bold'), text="Sub Total", bd=7)
        self.lblSubTotal.grid(row=1, column=0)
        self.txtSubTotal = Label(CostFrame, font=('arial', 14, 'bold'), textvariable=SubTotal, bd=7, width=26,
                                 justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtSubTotal.grid(row=1, column=1)

        self.lblTotalCost = Label(CostFrame, font=('arial', 14, 'bold'), text="Total Cost", bd=7)
        self.lblTotalCost.grid(row=2, column=0)
        self.txtTotalCost = Label(CostFrame, font=('arial', 14, 'bold'), textvariable=TotalCost, bd=7, width=26,
                                  justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtTotalCost.grid(row=2, column=1)
        # ========================================================================================================





        # ========================================================================================================

if __name__ == '__main__':
    root = Tk()

    # =========================================== Getting Screen Width ==================================================================
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    geometry = "%dx%d+%d+%d" % (w, h, 0, 0)

    root.geometry("500x300+320+200")
    root.title('Login Form')
    application = user(root)
    root.mainloop()