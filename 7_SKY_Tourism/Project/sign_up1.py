from tkinter import *
from tkinter import messagebox
import re
from home import Home
from signupdb import Database
from login1 import Login
from Utilities import ImageUtility
from datetime import date


class Signup:
    def __init__(self, pagesFunc):
        self.pagesFunc = pagesFunc
        self.top = Tk()
        self.top.geometry("1600x1300")
        self.top.configure(bg='white')
        self.imageUtility = ImageUtility()
        self.top.grid_rowconfigure(2, weight=2)

        bgimage_path = "images\\bigblue.png"

        img = PhotoImage(file=bgimage_path)

        self.open_eye = self.imageUtility.get_photo_image("images\\open_eye.png", 25, 15,
                                                  self.top)
        self.close_eye = self.imageUtility.get_photo_image("images\\closed_eye.png",25,15,self.top)

        fr = Frame(self.top, pady=100, bg="white", width=100, padx=100)
        label = Label(fr, image=img, width=1200, pady=0, height=800)
        label.place(x=-400, y=-100)
        fr.pack()


        Label(fr, text="Registration form", font="times 20 bold", bg="white", anchor="s").grid(row=0, column=0,
                                                                                               rowspan=1,
                                                                                               columnspan=2, pady=50,
                                                                                               sticky="s")
        name = Label(fr, text="Name:", font="times 14", anchor="e")
        name.grid(row=1, column=0, sticky="e")
        email = Label(fr, text="Email I'd:", font="times 14", anchor="e", fg="black")
        email.grid(row=2, column=0, sticky="e")
        dob = Label(fr, text="Date Of Birth:", font="times 14", anchor="e", fg="black")
        dob.grid(row=3, column=0, sticky="e")
        gender = Label(fr, text="Gender:", font="times 14", anchor="e", fg="black")
        gender.grid(row=4, column=0, sticky="e")
        phone = Label(fr, text="Phone No:", font="times 14", anchor="e", fg="black")
        phone.grid(row=5, column=0, sticky="e")
        password = Label(fr, text="Password:", font="times 14", anchor="e", fg="black")
        password.grid(row=6, column=0, sticky="e")

        self.name_val = StringVar()
        self.email_val = StringVar()
        self.dob_val = StringVar()
        self.gender_val = StringVar()
        self.phone_val = StringVar()
        self.password_val = StringVar()

        self.n_entry = Entry(fr, textvariable=self.name_val, border=0, width=40)
        self.n_entry.grid(row=1, column=1, padx=20, pady=20)
        self.e_entry = Entry(fr, textvariable=self.email_val, width=40, border=0)
        self.e_entry.grid(row=2, column=1, padx=20, pady=20)
        self.dob_entry = Entry(fr, textvariable=self.dob_val, width=40, border=0)
        self.dob_entry.grid(row=3, column=1, padx=20, pady=20)
        self.g_entry = Entry(fr, textvariable=self.gender_val, width=40, border=0)
        self.g_entry.grid(row=4, column=1, padx=20, pady=20)
        self.ph_entry = Entry(fr, textvariable=self.phone_val, width=40, border=0)
        self.ph_entry.grid(row=5, column=1, padx=20, pady=20)
        self.p_entry = Entry(fr, textvariable=self.password_val, width=40, border=0, show='*')
        self.p_entry.grid(row=6, column=1, padx=20, pady=20)
        self.show_password_button = Button(fr,image=self.close_eye, text='Show password',height=12, command=self.show)
        self.show_password_button.place(x=342,y=442)


        Button(fr, text="Submit", font="times 14", command=self.validate, bg="#6200EA",
               foreground="white",
               width=20,
               height=2).grid(row=7, column=0,
                              columnspan=2,
                              pady=50)
        sign_up = Button(fr, width=30, height=1, text='Already have an account? Login', border=0, bg='#6200EA', fg='White',
                         font="times 14", command=self.signin)
        sign_up.place(x=30, y=600)

        self.top.mainloop()

    def show(self):
        if self.p_entry.cget('show') == '':
           self.p_entry.config(show='*')
           self.show_password_button.config(image=self.close_eye)
        else:
            self.p_entry.config(show='')
            self.show_password_button.config(image=self.open_eye)

    def home(self,email):
        # self.top.destroy()
        # self.pagesFunc.get("home")(email)
        self.top.destroy()
        landingDictLambdaExp = {"landing": self.pagesFunc.get("landing")}
        homeLambdaExp = lambda email: Home(landingDictLambdaExp, email)
        Login({"signup": lambda: Signup(landingDictLambdaExp), "home": homeLambdaExp})

    def submit_click(self):
        na = self.name_val.get()
        em = self.email_val.get()
        do = self.dob_val.get()
        ge = self.gender_val.get()
        pho = self.phone_val.get()
        pas = self.password_val.get()
        Database().add_user(na, em, do, ge, pho, pas)
        self.n_entry.delete(0, END)
        self.e_entry.delete(0, END)
        self.dob_entry.delete(0, END)
        self.g_entry.delete(0, END)
        self.ph_entry.delete(0, END)
        self.p_entry.delete(0, END)

    def photo(image_file_path):
        return PhotoImage(file=image_file_path)

    ###########Validation of inputs############

    def validate(self):
        name = self.name_val.get()
        email = self.email_val.get()
        dob = self.dob_val.get()
        gender = self.gender_val.get()
        phone = self.phone_val.get()
        password = self.password_val.get()

        def validate_date_of_birth(date_str):
            # Check if date string matches pattern
            pattern = r'^\d{2}-\d{2}-\d{4}$'
            if not re.match(pattern, date_str):
                return False

            # Check if day and month values are valid
            day, month, year = map(int, date_str.split('-'))
            if month < 1 or month > 12:
                return False
            if day < 1 or day > 31:
                return False
            if month in [4, 6, 9, 11] and day > 30:
                return False
            if month == 2:
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    if day > 29:
                        return False
                else:
                    if day > 28:
                        return False

            # Check if date is in the past
            today = date.today()
            dob = date(year, month, day)
            if dob > today:
                return False

            return True

        if not name:
            messagebox.showerror("Error", "Name field cannot be empty.")
            return
        elif not re.match(r"^[A-Za-z\s]+$", name):
            messagebox.showerror("Error", "Name can only contain letters and spaces.")
            return
        if not email:
            messagebox.showerror("Error", "Email field cannot be empty.")
            return
        elif not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            messagebox.showerror("Error", "Invalid email address.")
            return
        if not dob:
            messagebox.showerror("Error", "Date of Birth field cannot be empty.")
            return
        elif not validate_date_of_birth(dob):
            messagebox.showerror("Error", "Invalid DOB")
            return
        if not gender:
            messagebox.showerror("Error", "gender field cannot be empty.")
            return
        elif not re.match(r"^(Male|Female|male|female)$", gender):
            messagebox.showerror("Error", "Invali gender")
            return
        if not phone:
            messagebox.showerror("Error", "Phone no. field cannot be empty.")
            return
        elif not re.match(r"^\d{10}$", phone):
            messagebox.showerror("Error", "Invali Phone no.")
            return
        if not password:
            messagebox.showerror("Error", "Password field cannot be empty.")
            return
        elif not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=!]).{8,}$', password):
            messagebox.showerror("Error", "Invalid Password ,   Password should consist of 8 chacherters ")
            return
        else:
            self.submit_click()
            self.home(email)

    def signin(self):
        self.top.destroy()
        landingDictLambdaExp = {"landing": self.pagesFunc.get("landing")}
        homeLambdaExp = lambda email: Home(landingDictLambdaExp, email)
        Login({"signup": lambda: Signup(landingDictLambdaExp), "home": homeLambdaExp})



# Signup()