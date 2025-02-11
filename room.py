from tkinter import *
from tkinter import ttk
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
import tempfile, os

class RoomBooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Room booking")
        self.root.geometry("1330x565+200+220")

        #variables
        self.varRef= StringVar()
        self.varCheckin= StringVar()
        self.varCheckout= StringVar()
        self.varRoomtype= StringVar()
        self.varAvailability= StringVar()
        self.varMeal= StringVar()
        self.varNoofdays= StringVar()
        self.varPaidtax= StringVar()
        self.varActualtotal= StringVar()
        self.varTotal= StringVar()

        #title
        label_title = Label(self.root, text="Room Booking", font=("times new roman",18,"bold"), bg="#002b64", fg="#fefcf0")
        label_title.place(x=0,y=0,width=1330,height=50)

        #label frame
        labelframeleft = LabelFrame(self.root,text="Rooms and Availability",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=7,y=56,width=470,height=497) 

        #labels and entry
        #customer ref
        label_custref= Label(labelframeleft, text="Reference Number ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_custref.grid(row=0,column=0, sticky=W)

        entry_ref= ttk.Entry(labelframeleft, textvariable=self.varRef, width=30,font=("times new roman",12,"bold"))
        entry_ref.grid(row=0,column=1, sticky=W)

        #fetch data button
        btnFetch= Button(labelframeleft, command=self.fetch_ref, text="Fetch", font=("times new roman",8), bg="#002b64", fg="#fefcf0", width=11, relief="flat")
        btnFetch.place(x=348,y=5)

        #checkin
        label_checkin= Label(labelframeleft, text="Check In ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_checkin.grid(row=1,column=0, sticky=W)

        entry_checkin= ttk.Entry(labelframeleft, textvariable=self.varCheckin, width=35,font=("times new roman",12,"bold"))
        entry_checkin.grid(row=1,column=1)

        #checkout
        label_checkout= Label(labelframeleft, text="Check Out", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_checkout.grid(row=2,column=0, sticky=W)

        entry_checkout= ttk.Entry(labelframeleft, textvariable=self.varCheckout, width=35,font=("times new roman",12,"bold"))
        entry_checkout.grid(row=2,column=1) 

        # Room Type
        label_roomtype = Label(labelframeleft, text="Room Type ", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_roomtype.grid(row=3, column=0, sticky=W)

        roomtype_box = ttk.Combobox(labelframeleft, textvariable=self.varRoomtype, font=("times new roman", 12, "bold"), width=33, state="readonly")
        roomtype_box["value"] = ("Single", "Double", "Delux", "Suite")
        roomtype_box.grid(row=3, column=1)
        
        # Bind the combobox to call the update_availroom function on selection change
        roomtype_box.bind("<<ComboboxSelected>>", self.update_availroom)

        # Available Room
        label_availroom = Label(labelframeleft, text="Available Room ", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_availroom.grid(row=4, column=0, sticky=W)

        self.availroom_box = ttk.Combobox(labelframeleft, textvariable=self.varAvailability, font=("times new roman", 12, "bold"), width=33, state="readonly")
        self.availroom_box.grid(row=4, column=1)

        # Database connection for fetching room numbers
        self.conn = mysql.connector.connect(host="localhost", username="root", password="Mysql@19", database="management")
        self.myCursor = self.conn.cursor()

        #meal 
        label_mealtype= Label(labelframeleft, text="Meal ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_mealtype.grid(row=5,column=0, sticky=W)

        mealtype_box= ttk.Combobox(labelframeleft, textvariable=self.varMeal, font=("times new roman",12,"bold"), width=33, state="readonly")
        mealtype_box["value"]=("No", "Breakfast", "Dinner", "Buffet")
        mealtype_box.grid(row=5, column=1)

        #days
        label_days= Label(labelframeleft, text="Number of Days ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_days.grid(row=6,column=0, sticky=W)

        entry_days= ttk.Entry(labelframeleft, textvariable=self.varNoofdays, width=35,font=("times new roman",12,"bold"))
        entry_days.grid(row=6,column=1)

        #tax
        label_tax= Label(labelframeleft, text="Tax Paid ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_tax.grid(row=7,column=0, sticky=W)

        entry_tax= ttk.Entry(labelframeleft, textvariable=self.varPaidtax, width=35,font=("times new roman",12,"bold"))
        entry_tax.grid(row=7,column=1)

        #sub total
        label_subtotal= Label(labelframeleft, text="Sub Total ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_subtotal.grid(row=9,column=0, sticky=W)

        entry_subtotal= ttk.Entry(labelframeleft, textvariable=self.varTotal, width=35,font=("times new roman",12,"bold"))
        entry_subtotal.grid(row=9,column=1)

        #Total cose
        label_totalcost= Label(labelframeleft, text="Total Cost ", font=("times new roman",12,"bold"), padx=2, pady=6)
        label_totalcost.grid(row=10,column=0, sticky=W)

        entry_totalcost= ttk.Entry(labelframeleft, textvariable=self.varActualtotal, width=35,font=("times new roman",12,"bold"))
        entry_totalcost.grid(row=10,column=1)

        btn_billframe= Frame(labelframeleft, bd=2)
        btn_billframe.place(x=0,y=350, width=450,height=40)

        # Bill button
        btnBill = Button(btn_billframe, text="Bill", command=self.total, font=("times new roman", 10, "bold"), bg="#002b64", fg="#fefcf0", width=12)
        btnBill.grid(row=11, column=0, padx=7, sticky=W)

        # Print button
        btnPrint = Button(btn_billframe, text="Print", command=self.print_bill, font=("times new roman", 10, "bold"), bg="#002b64", fg="#fefcf0", width=12)
        btnPrint.grid(row=11, column=1, padx=7, sticky=W)

        #buttons
        btn_frame= Frame(labelframeleft, bd=2)
        btn_frame.place(x=0,y=390, width=450,height=40)

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

        #table frame for system
        tableframe= LabelFrame(self.root,text="View Details and Search System",padx=2,font=("times new roman",12,"bold"))
        tableframe.place(x=485,y=302,width=833,height=250)

        label_search= Label(tableframe, text="Search By ", font=("times new roman",12,"bold"), bg="#002b64", fg="#fefcf0")
        label_search.grid(row=0,column=0, sticky=W)

        self.search_var= StringVar()
        searchbox= ttk.Combobox(tableframe, textvariable=self.search_var, font=("times new roman",12,"bold"), width=27, state="readonly")
        searchbox["value"] = ("ref", "roomtype")

        searchbox.grid(row=0, column=1)

        self.search_txt= StringVar()
        txtsearch= ttk.Entry(tableframe, textvariable=self.search_txt, font=("times new roman",12,"bold"), width=27)
        txtsearch.grid(row=0,column=2, padx=5)

        btnSearch= Button(tableframe, text="Search", command=self.search, font=("times new roman",10,"bold"), bg="#002b64", fg="#fefcf0", width=10)
        btnSearch.grid(row=0,column=3, padx=5)

        btnShowall= Button(tableframe, text="Show All", command=self.fetch_data, font=("times new roman",10,"bold"), bg="#002b64", fg="#fefcf0", width=10)
        btnShowall.grid(row=0,column=4, padx=5)

        #show data table
        details_frame= Frame(tableframe, bd=2, relief= RIDGE)
        details_frame.place(x=0,y=40, width=820,height=180)

        scroll_x= ttk.Scrollbar(details_frame, orient= HORIZONTAL)
        scroll_y= ttk.Scrollbar(details_frame, orient= VERTICAL)

        self.room_datalist = ttk.Treeview(details_frame, column=("ref", "checkin", "checkout", "roomtype", "availability", "meal", "noofdays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_datalist.xview)
        scroll_y.config(command=self.room_datalist.yview)

        self.room_datalist.heading("ref", text="Reference")
        self.room_datalist.heading("checkin", text="Check In")
        self.room_datalist.heading("checkout", text="Check Out")
        self.room_datalist.heading("roomtype", text="Room Type")
        self.room_datalist.heading("availability", text="Room Availability")
        self.room_datalist.heading("meal", text="Meal")
        self.room_datalist.heading("noofdays", text="No of days")


        self.room_datalist["show"] = "headings"
        self.room_datalist.column("ref", width=100)
        self.room_datalist.column("checkin", width=100)
        self.room_datalist.column("checkout", width=100)
        self.room_datalist.column("roomtype", width=100)
        self.room_datalist.column("availability", width=100)
        self.room_datalist.column("meal", width=100)
        self.room_datalist.column("noofdays", width= 100)
        self.room_datalist.pack(fill=BOTH, expand=1)
        self.room_datalist.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def update_availroom(self, event):
        # Get selected room type from the roomtype_box
        type = self.varRoomtype.get()

        # Fetch room numbers based on selected room type
        query = f"SELECT roomno FROM details WHERE type = '{type}'"
        self.myCursor.execute(query)
        dataRows = self.myCursor.fetchall()

        # Extract room numbers from the fetched data
        room_numbers = [row[0] for row in dataRows]

        # Update the available room combobox with the filtered room numbers
        self.availroom_box["value"] = room_numbers
        self.availroom_box.set('')  # Optionally, clear the selection

    def add_data(self):
        if self.varRef.get()=="" or self.varCheckin.get()=="":
            messagebox.showerror("Error", "All Fields Are Required", parent= self.root)
        else:
            try:
                conn= mysql.connector.connect(host= "localhost", username="root", password=" ", database=" ")
                myCursor= conn.cursor()
                myCursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(self.varRef.get(),self.varCheckin.get(),self.varCheckout.get(),self.varRoomtype.get(),self.varAvailability.get(),self.varMeal.get(),self.varNoofdays.get()))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room Booked", parent= self.root)

            except Exception as es:
                messagebox.showerror("Warning", f"Something Went Wrong:{str(es)}", parent= self.root)

    def fetch_data(self):
        conn= mysql.connector.connect(host= "localhost", username="root", password=" ", database=" ")
        myCursor= conn.cursor()
        myCursor.execute("select * from room")
        dataRows= myCursor.fetchall()
        if len(dataRows)!=0:
            self.room_datalist.delete(*self.room_datalist.get_children())
            for i in dataRows:
                self.room_datalist.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursorRow= self.room_datalist.focus()
        content= self.room_datalist.item(cursorRow)
        row= content["values"]

        self.varRef.set(row[0])
        self.varCheckin.set(row[1])
        self.varCheckout.set(row[2])
        self.varRoomtype.set(row[3])
        self.varAvailability.set(row[4])
        self.varMeal.set(row[5])
        self.varNoofdays.set(row[6])

    def update(self):
        if self.varRef.get()=="":
            messagebox.showerror("Error","Please Enter Ref Number", parent= self.root)
        else:
            conn= mysql.connector.connect(host= "localhost", username="root", password=" ", database=" ")
            myCursor= conn.cursor()
            myCursor.execute("update room set checkin=%s, checkout=%s, roomtype=%s, availability=%s, meal=%s, noofdays=%s where ref=%s", (self.varCheckin.get(),self.varCheckout.get(),self.varRoomtype.get(),self.varAvailability.get(),self.varMeal.get(),self.varNoofdays.get(),self.varRef.get()))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "User Updated Successfully", parent= self.root)

    def delete(self):
        delete= messagebox.askyesno("Hotel management system", "Do you want to delete this booking", parent= self.root)
        if delete>0:
            conn= mysql.connector.connect(host= "localhost", username="root", password=" ", database=" ")
            myCursor= conn.cursor()
            query="delete from room where Ref=%s"
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
        self.varCheckin.set("")
        self.varCheckout.set("")
        self.varRoomtype.set("")
        self.varAvailability.set("")
        self.varMeal.set("")
        self.varNoofdays.set("")
        self.varPaidtax("")
        self.varActualtotal("")
        self.varTotal("")

    def search(self):
        conn= mysql.connector.connect(host= "localhost", username="root", password=" ", database=" ")
        myCursor= conn.cursor()
        myCursor.execute("select * from room where " + str(self.search_var.get()) + " LIKE '%" + str(self.search_txt.get()) + "%'")

        rows= myCursor.fetchall()
        if len (rows)!=0:
            self.room_datalist.delete(*self.room_datalist.get_children())
            for i in rows:
                self.room_datalist.insert("", END, values=i)
            
            conn.commit()
        conn.close()

    def fetch_ref(self):
        if self.varRef.get()=="":
            messagebox.showerror("Error","Please Enter Reference Number", parent=self.root)
        else:
            conn= mysql.connector.connect(host= "localhost", username="root", password=" ", database=" ")
            myCursor= conn.cursor()
            query=("select Name from customer where ref=%s")
            value=(self.varRef.get(),)
            myCursor.execute(query, value)
            row= myCursor.fetchone()

            if row== None:
                messagebox.showerror("Error","This Number Does Not Exist", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe= Frame(self.root,padx=2, bd=4, relief=RIDGE)
                showDataframe.place(x=485,y=64,width=829,height=180)
                #name
                labelName= Label(showDataframe, text="Name", font=("times new roman",12,"bold"))
                labelName.place(x=0,y=0)

                label= Label(showDataframe, text=row[0], font=("times new roman",12,"bold"))
                label.place(x=90,y=0)
                #gender
                conn= mysql.connector.connect(host= "localhost", username="root", password=" ", database=" ")
                myCursor= conn.cursor()
                query=("select Gender from customer where ref=%s")
                value=(self.varRef.get(),)
                myCursor.execute(query, value)
                row= myCursor.fetchone()

                labelGender= Label(showDataframe, text="Gender", font=("times new roman",12,"bold"))
                labelGender.place(x=0,y=30)

                label2= Label(showDataframe, text=row[0], font=("times new roman",12,"bold"))
                label2.place(x=90,y=30)

                #contact
                query=("select Ref from customer where ref=%s")
                value=(self.varRef.get(),)
                myCursor.execute(query, value)
                row= myCursor.fetchone()

                labelRef= Label(showDataframe, text="Ref", font=("times new roman",12,"bold"))
                labelRef.place(x=0,y=60)

                label3= Label(showDataframe, text=row[0], font=("times new roman",12,"bold"))
                label3.place(x=90,y=60)

                #email
                query=("select Email from customer where ref=%s")
                value=(self.varRef.get(),)
                myCursor.execute(query, value)
                row= myCursor.fetchone()

                labelEmail= Label(showDataframe, text="Email", font=("times new roman",12,"bold"))
                labelEmail.place(x=0,y=90)

                label4= Label(showDataframe, text=row[0], font=("times new roman",12,"bold"))
                label4.place(x=90,y=90)

                #nationality
                query=("select Nationality from customer where ref=%s")
                value=(self.varRef.get(),)
                myCursor.execute(query, value)
                row= myCursor.fetchone()

                labelNation= Label(showDataframe, text="Nationality", font=("times new roman",12,"bold"))
                labelNation.place(x=0,y=120)

                label5= Label(showDataframe, text=row[0], font=("times new roman",12,"bold"))
                label5.place(x=90,y=120)

                #idproof
                query=("select Idproof from customer where ref=%s")
                value=(self.varRef.get(),)
                myCursor.execute(query, value)
                row= myCursor.fetchone()

                labelId= Label(showDataframe, text="Id Proof", font=("times new roman",12,"bold"))
                labelId.place(x=300,y=0)

                label6= Label(showDataframe, text=row[0], font=("times new roman",12,"bold"))
                label6.place(x=390,y=0)

                #address
                conn= mysql.connector.connect(host= "localhost", username="root", password=" ", database=" ")
                myCursor= conn.cursor()
                query=("select Address from customer where ref=%s")
                value=(self.varRef.get(),)
                myCursor.execute(query, value)
                row= myCursor.fetchone()

                labelAddress= Label(showDataframe, text="Address", font=("times new roman",12,"bold"))
                labelAddress.place(x=300,y=30)

                label7= Label(showDataframe, text=row[0], font=("times new roman",12,"bold"))
                label7.place(x=390,y=30)

    def total(self):
        inDate= self.varCheckin.get()
        outDate= self.varCheckout.get()
        inDate= datetime.strptime(inDate, "%d/%m/%Y")
        outDate= datetime.strptime(outDate, "%d/%m/%Y")
        self.varNoofdays.set(abs(outDate-inDate).days)
    
        # Define prices for room and meal combinations
        room_meal_prices = {
            ("No", "Single"): (0, 1000),
            ("No", "Double"): (0, 1500),
            ("No", "Delux"): (0, 2000),
            ("No", "Suite"): (0, 3000),
            ("Breakfast", "Single"): (300, 1000),
            ("Breakfast", "Double"): (300, 1500),
            ("Breakfast", "Delux"): (300, 2000),
            ("Breakfast", "Suite"): (300, 3000),
            ("Dinner", "Single"): (500, 1000),
            ("Dinner", "Double"): (500, 1500),
            ("Dinner", "Delux"): (500, 2000),
            ("Dinner", "Suite"): (500, 3000),
            ("Buffet", "Single"): (700, 1000),
            ("Buffet", "Double"): (700, 1500),
            ("Buffet", "Delux"): (700, 2000),
            ("Buffet", "Suite"): (700, 3000),
        }

        try:
            # Get user input values
            meal = self.varMeal.get()
            room = self.varRoomtype.get()
            num_days = float(self.varNoofdays.get())  # Number of days

            # Check if the combination exists
            if (meal, room) in room_meal_prices:
                meal_price, room_price = room_meal_prices[(meal, room)]

                # Calculate subtotal, tax, and total
                subtotal = (meal_price + room_price) * num_days
                tax = 0.1 * subtotal  # 10% tax
                total = subtotal + tax

                # Display results
                self.varPaidtax.set(f"Rs. {tax:.2f}")
                self.varTotal.set(f"Rs. {subtotal:.2f}")
                self.varActualtotal.set(f"Rs. {total:.2f}")
            else:
                messagebox.showerror("Error", "Invalid room and meal combination")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def print_bill(self):
        if self.varTotal.get() == "":
            messagebox.showerror("Error", "Bill is empty")
            return

        try:
            # Create temporary file
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
            bill_path = temp_file.name

            # Write bill details to the file
            with open(bill_path, "w") as file:
                file.write("Billing for stay at The Starfish\n")
                file.write("=" * 40 + "\n")
                file.write(f"Reference Number: {self.varRef.get()}\n")
                file.write(f"Check In: {self.varCheckin.get()}\n")
                file.write(f"Check Out: {self.varCheckout.get()}\n")
                file.write(f"Room Type: {self.varRoomtype.get()}\n")
                file.write(f"Available Room: {self.varAvailability.get()}\n")
                file.write(f"Meal Plan: {self.varMeal.get()}\n")
                file.write(f"Number of Days: {self.varNoofdays.get()}\n")
                file.write(f"Tax Paid: {self.varPaidtax.get()}\n")
                file.write(f"Sub Total: {self.varTotal.get()}\n")
                file.write(f"Total Cost: {self.varActualtotal.get()}\n")
                file.write("=" * 40 + "\n")
                file.write("Thank you for staying with us!\n")

            # Print the file
            os.startfile(bill_path, "print")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while printing: {e}")


if __name__ == "__main__":
    root = Tk()
    obj = RoomBooking(root)
    root.mainloop()

