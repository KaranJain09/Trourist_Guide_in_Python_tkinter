from tkinter import *
from actual_nearby_places import Places
from newaboutus import Aboutus
from newguihotel import Hotel
from profile import Profile


class Home:
    def __init__(self, pagesFunc, email):
        self.pagesFunc = pagesFunc
        self.email = email
        self.root = Tk()
        root = self.root
        root.geometry("1600x3000")
        root.title("Mini Project")

        f2 = Frame(root, borderwidth=50, bg="lightblue")
        f2.pack(side=TOP, fill="x")
        self.f3 = Frame(root, borderwidth=10, bg="black")
        self.f3.pack(side=LEFT, anchor="nw")

        menu_space = 120
        places = self.get_button(text="Place", command=self.placecall)
        places.pack(side="left", padx=menu_space)
        hotels = self.get_button(text="Hotel", command=self.hotelcall)
        hotels.pack(side="left", padx=menu_space)
        about = self.get_button(text="About", command=self.aboutcall)
        about.pack(side="left", padx=menu_space)
        profile = self.get_button(text="Profile", command=self.profile)
        profile.pack(side="left", padx=menu_space)
        home = self.get_button(text="Logout", command=self.logout)
        home.pack(side="left", padx=menu_space)

        l = Label(f2, text="SKY TOURISM", bg="lightblue", font=("TIMES", 35), fg="#41729F")
        l.pack()

        canvas = Canvas(root, width=1000, height=800, bg="white")
        # scroll_y = Scrollbar(root, orient="vertical", command=canvas.yview)
        # scroll_y.pack(side=LEFT, fill=Y)
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.pack(expand=YES)

        img = PhotoImage(file="images\\newgoa1.png")
        Label(root, image=img, width=400, height=250).place(x=250, y=240)
        l = Label(canvas, text="Famous Places to visit in Mumbai& Goa")
        l.config(font=("Courier", 20))
        l.place(x=300, y=400)

        Label(root, text="3)Gateway Of India", bg="cyan", fg="black", font=10).place(x=1100, y=508)
        Label(root, text="3)Kesarwal Spring Waterfall", bg="cyan", fg="black", font=10).place(x=1100, y=215)
        Label(root, text="2)Marine Drive", bg="cyan", fg="black", font=10).place(x=680, y=508)
        Label(root, text="2)Angoda Beach", bg="cyan", fg="black", font=10).place(x=680, y=215)
        Label(root, text="1)Sanjay Gandhi National Park", bg="cyan", fg="black", font=10).place(x=250, y=508)
        Label(root, text="1)City Lake Beach", bg="cyan", fg="black", font=10).place(x=250, y=215)
        Label(root, text="Famous places\n in Goa", bg="cyan", fg="black", font=10).place(x=60, y=350)
        Label(root, text="Famous places\n in Mumbai", bg="cyan", fg="black", font=10).place(x=60, y=650)
        img1 = PhotoImage(file="images\\newgoa2.png")
        img2 = PhotoImage(file="images\\newgoa3.png")
        img3 = PhotoImage(file="images\\newmum3.png")
        img4 = PhotoImage(file="images\\newmum2.png")
        img5 = PhotoImage(file="images\\newmum1.png")
        Label(root, image=img1, width=400, height=250).place(x=680, y=240)
        Label(root, image=img2, width=400, height=250).place(x=1100, y=240)
        Label(root, image=img3, width=400, height=250).place(x=250, y=532)
        Label(root, image=img4, width=400, height=250).place(x=680, y=532)
        Label(root, image=img5, width=400, height=250).place(x=1100, y=532)

        root.mainloop()

    def profile(self):
        Profile(self.email)

    def logout(self):
        self.root.destroy()
        self.pagesFunc.get("landing")()

    def hotelcall(self):
        hotel = Hotel()

    def placecall(self):
        place = Places()

    def aboutcall(self):
        about = Aboutus()

    def get_button(self, text, command):
        return Button(self.f3, font=10, bg="black", border=0, fg="skyblue", cursor="hand2", text=text, command=command)

