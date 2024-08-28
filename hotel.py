from tkinter import *
from PIL import Image, ImageTk
from customer import CustomerWindow
from room import RoomBooking

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("The Starfish")
        self.root.geometry("1550x800+0+0")
        #self.root.configure(bg="#f0f0f0")

        # Header image
        img1 = Image.open(r"C:\Users\Lenovo\Desktop\hotel-management\images\hotelheader.png")
        self.photoimg1 = ImageTk.PhotoImage(img1)

        labelimg1 = Label(self.root, image=self.photoimg1)
        labelimg1.place(x=0, y=0, width=1550, height=190)

        # Logo
        img2 = Image.open(r"C:\Users\Lenovo\Desktop\hotel-management\images\hotellogo.png")
        img2 = img2.resize((200, 200), Image.LANCZOS)  
        self.photoimg2 = ImageTk.PhotoImage(img2)

        labelimg2 = Label(self.root, image=self.photoimg2)
        labelimg2.place(x=0, y=0, width=200, height=200)

        # Main Frame
        mainframe = Frame(self.root, bg="black") # colour for reference
        mainframe.place(x=0, y=190, width=1550, height=610)

        # Menu
        labelmenu = Label(mainframe, text="Menu", font=("times new roman", 20, "bold"), bg="#002b64", fg="#fefcf0")
        labelmenu.place(x=0, y=0, width=200)

        # Buttons Frame
        buttonframe = Frame(mainframe, bg="#002b64")  # Colour for reference
        buttonframe.place(x=0, y=35, width=200, height=610)

        custbtn = Button(buttonframe, text="Customer", command=self.customerdetails, width=12, font=("times new roman", 20, "bold"), bg="#002b64", fg="#fefcf0", bd=0, cursor="hand1")
        custbtn.grid(row=0, column=0, sticky="nsew")

        roombtn = Button(buttonframe, text="Rooms", command=self.roomdetails, width=12, font=("times new roman", 20, "bold"), bg="#002b64", fg="#fefcf0", bd=0, cursor="hand1")
        roombtn.grid(row=1, column=0, sticky="nsew")

        detailsbtn = Button(buttonframe, text="Details", width=12, font=("times new roman", 20, "bold"), bg="#002b64", fg="#fefcf0", bd=0, cursor="hand1")
        detailsbtn.grid(row=2, column=0, sticky="nsew")

        reportbtn = Button(buttonframe, text="Report", width=12, font=("times new roman", 20, "bold"), bg="#002b64", fg="#fefcf0", bd=0, cursor="hand1")
        reportbtn.grid(row=3, column=0, sticky="nsew")

        logoutbtn = Button(buttonframe, text="Logout", width=12, font=("times new roman", 20, "bold"), bg="#002b64", fg="#fefcf0", bd=0, cursor="hand1")
        logoutbtn.grid(row=4, column=0, sticky="nsew")

        # Start image
        img3 = Image.open(r"C:\Users\Lenovo\Desktop\hotel-management\images\right.png")
        img3 = img3.resize((1300, 590), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        labelimg3 = Label(self.root, image=self.photoimg3)
        labelimg3.place(x=200, y=190, width=1300, height=580)

    def customerdetails(self):
        self.new_window = Toplevel(self.root)
        self.app = CustomerWindow(self.new_window)

    def roomdetails(self):
        self.new_window = Toplevel(self.root)
        self.app = RoomBooking(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
