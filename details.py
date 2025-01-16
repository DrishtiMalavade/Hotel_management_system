from tkinter import *
from tkinter import ttk
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Details:
    def __init__(self, root):
        self.root = root
        self.root.title("Room details")
        self.root.geometry("1330x565+200+220")

        # Initialize StringVar variables
        self.varFloor = StringVar()
        self.varType = StringVar()
        self.varRoomno = StringVar()

        # Title
        label_title = Label(self.root, text="Room Details", font=("times new roman", 18, "bold"), bg="#002b64", fg="#fefcf0")
        label_title.place(x=0, y=0, width=1330, height=50)

        # Label Frame
        labelframeleft = LabelFrame(self.root, text="Search and Add Rooms", padx=2, font=("times new roman", 12, "bold"))
        labelframeleft.place(x=7, y=56, width=470, height=497)

        # Floor
        label_floor = Label(labelframeleft, text="Floor ", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_floor.grid(row=1, column=0, sticky=W)

        entry_floor = ttk.Entry(labelframeleft, textvariable=self.varFloor, width=39, font=("times new roman", 12, "bold"))
        entry_floor.grid(row=1, column=1)

        # Room Type
        label_roomtype= Label(labelframeleft, text="Room Type ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_roomtype.grid(row=2,column=0, sticky=W)

        roomtype_box= ttk.Combobox(labelframeleft, textvariable=self.varType, font=("times new roman",12,"bold"), width=37, state="readonly")
        roomtype_box["value"]=("Single", "Double", "Delux", "Suite")
        roomtype_box.grid(row=2, column=1)

        # Room Number
        label_roomno = Label(labelframeleft, text="Room Number ", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_roomno.grid(row=3, column=0, sticky=W)

        entry_roomno = ttk.Entry(labelframeleft, textvariable=self.varRoomno, width=39, font=("times new roman", 12, "bold"))
        entry_roomno.grid(row=3, column=1)

        #buttons
        btn_frame= Frame(labelframeleft, bd=2)
        btn_frame.place(x=0,y=150, width=450,height=40)

        #add entry
        btnAdd= Button(btn_frame, text="Add", command=self.add_data, font=("times new roman",10,"bold"), bg="#002b64", fg="#fefcf0", width=12)
        btnAdd.grid(row=0,column=0, padx=7)

        #update
        btnUpd= Button(btn_frame, text="Update", command=self.update, font=("times new roman",10,"bold"), bg="#002b64", fg="#fefcf0", width=12)
        btnUpd.grid(row=0,column=1, padx=7)

        #delete
        btnDel= Button(btn_frame, text="Delete", command=self.delete, font=("times new roman",10,"bold"), bg="#002b64", fg="#fefcf0", width=12)
        btnDel.grid(row=0,column=2, padx=7)

        #reset
        btnReset= Button(btn_frame, text="Reset", command=self.reset, font=("times new roman",10,"bold"), bg="#002b64", fg="#fefcf0", width=12)
        btnReset.grid(row=0,column=3, padx=7)
    
        #table frame for search
        tableframe= LabelFrame(self.root,text="Room Numbers And Availability",padx=2,font=("times new roman",12,"bold"))
        tableframe.place(x=482,y=56,width=840,height=497)

        label_search= Label(tableframe, text="Search By ", font=("times new roman",12,"bold"), bg="#002b64", fg="#fefcf0")
        label_search.grid(row=0,column=0, sticky=W)

        self.search_var= StringVar()
        searchbox= ttk.Combobox(tableframe, textvariable=self.search_var, font=("times new roman",12,"bold"), width=32, state="readonly")
        searchbox["value"] = ("floor", "roomno", "roomtype")

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

        self.room_details = ttk.Treeview(details_frame, column=("floor", "roomtype", "roomno"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_details.xview)
        scroll_y.config(command=self.room_details.yview)

        self.room_details.heading("floor", text="Floor")
        self.room_details.heading("roomtype", text="Room Type")
        self.room_details.heading("roomno", text="Room No")

        self.room_details["show"] = "headings"
        self.room_details.column("floor", width= 100)
        self.room_details.column("roomtype", width=100)
        self.room_details.column("roomno", width=100)
        
        self.room_details.pack(fill=BOTH, expand=1)
        self.room_details.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()
      
    def get_cursor(self, event=""):
        cursorRow= self.room_details.focus()
        content= self.room_details.item(cursorRow)
        row= content["values"]

        self.varFloor.set(row[0])
        self.varType.set(row[1])
        self.varRoomno.set(row[2])

    def search(self):
        conn= mysql.connector.connect(host= "localhost", username="root", password=" ", database=" ")
        myCursor= conn.cursor()
        myCursor.execute("select * from details where " + str(self.search_var.get()) + " LIKE '%" + str(self.search_txt.get()) + "%'")

        rows= myCursor.fetchall()
        if len (rows)!=0:
            self.room_details.delete(*self.room_details.get_children())
            for i in rows:
                self.room_details.insert("", END, values=i)
            
            conn.commit()
        conn.close()

    def add_data(self):
        if self.varFloor.get().strip() == "" or self.varRoomno.get().strip() == "": 
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
            return

        else:
            try:
                conn= mysql.connector.connect(host= "localhost", username="root", password=" ", database=" ") #your mysql password here
                myCursor= conn.cursor()
                myCursor.execute("insert into details values(%s,%s,%s)",(self.varFloor.get(),self.varType.get(),self.varRoomno.get()))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room Has Been Added", parent= self.root)

            except Exception as es:
                messagebox.showerror("Warning", f"Something Went Wrong:{str(es)}", parent= self.root)

    def update(self):
        if self.varRoomno.get()=="" or self.varFloor.get()=="":
            messagebox.showerror("Error","Please Enter All Details", parent= self.root)
        else:
            conn= mysql.connector.connect(host= "localhost", username="root", password=" ", database=" ") #your mysql password here
            myCursor= conn.cursor()
            myCursor.execute("update details set floor=%s, type=%s, roomno=%s", (self.varFloor.get(),self.varType.get(),self.varRoomno.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Room Details Updated Successfully", parent= self.root)

    def delete(self):
        delete= messagebox.askyesno("Hotel management system", "Do you want to delete this room detail", parent= self.root)
        if delete>0:
            conn= mysql.connector.connect(host= "localhost", username="root", password=" ", database=" ")
            myCursor= conn.cursor()
            query="delete from details where roomno=%s"
            value=(self.varRoomno.get(),)
            myCursor.execute(query,value)
            #myCursor.execute("")    
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.varFloor.set("")
        self.varType.set("")
        self.varRoomno.set("")
 
    def fetch_data(self):
            conn= mysql.connector.connect(host= "localhost", username="root", password=" ", database=" ") #your rmysql password here
            myCursor= conn.cursor()
            myCursor.execute("select * from details")
            dataRows= myCursor.fetchall()
            if len(dataRows)!=0:
                self.room_details.delete(*self.room_details.get_children())
                for i in dataRows:
                    self.room_details.insert("", END, values=i)
                conn.commit()
            conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = Details(root)
    root.mainloop()
