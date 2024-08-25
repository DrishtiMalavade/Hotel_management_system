from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class CustomerWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer")
        self.root.geometry("1170x520+190+183")
        #self.root.configure(bg="#f0f0f0")
        
        #variables
        self.varRef= StringVar()
        x= random.randint(1000,9999)
        self.varRef.set(str(x))

        self.varName= StringVar()
        self.varMomname= StringVar()
        self.varGender= StringVar()
        self.varPost= StringVar()
        self.varMobile= StringVar()
        self.varEmail= StringVar()
        self.varName= StringVar()
        self.varNationality= StringVar()
        self.varAddress= StringVar()
        self.varIdproof= StringVar()
        self.varIdnum= StringVar()


        #title
        label_title = Label(self.root, text="Add Customer Details", font=("times new roman",18,"bold"), bg="#002b64", fg="#fefcf0")
        label_title.place(x=0,y=0,width=1170,height=50)

        #label frame
        labelframeleft = LabelFrame(self.root,text="Customer Details",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=450)

        #labels and entry
        #customer ref
        label_custref= Label(labelframeleft, text="Customer Ref ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_custref.grid(row=0,column=0, sticky=W)

        entry_ref= ttk.Entry(labelframeleft, width=29,font=("times new roman",12,"bold"))
        entry_ref.grid(row=0,column=1)

        #customer name
        label_custname= Label(labelframeleft, text="Customer Name ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_custname.grid(row=1,column=0, sticky=W)

        entry_name= ttk.Entry(labelframeleft, width=29,font=("times new roman",12,"bold"))
        entry_name.grid(row=1,column=1)

        #mother name
        label_momname= Label(labelframeleft, text="Mothers Name ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_momname.grid(row=2,column=0, sticky=W)

        entry_momname= ttk.Entry(labelframeleft, width=29,font=("times new roman",12,"bold"))
        entry_momname.grid(row=2,column=1)
        
        #gender
        label_gender= Label(labelframeleft, text="Gender ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_gender.grid(row=3,column=0, sticky=W)

        gender_box= ttk.Combobox(labelframeleft, font=("times new roman",12,"bold"), width=27, state="readonly")
        gender_box["value"]=("Male", "Female", "Non Binary", "Prefer not to say")
        gender_box.grid(row=3, column=1)

        #postal code
        label_postcode= Label(labelframeleft, text="Post Code ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_postcode.grid(row=4,column=0, sticky=W)

        entry_postcode= ttk.Entry(labelframeleft, width=29,font=("times new roman",12,"bold"))
        entry_postcode.grid(row=4,column=1)

        #mobile number
        label_mobile= Label(labelframeleft, text="Mobile Number ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_mobile.grid(row=5,column=0, sticky=W)

        entry_mobile= ttk.Entry(labelframeleft, width=29,font=("times new roman",12,"bold"))
        entry_mobile.grid(row=5,column=1)

        #email
        label_email= Label(labelframeleft, text="Email ID ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_email.grid(row=6,column=0, sticky=W)

        entry_email= ttk.Entry(labelframeleft, width=29,font=("times new roman",12,"bold"))
        entry_email.grid(row=6,column=1)

        #nationality
        label_nationality= Label(labelframeleft, text="Nationality ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_nationality.grid(row=7,column=0, sticky=W)

        entry_nationality= ttk.Entry(labelframeleft, width=29,font=("times new roman",12,"bold"))
        entry_nationality.grid(row=7,column=1)

        #id proof
        label_custid= Label(labelframeleft, text="Id Proof ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_custid.grid(row=8,column=0, sticky=W)

        id_box= ttk.Combobox(labelframeleft, font=("times new roman",12,"bold"), width=27, state="readonly")
        id_box["value"]=("Passport", "Driving Liscense", "Pan Card", "Other")
        id_box.grid(row=8, column=1)

        #id number
        label_custidnum= Label(labelframeleft, text="Id Number ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_custidnum.grid(row=9,column=0, sticky=W)

        entry_idnum= ttk.Entry(labelframeleft, width=29,font=("times new roman",12,"bold"))
        entry_idnum.grid(row=9,column=1)

        #address
        label_add= Label(labelframeleft, text="Address ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_add.grid(row=10,column=0, sticky=W)

        entry_add= ttk.Entry(labelframeleft, width=29,font=("times new roman",12,"bold"))
        entry_add.grid(row=10,column=1)

        #buttons
        btn_frame= Frame(labelframeleft, bd=2)
        btn_frame.place(x=0,y=390, width=412,height=40)

        #add entry
        btnAdd= Button(btn_frame, text="Add", command=self.add_data, font=("times new roman",10,"bold"), bg="#002b64", fg="#fefcf0", width=10)
        btnAdd.grid(row=0,column=0, padx=5)

        #update
        btnUpd= Button(btn_frame, text="Update", command=self.update, font=("times new roman",10,"bold"), bg="#002b64", fg="#fefcf0", width=10)
        btnUpd.grid(row=0,column=1, padx=5)

        #delete
        btnDel= Button(btn_frame, text="Delete", font=("times new roman",10,"bold"), bg="#002b64", fg="#fefcf0", width=10)
        btnDel.grid(row=0,column=2, padx=5)

        #reset
        btnReset= Button(btn_frame, text="Reset", font=("times new roman",10,"bold"), bg="#002b64", fg="#fefcf0", width=10)
        btnReset.grid(row=0,column=3, padx=5)
    
        #table frame
        tableframe= LabelFrame(self.root,text="View Details and Search System",padx=2,font=("times new roman",12,"bold"))
        tableframe.place(x=435,y=50,width=733,height=450)


        label_search= Label(tableframe, text="Search By ", font=("times new roman",12,"bold"), bg="#002b64", fg="#fefcf0")
        label_search.grid(row=0,column=0, sticky=W)

        searchbox= ttk.Combobox(tableframe, font=("times new roman",12,"bold"), width=27, state="readonly")
        searchbox["value"]=("Mobile Number", "Reference numer", "Name")
        searchbox.grid(row=0, column=1)

        txtsearch= ttk.Entry(tableframe, font=("times new roman",12,"bold"), width=27)
        txtsearch.grid(row=0,column=2, padx=5)

        btnSearch= Button(tableframe, text="Add", font=("times new roman",10,"bold"), bg="#002b64", fg="#fefcf0", width=10)
        btnSearch.grid(row=0,column=3, padx=5)

        btnShowall= Button(tableframe, text="Update", font=("times new roman",10,"bold"), bg="#002b64", fg="#fefcf0", width=10)
        btnShowall.grid(row=0,column=4, padx=5)

        #show data table

        details_frame= Frame(tableframe, bd=2, relief= RIDGE)
        details_frame.place(x=0,y=40, width=720,height=380)

        scroll_x= ttk.Scrollbar(details_frame, orient= HORIZONTAL)
        scroll_y= ttk.Scrollbar(details_frame, orient= VERTICAL)

        self.cust_datalist = ttk.Treeview(details_frame, column=("ref", "name", "momname", "gender", "postcode", "mobile", "email", "nationality", "idproof", "idnumber", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.cust_datalist.xview)
        scroll_y.config(command=self.cust_datalist.yview)

        self.cust_datalist.heading("ref", text="Customer Ref")
        self.cust_datalist.heading("name", text="Name")
        self.cust_datalist.heading("momname", text="Mothers Name")
        self.cust_datalist.heading("gender", text="Gender")
        self.cust_datalist.heading("postcode", text="Postcode")
        self.cust_datalist.heading("mobile", text="Mobile")
        self.cust_datalist.heading("email", text="Email")
        self.cust_datalist.heading("nationality", text="Nationality")
        self.cust_datalist.heading("idproof", text="ID Proof")
        self.cust_datalist.heading("idnumber", text="ID Number")
        self.cust_datalist.heading("address", text="Address")

        self.cust_datalist["show"] = "headings"

        self.cust_datalist.column("ref", width= 100)
        self.cust_datalist.column("name", width=100)
        self.cust_datalist.column("momname", width=100)
        self.cust_datalist.column("gender", width=100)
        self.cust_datalist.column("postcode", width=100)
        self.cust_datalist.column("mobile", width=100)
        self.cust_datalist.column("email", width=150)
        self.cust_datalist.column("nationality", width= 100)
        self.cust_datalist.column("idproof", width= 100)
        self.cust_datalist.column("idnumber", width= 100)

        self.cust_datalist.pack(fill=BOTH, expand=1)
        self.cust_datalist.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.varMobile.get()=="" or self.varMomname.get()=="":
            messagebox.showerror("Error", "All Fields Are Required", parent= self.root)
        else:
            try:
                conn= mysql.connector.connect(host= "localhost", username="root", password=" ", database="hotelmanagement") #your mysql password here
                myCursor= conn.cursor()
                myCursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.varRef.get(),self.varName.get(),self.varMomname.get(),self.varGender.get(),self.varPost.get(),self.varMobile.get(),self.varEmail.get(),self.varNationality.get(),self.varIdproof.get(),self.varIdnum.get(),self.varAddress.get()))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer Has Been Added", parent= self.root)

            except Exception as es:
                messagebox.showerror("Warning", f"Something Went Wrong:{str(es)}", parent= self.root)


    def fetch_data(self):
        conn= mysql.connector.connect(host= "localhost", username="root", password=" ", database="hotelmanagement") #your rmysql password here
        myCursor= conn.cursor()
        myCursor.execute("select * from customer")
        dataRows= myCursor.fetchall()
        if len(dataRows)!=0:
            self.cust_datalist.delete(*self.cust_datalist.get_children())
            for i in dataRows:
                self.cust_datalist.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursorRow= self.cust_datalist.focus()
        content= self.cust_datalist.item(cursorRow)
        row= content["values"]

        self.varRef.set(row[0])
        self.varName.set(row[1])
        self.varMomname.set(row[2])
        self.varGender.set(row[3])
        self.varPost.set(row[4])
        self.varMobile.set(row[5])
        self.varEmail.set(row[6])
        self.varNationality.set(row[7])
        self.varIdproof.set(row[8])
        self.varIdnum.set(row[9])
        self.varAddress.set(row[10])

    def update(self):
        if self.varMobile.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number", parent= self.root)
        else:
            conn= mysql.connector.connect(host= "localhost", username="root", password=" ", database="hotelmanagement") #your mysql password here
            myCursor= conn.cursor()
            myCursor.execute("update customer set name=%s, momname=%s, gender=%s, postcode=%s, mobile=%s, email=%s, nationality=%s, idproof=%s, idnumber=%s, address=%s where ref=%s", (self.varName.get(),self.varMomname.get(),self.varGender.get(),self.varPost.get(),self.varMobile.get(),self.varEmail.get(),self.varNationality.get(),self.varIdproof.get(),self.varIdnum.get(),self.varAddress.get(),self.varRef.get()))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "User Updated Successfully", parent= self.root)






if __name__ == "__main__":
    root = Tk()
    obj = CustomerWindow(root)
    root.mainloop()

