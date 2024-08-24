from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk


class CustomerWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer")
        self.root.geometry("1170x520+190+183")
        #self.root.configure(bg="#f0f0f0")

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
        btnAdd= Button(btn_frame, text="Add", font=("times new roman",10,"bold"), bg="#002b64", fg="#fefcf0", width=10)
        btnAdd.grid(row=0,column=0, padx=5)

        #update
        btnUpd= Button(btn_frame, text="Update", font=("times new roman",10,"bold"), bg="#002b64", fg="#fefcf0", width=10)
        btnUpd.grid(row=0,column=1, padx=5)

        #delete
        btnDel= Button(btn_frame, text="Delete", font=("times new roman",10,"bold"), bg="#002b64", fg="#fefcf0", width=10)
        btnDel.grid(row=0,column=2, padx=5)

        #reset
        btnReset= Button(btn_frame, text="Reset", font=("times new roman",10,"bold"), bg="#002b64", fg="#fefcf0", width=10)
        btnReset.grid(row=0,column=3, padx=5)
    



if __name__ == "__main__":
    root = Tk()
    obj = CustomerWindow(root)
    root.mainloop()

