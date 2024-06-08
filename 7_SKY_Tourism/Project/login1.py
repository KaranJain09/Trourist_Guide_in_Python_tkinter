from tkinter import *
from tkinter import messagebox
import sqlite3
from Utilities import ImageUtility


class Login:
    def __init__(self, pagesFunc):
        self.pagesFunc = pagesFunc
        self.root = Tk()
        self.imageUtility = ImageUtility()
        self.root.title('.....login...')
        self.root.geometry('1600x1000')
        self.root.configure(bg="#fff")
        self.root.resizable(TRUE, TRUE)

        photo = self.imageUtility.get_photo_image("images\\background.png", 1600, 1000,
                                                  self.root)
        self.open_eye = self.imageUtility.get_photo_image("images\\open_eye.png", 25,15,self.root)

        self.close_eye = self.imageUtility.get_photo_image("images\\closed_eye.png", 25, 15, self.root)

        Label(self.root, width=1000, height=800, image=photo, bg="white").pack(fill="both", expand=True)

        frame = Frame(self.root, width=400, height=400, bg="white")
        frame.place(x=580, y=140)

        heading = Label(frame, text='Login In', fg='#57a1f8', bg="White",
                        font=('Microsoft Yauheni UI Light', 23, 'bold'))
        heading.place(x=100, y=5)

        self.email_val = StringVar()
        self.user = Entry(frame, textvariable=self.email_val, width=25, fg='black', border=0, bg='White',
                          font=('Microsoft Yahei UI Light', 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Email Id')
        self.user.bind('<FocusIn>', self.on_user_enter)
        self.user.bind('<FocusOut>', self.on_user_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

        self.password_val = StringVar()
        self.code = Entry(frame, textvariable=self.password_val, width=25, fg='black', border=0, bg='White',font=('Microsoft Yauheni UI Light', 11))
        self.code.place(x=30, y=150)
        self.code.insert(0, 'Password')
        self.code.bind('<FocusIn>', self.on_code_enter)
        self.code.bind('<FocusOut>', self.on_code_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

        #################################################
        Button(frame, width=39, pady=7, text="Login", bg='#57a1f8', fg='white', border=0,
               command=lambda: self.validate_login()).place(x=35, y=204)
        lable = Label(frame, text="don't have an account?", fg='black', bg='white',
                      font=('Microsoft Yahei UI Light', 9))
        lable.place(x=75, y=270)

        sign_up = Button(frame, width=8, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8',
                         command=self.signup)
        sign_up.place(x=215, y=270)

        self.show_password_button = Button(frame, image=self.open_eye, text='Show password',width=35, height=15, command=self.show)
        self.show_password_button.place(x=280, y=147)
        self.root.mainloop()

    def show(self):
        if self.code.cget('show') == '':
            self.code.config(show='*')
            self.show_password_button.config(image=self.close_eye)
        else:
            self.code.config(show='')
            self.show_password_button.config(image=self.open_eye)

    def signup(self):
        self.root.destroy()
        self.pagesFunc.get("signup")()

    def main_page(self):
        self.root.destroy()
        self.pagesFunc.get("home")(self.email_val.get())

    def validate_login(self):
        print(self.email_val.get())
        # check if email field is empty
        if self.email_val.get() == "":
            messagebox.showerror("Error", "Please enter your email.")
            return
        # check if password field is empty
        if self.password_val.get() == "":
            messagebox.showerror("Error", "Please enter your password.")
            return
        # Connect to the SQLite3 database
        conn = sqlite3.connect('signup.db')
        # Create a cursor object
        cursor = conn.cursor()
        # Execute a SELECT query to retrieve the user's credentials from the database based on their email
        cursor.execute('SELECT u_password FROM REGISTER WHERE u_email = ?', (self.email_val.get(),))
        result = cursor.fetchone()

        # If the email is not found in the database
        if not result:
            messagebox.showerror('Error', 'Email is wrong')
            return False

        # Compare the retrieved password with the entered password
        if self.password_val.get() == result[0]:
            messagebox.showinfo('Success', 'Login successful!')
            self.main_page()
            return True
        else:
            messagebox.showerror('Error', ' Password is wrong')
            return False
        # Close the database connection
        conn.close()

        return

    def on_user_enter(self, e):
        self.user.delete(0, 'end')
        return

    def on_user_leave(self, e):
        name = self.user.get()
        if name == "":
            self.user.insert(8, 'Username')
            return
        return

    def on_code_enter(self, e):
        self.code.delete(0, 'end')
        return

    def on_code_leave(self, e):
        name = self.code.get()
        if name == "":
            self.code.insert(8, 'Password')
        return

#Login()
