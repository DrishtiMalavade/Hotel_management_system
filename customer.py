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
        self.root.geometry("1330x565+200+220")
        
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
        label_title.place(x=0,y=0,width=1330,height=50)

        #label frame 
        labelframeleft = LabelFrame(self.root,text="Customer Details",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=7,y=56,width=470,height=497)

        #labels and entry
        #customer ref
        label_custref= Label(labelframeleft, text="Customer Ref ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_custref.grid(row=0,column=0, sticky=W)

        entry_ref= ttk.Entry(labelframeleft, textvariable=self.varRef,width=39,font=("times new roman",12,"bold"), state="readonly")
        entry_ref.grid(row=0,column=1)

        #customer name
        label_custname= Label(labelframeleft, text="Customer Name ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_custname.grid(row=1,column=0, sticky=W)

        entry_name= ttk.Entry(labelframeleft, textvariable=self.varName, width=39,font=("times new roman",12,"bold"))
        entry_name.grid(row=1,column=1)

        #mother name
        label_momname= Label(labelframeleft, text="Mothers Name ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_momname.grid(row=2,column=0, sticky=W)

        entry_momname= ttk.Entry(labelframeleft,textvariable=self.varMomname, width=39,font=("times new roman",12,"bold"))
        entry_momname.grid(row=2,column=1)
        
        #gender
        label_gender= Label(labelframeleft, text="Gender ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_gender.grid(row=3,column=0, sticky=W)

        gender_box= ttk.Combobox(labelframeleft,textvariable=self.varGender, font=("times new roman",12,"bold"), width=37, state="readonly")
        gender_box["value"]=("Male", "Female", "Non Binary", "Prefer not to say")
        gender_box.grid(row=3, column=1)

        #postal code
        label_postcode= Label(labelframeleft, text="Post Code ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_postcode.grid(row=4,column=0, sticky=W)

        entry_postcode= ttk.Entry(labelframeleft,textvariable=self.varPost, width=39,font=("times new roman",12,"bold"))
        entry_postcode.grid(row=4,column=1)

        #mobile number
        label_mobile= Label(labelframeleft, text="Mobile Number ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_mobile.grid(row=5,column=0, sticky=W)

        entry_mobile= ttk.Entry(labelframeleft, textvariable=self.varMobile ,width=39,font=("times new roman",12,"bold"))
        entry_mobile.grid(row=5,column=1)

        #email
        label_email= Label(labelframeleft, text="Email ID ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_email.grid(row=6,column=0, sticky=W)

        entry_email= ttk.Entry(labelframeleft,textvariable=self.varEmail, width=39,font=("times new roman",12,"bold"))
        entry_email.grid(row=6,column=1)

        #nationality
        label_nationality= Label(labelframeleft, text="Nationality ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_nationality.grid(row=7,column=0, sticky=W)

        entry_nationality= ttk.Entry(labelframeleft,textvariable=self.varNationality, width=39,font=("times new roman",12,"bold"))
        entry_nationality.grid(row=7,column=1)

        #id proof
        label_custid= Label(labelframeleft, text="Id Proof ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_custid.grid(row=8,column=0, sticky=W)

        id_box= ttk.Combobox(labelframeleft,textvariable=self.varIdproof, font=("times new roman",12,"bold"), width=37, state="readonly")
        id_box["value"]=("Passport", "Driving Licence", "Pan Card", "Other")
        id_box.grid(row=8, column=1)

        #id number
        label_custidnum= Label(labelframeleft, text="Id Number ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_custidnum.grid(row=9,column=0, sticky=W)

        entry_idnum= ttk.Entry(labelframeleft,textvariable=self.varIdnum, width=39,font=("times new roman",12,"bold"))
        entry_idnum.grid(row=9,column=1)

        #address
        label_add= Label(labelframeleft, text="Address ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_add.grid(row=10,column=0, sticky=W)

        entry_add= ttk.Entry(labelframeleft,textvariable=self.varAddress, width=39,font=("times new roman",12,"bold"))
        entry_add.grid(row=10,column=1)

        #buttons
        btn_frame= Frame(labelframeleft, bd=2)
        btn_frame.place(x=0,y=388, width=450,height=40)

        #add entry
        btnAdd= Button(btn_frame, text="Add", command=self.add_data, font=("times new roman",10,"bold"), bg="#002b64", fg="#fefcf0", width=12)
        btnAdd.grid(row=0,column=0, padx=9)

        #update
        btnUpd= Button(btn_frame, text="Update", command=self.update, font=("times new roman",10,"bold"), bg="#002b64", fg="#fefcf0", width=12)
        btnUpd.grid(row=0,column=1, padx=9)

        #delete
        btnDel= Button(btn_frame, text="Delete", command=self.delete, font=("times new roman",10,"bold"), bg="#002b64", fg="#fefcf0", width=12)
        btnDel.grid(row=0,column=2, padx=9)

        #reset
        btnReset= Button(btn_frame, text="Reset", command=self.reset, font=("times new roman",10,"bold"), bg="#002b64", fg="#fefcf0", width=12)
        btnReset.grid(row=0,column=3, padx=9)
    
        #table frame for search 
        tableframe= LabelFrame(self.root,text="View Details and Search System",padx=2,font=("times new roman",12,"bold"))
        tableframe.place(x=482,y=56,width=840,height=497)
        
        label_search= Label(tableframe, text="Search By ", font=("times new roman",12,"bold"), bg="#002b64", fg="#fefcf0")
        label_search.grid(row=0,column=0, sticky=W)

        self.search_var= StringVar()
        searchbox= ttk.Combobox(tableframe, textvariable=self.search_var, font=("times new roman",12,"bold"), width=32, state="readonly")
        searchbox["value"] = ("mobile", "ref", "name")

        searchbox.grid(row=0, column=1)

        self.search_txt= StringVar()
        txtsearch= ttk.Entry(tableframe, textvariable=self.search_txt, font=("times new roman",12,"bold"), width=32)
        txtsearch.grid(row=0,column=2, padx=5)

        btnSearch= Button(tableframe, text="Search", command=self.search, font=("times new roman",10,"bold"), bg="#002b64", fg="#fefcf0", width=10)
        btnSearch.grid(row=0,column=3, padx=5)

        btnShowall= Button(tableframe, text="Show All", command=self.fetch_data, font=("times new roman",10,"bold"), bg="#002b64", fg="#fefcf0", width=10)
        btnShowall.grid(row=0,column=4, padx=5)

        #show data table
        details_frame= Frame(tableframe, bd=2, relief= RIDGE)
        details_frame.place(x=0,y=40, width=805,height=430)

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
        if self.varMobile.get().strip() == "" or self.varMomname.get().strip() == "": #########
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
            return
        else:
            try:
                conn= mysql.connector.connect(host= "localhost", username="root", password=" ", database=" ") #your mysql password here
                myCursor= conn.cursor()
                myCursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.varRef.get(),self.varName.get(),self.varMomname.get(),self.varGender.get(),self.varPost.get(),self.varMobile.get(),self.varEmail.get(),self.varNationality.get(),self.varIdproof.get(),self.varIdnum.get(),self.varAddress.get()))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer Has Been Added", parent= self.root)

            except Exception as es:
                messagebox.showerror("Warning", f"Something Went Wrong:{str(es)}", parent= self.root)

    def fetch_data(self):
        conn= mysql.connector.connect(host= "localhost", username="root", password=" ", database=" ") #your mysql password here
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
            conn= mysql.connector.connect(host= "localhost", username="root", password=" ", database=" ") #your mysql password here
            myCursor= conn.cursor()
            myCursor.execute("update customer set name=%s, momname=%s, gender=%s, postcode=%s, mobile=%s, email=%s, nationality=%s, idproof=%s, idnumber=%s, address=%s where ref=%s", (self.varName.get(),self.varMomname.get(),self.varGender.get(),self.varPost.get(),self.varMobile.get(),self.varEmail.get(),self.varNationality.get(),self.varIdproof.get(),self.varIdnum.get(),self.varAddress.get(),self.varRef.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "User Updated Successfully", parent= self.root)

    def delete(self):
        delete= messagebox.askyesno("Hotel management system", "Do you want to delete this customer", parent= self.root)
        if delete>0:
            conn= mysql.connector.connect(host= "localhost", username="root", password=" ", database=" ")
            myCursor= conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.varRef.get(),)
            myCursor.execute(query,value)
            #myCursor.execute("")    
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


    def reset(self):
        #self.varRef.set("")
        self.varName.set("")
        self.varMomname.set("")
        self.varGender.set("")
        self.varPost.set("")
        self.varMobile.set("")
        self.varEmail.set("")
        self.varNationality.set("")
        self.varIdproof.set("")
        self.varIdnum.set("")
        self.varAddress.set("")

        x= random.randint(1000,9999)
        self.varRef.set(str(x))

    def search(self):
        conn= mysql.connector.connect(host= "localhost", username="root", password=" ", database=" ")
        myCursor= conn.cursor()
        myCursor.execute("select * from customer where " + str(self.search_var.get()) + " LIKE '%" + str(self.search_txt.get()) + "%'")

        rows= myCursor.fetchall()
        if len (rows)!=0:
            self.cust_datalist.delete(*self.cust_datalist.get_children())
            for i in rows:
                self.cust_datalist.insert("", END, values=i)
            
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = CustomerWindow(root)
    root.mainloop()

