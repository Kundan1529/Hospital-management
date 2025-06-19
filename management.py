from tkinter import * 
from tkinter import ttk
import random 
import time
import datetime
from tkinter import messagebox 
import mysql.connector 

class Hospital:
    def __init__(self, root):
        self.root = root 
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        
        self.NameofTablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEfect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachinge = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientName = StringVar()
        self.DateofBirth = StringVar()
        self.PatientAddress = StringVar()
        
        
        lbltitle = Label(self.root,bd=20,relief = RIDGE,text="Hospital Managemet System",fg ="red",bg='white',font=('Sans sarif',50,"bold"))
        lbltitle.pack(side=TOP,fill=X)
        # ___________________________
        Dataframe = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)
        
        Dataframeleft = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=('Sans sarif',12,"bold"),text="Patient Information")
        Dataframeleft.place(x=0,y=5,width=980,height=350)
        
        DataframeRight = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=('Sans sarif',12,"bold"),text="Prescription")
        DataframeRight.place(x=990,y=5,width=460,height=350)
        
        # -----------buttons Frame ---------
        Buttonframe = Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)
        
        # -----------Details  Frame ---------
        Detailsframe = Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)
        
        #=====================DataFrameLeft======================
        lblNameTablet = Label(Dataframeleft,text='Names of Tablet', font=('Sans sarif',12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)
        
        comNametablet = ttk.Combobox(Dataframeleft, textvariable=self.NameofTablets,font=('Sans sarif',12,"bold"),width=33)
        comNametablet['values']=("Nice","Corona vaccine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNametablet.grid(row=0,column=1)
        
        lblref = Label(Dataframeleft,font=('arial',12,'bold'),text='Reference no', padx=2)
        lblref.grid(row=1,column=0, sticky=W)
        txtref = Entry(Dataframeleft,textvariable=self.ref ,font=('arial',12,'bold'), width=35)
        txtref.grid(row=1,column=1)
        
        lblDose= Label(Dataframeleft,font=('arial',12,'bold'),text='Dose',padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose= Entry(Dataframeleft,textvariable=self.Dose ,font=('arial',12,'bold'),width=35 )
        txtDose.grid(row=2,column=1)
        
        lblNooftablets = Label(Dataframeleft,font=('arial',12,'bold'), text="No of Tablets", padx=2, pady=6)
        lblNooftablets.grid(row=3,column=0,sticky=W)
        txtNooftablets = Entry(Dataframeleft,textvariable=self.NumberofTablets,font=('arial',12,'bold'),width=35)
        txtNooftablets.grid(row=3,column=1)
        
        lblLot = Label(Dataframeleft,font=('arial',12,'bold'),text="Lot",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot = Entry(Dataframeleft, textvariable=self.Lot,font=('arial',12,'bold'), width=35)
        txtLot.grid(row=4,column=1)
        
        lblissueDate = Label(Dataframeleft,font=('arial',12,'bold'),text='Issue Date',padx=2,pady=6)
        lblissueDate.grid(row=5,column=0, sticky=W)
        txtissueDate = Entry(Dataframeleft, textvariable=self.Issuedate,font=('arial',12,'bold'),width=35)
        txtissueDate.grid(row=5,column=1)
        
        lblExpDate = Label(Dataframeleft,font=('arial',12,'bold'), text='Exp Date:', padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate = Entry(Dataframeleft, self.ExpDate,font=('arial',12,'bold'),width=35)
        txtExpDate.grid(row=6,column=1)
        
        lblDailyDose = Label(Dataframeleft,font=('arial',12,'bold'),text="Daly Dose:",padx=2, pady=6)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(Dataframeleft, textvariable=self.DailyDose,font=('arial',12,'bold'),width=35)
        txtDailyDose.grid(row=7,column=1)
        
        lblSideEffect = Label(Dataframeleft,font=('arial',12,'bold'),text="Side Effect", padx=2, pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect = Entry(Dataframeleft, textvariable=self.sideEfect,font=('arial',12,'bold'),width=35)
        txtSideEffect.grid(row=8,column=1)
        
        lblfurtherinfo = Label(Dataframeleft,font=('arial',12,'bold'),text="Further Information", padx=2)
        lblfurtherinfo.grid(row=0,column=2,sticky=W)
        txtfurtherinfo = Entry(Dataframeleft,textvariable=self.FurtherInformation,font=('arial',12,'bold'),width=35)
        txtfurtherinfo.grid(row=0,column=3)
        
        lblBloodPressure = Label(Dataframeleft,font=('arial',12,'bold'),text="Blood Pressure", padx=2, pady=6)
        lblBloodPressure.grid(row=1, column=2,sticky=W)
        txtBloodPressure = Entry(Dataframeleft,font=('arial',12,'bold'),width=35)
        txtBloodPressure.grid(row=1, column=3)
        
        
        lblStorage = Label(Dataframeleft,font=('arial',12,'bold'), text="Storage Advice", padx=2, pady=6) 
        lblStorage.grid(row=2, column=2 , sticky=W)
        txtStorage = Entry(Dataframeleft,textvariable=self.StorageAdvice,font=('arial',12,'bold'),width=35)
        txtStorage.grid(row=2,column=3)
        
        lblMedicine = Label(Dataframeleft,font=('arial',12,'bold'), text="Medicatin", padx=2, pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W) 
        txtMedicine = Entry(Dataframeleft,textvariable=self.txtPrescription, font=('arial',12,'bold'), width=35) 
        txtMedicine.grid(row=3, column=3, sticky=W)
        
        lblPatientId = Label(Dataframeleft, font=('arial',12,'bold'),text="Patient Id", padx=2, pady=6)
        lblPatientId.grid(row=4 , column=2, sticky=W)
        txtPatientId = Entry(Dataframeleft,font=('arial',12,'bold'), width=35) 
        txtPatientId.grid(row=4, column=3) 
        
        lblNhsNumber = Label(Dataframeleft, font=('arial',12,'bold'),text="NHS Number", padx=2, pady=6) 
        lblNhsNumber.grid(row=5, column=2, sticky=W) 
        txtNhsNumber = Entry(Dataframeleft,font=('arial',12,'bold'), width=35) 
        txtNhsNumber.grid(row=5, column=3) 
        
        lblPatientName = Label(Dataframeleft, font=('arial',12,'bold'),text="Patient Name", padx=2, pady=6) 
        lblPatientName.grid(row=6, column=2, sticky=W)
        txtPatientName = Entry(Dataframeleft,textvariable=self.PatientName,font=('arial',12,'bold'),width=35) 
        txtPatientName.grid(row=6, column=3) 
        
        lblDateOfBirth = Label(Dataframeleft, font=('arial',12,'bold'),text="Date of Birth", padx=2, pady=6) 
        lblDateOfBirth.grid(row=7, column=2 , sticky=W) 
        txtDateOfBirth = Entry(Dataframeleft,textvariable=self.DateofBirth, font=('arial',12,'bold'),width=35) 
        txtDateOfBirth.grid(row=7, column=3) 
        
        lblPatientAddress = Label(Dataframeleft,font=('arial',12,'bold'), text="Patient Address", padx=2, pady=6) 
        lblPatientAddress.grid(row=8, column=2, sticky=W) 
        txtPatientAddress = Entry(Dataframeleft, textvariable=self.PatientAddress, font=('arial',12,'bold'), width=35) 
        txtPatientAddress.grid(row=8, column=3)
        
        
        
        # ================DataframeRight================ 
        self.txtPrescription = Text(DataframeRight,font=('arial',12,'bold'), width=45,height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0,column=0)
        
        
        
        #===========Buttons==================
        btnPrescription = Button(Buttonframe,command=self.iPrectioption, text="Prescription",bg = 'green', fg='white', font=('arial',12,'bold'),width=23, height=1, padx=2, pady=6)
        btnPrescription.grid(row=0, column=0) 
        
        btnPrescriptionData  = Button(Buttonframe, text="Prescription Data",bg ='green',fg ='white', font=('arial',12,'bold'),width=23, height=1, padx=2, pady=6)
        btnPrescriptionData.grid(row=0, column=1) 
        
        
        btnUpdate = Button(Buttonframe,command=self.update, text="Update ",bg = 'green',fg='white',  font=('arial',12,'bold'),width=23, height=1, padx=2, pady=6)
        btnUpdate.grid(row=0, column=2) 
        
        
        btnDelete = Button(Buttonframe,command=self.idelete, text="Delete",bg = 'green',fg="white", font=('arial',12,'bold'),width=23, height=1, padx=2, pady=6)
        btnDelete.grid(row=0, column=3) 

        btnClear = Button(Buttonframe,command=self.clear, text="Clear",bg = 'green',fg="white",  font=('arial',12,'bold'),width=23, height=1, padx=2, pady=6)
        btnClear.grid(row=0, column=4) 
        
        btnExit = Button(Buttonframe,command=self.iExit, text="Exit",bg = 'green', fg="white", font=('arial',12,'bold'),width=23, height=1, padx=2, pady=6)
        btnExit.grid(row=0, column=5) 
        
        
        
        # =============Table =======================
        # =============Scrollbar==============
        
        scroll_x = ttk.Scrollbar(Detailsframe, orient= HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        # Correct Treeview columns definition (note the spelling consistency)
        self.hospital_table = ttk.Treeview(Detailsframe, columns=(
            'nameoftable',  # Changed from 'namoftable' to match heading
            'ref', 
            'dose',
            'nooftablets',
            'lot', 
            'issuedate', 
            'expdate', 
            'dailydose', 
            'storage', 
            'nhsnumber',
            'pname',
            'dob',
            'address'
        ), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Remove these redundant lines - they're already declared above
        # scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        # scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        # Set headings (must exactly match column names above)
        self.hospital_table.heading('nameoftable', text="Name of Tablets")  # Now matches
        self.hospital_table.heading('ref', text="Reference no.")  # Fixed spelling
        self.hospital_table.heading('dose', text="Dose")
        self.hospital_table.heading('nooftablets', text="No of Tablets")
        self.hospital_table.heading('lot', text="Lot")
        self.hospital_table.heading('issuedate', text="Issue Date")
        self.hospital_table.heading('expdate', text="Exp date")
        self.hospital_table.heading('dailydose', text="Daily Dose")
        self.hospital_table.heading('storage', text="Storage")
        self.hospital_table.heading('nhsnumber', text="NHS number")
        self.hospital_table.heading('pname', text="Patient Name")
        self.hospital_table.heading('dob', text="DOB")
        self.hospital_table.heading('address', text="Address")

        self.hospital_table['show'] = 'headings'
        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
        
        self.hospital_table.column('nameoftable',width=100)
        self.hospital_table.column('ref',width=100)
        self.hospital_table.column('dose',width=100)
        self.hospital_table.column('nooftablets',width=100)
        self.hospital_table.column('lot',width=100)
        self.hospital_table.column('issuedate',width=100)
        self.hospital_table.column('expdate',width=100)
        self.hospital_table.column('dailydose',width=100)
        self.hospital_table.column('storage',width=100)
        self.hospital_table.column('nhsnumber',width=100)
        self.hospital_table.column('pname',width=100)
        self.hospital_table.column('dob',width=100)
        self.hospital_table.column('address',width=100)
        self.fetch_data()
        
     # ====================Functionality Declaration ================
    def iPrescriptionData(self):
        if self.NameofTablets.get() =="" or self.ref.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn = mysql.connector.connect(host = 'localhost', username = "root", password = "Test@123", database = "Mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s, %s, %s, %s, %s, %s ,%s,%s, %s, %s, %s, %s,)",(self.NameofTablets.get(),
                                                                                                                self.ref.get(),
                                                                                                                self.Dose.get(),
                                                                                                                self.NumberofTablets.get(),
                                                                                                                self.Lot.get(),
                                                                                                                self.Issuedate.get(),
                                                                                                                self.ExpDate.get(),
                                                                                                                self.ExpDate.get(),
                                                                                                                self.DailyDose.get(),
                                                                                                                self.StorageAdvice.get(),
                                                                                                                self.PatientName.get(),
                                                                                                                self.DateofBirth.get(),
                                                                                                                self.PatientAddress.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            
    def update(self):
        conn = mysql.connector.connect(host = 'localhost', username = "root", password = "Test@123", database = "Mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("update hospital set nameoftable = %s,dose=%s,nooftablets=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,storage=%s,nhsnumber=%s,pname=%s,dob=%s,address=%s where ref= %s ",(self.NameofTablets.get(),
                                                                                                                
                                                                                                                self.Dose.get(),
                                                                                                                self.NumberofTablets.get(),
                                                                                                                self.Lot.get(),
                                                                                                                self.Issuedate.get(),
                                                                                                                self.ExpDate.get(),
                                                                                                                self.ExpDate.get(),
                                                                                                                self.DailyDose.get(),
                                                                                                                self.StorageAdvice.get(),
                                                                                                                self.PatientName.get(),
                                                                                                                self.DateofBirth.get(),
                                                                                                                self.PatientAddress.get(),
                                                                                                                self.ref.get(),))
        
               
    def fetch_data(self):
        conn = mysql.connector.connect(host = 'localhost', username = "root", password = "Test@123", database = "Mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital ")
        rows = my_cursor.fetchall()
        if len(rows) !=0:
            self.hospital_table.delete(self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert(" ",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self, event="" ):
        cursor_rows = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_rows)
        row = content["values"]
        self.NameofTablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.PatientName.set(row[10])
        self.DateofBirth.set(row[11])
        self.PatientAddress.set(row[12])
        
    def iPrectioption(self):
        self.txtPrescription.insert(END,"name of Tablets:\t\t\t"+ self.NameofTablets.get() + "\n")
        
        
        
    def idelete(self):  
        conn = mysql.connector.connect(host = 'localhost', username = "root", password = "Test@123", database = "Mydata")
        my_cursor = conn.cursor()
        query = "delete from  hospital where ref = %s"
        value =(self.ref.get(),)
        my_cursor.execute(query,value)
        
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Patient has been deleted successfully")
      
    def clear(self):
        self.NameofTablets.set("")
        self.ref.ser("")  
        
        
    def iExit(self):
        iExit = messagebox.askyesno("Hospital management system","Confirm you want to exit")
        if iExit >0:
            root.destroy()
            return 
        
        
        
        
        
        
        
        
        
        
        
        
        
root = Tk()
ob = Hospital(root)
root.mainloop()