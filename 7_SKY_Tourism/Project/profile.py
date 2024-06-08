import tkinter as tk
import sqlite3
from tkinter import *
from Utilities import ImageUtility


class Profile:
    def __init__(self, email):
        self.email_val = email
        self.imageUtility = ImageUtility()
        print("email %s", self.email_val)
        conn = sqlite3.connect('signup.db')
        c = conn.cursor()
        # Get user info from the database
        c.execute("SELECT * FROM REGISTER WHERE u_email=?", (self.email_val,))
        user_info = c.fetchone()
        # Close the database connection
        conn.close()
        # Create the profile page
        self.profile = tk.Tk()
        self.profile.title("Profile Page")
        self.profile.geometry("1600x1000")

        photo= self.imageUtility.get_photo_image("images\\profile_bg.png", 1600, 1000,self.profile)
        Label(self.profile, width=1600, height=1000, image=photo, bg="white").grid(row=0,column=0)


        def go_to_main():
            self.profile.destroy()

        # Display user info in labels
        frame=Frame(self.profile, width=650, height=350,bg="cyan")
        frame.place(x=30,y=30)

        ph = self.imageUtility.get_photo_image("images\\profile_pic.png", 100, 100, self.profile)
        Label(frame, width=100, height=100, image=ph, background="cyan").place(x=0, y=0)
        
        Label(frame, text="Name:",font=('Helvetica',18,'bold'), bg="palegreen", fg="black").place(x=140,y=20)
        Label(frame, text=user_info[0] ,font=('Helvetica',18,'italic'), bg="palegreen", fg="black").place(x=300,y=20)
        Label(frame, text="Email:",font=('Helvetica',18,'bold'), bg="palegreen", fg="black").place(x=140,y=60)
        Label(frame, text=user_info[1],font=('Helvetica',18,'italic'), bg="palegreen", fg="black").place(x=300,y=60)
        Label(frame, text="Date of Birth:",font=('Helvetica',18,'bold'), bg="palegreen", fg="black").place(x=140,y=100)
        Label(frame, text=user_info[2],font=('Helvetica',18,'italic'), bg="palegreen", fg="black").place(x=300,y=100)
        Label(frame, text="Gender",font=('Helvetica',18,'bold'), bg="palegreen", fg="black").place(x=140,y=140)
        Label(frame, text=user_info[3],font=('Helvetica',18,'italic'), bg="palegreen", fg="black").place(x=300,y=140)
        Label(frame, text="Phone No.:",font=('Helvetica',18,'bold'), bg="palegreen", fg="black").place(x=140,y=180)
        Label(frame, text=user_info[4],font=('Helvetica',18,'italic'), bg="palegreen", fg="black").place(x=300,y=180)
        back = Button(frame, text="Back",font=('Helvetica',15,'bold'), bg="palegreen", fg="black", width="10", command=go_to_main)
        back.place(x=20,y=260)


        self.profile.mainloop()
