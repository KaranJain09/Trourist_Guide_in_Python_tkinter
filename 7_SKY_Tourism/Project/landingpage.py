from tkinter import *
from sign_up1 import Signup
from login1 import Login
from Utilities import ImageUtility
from home import Home


# function to redirect to signin page

class Landing:
    def __init__(self):
        self.imageUtility = ImageUtility();
        # create tkinter window
        self.root = Tk()

        # set window size and title
        self.root.geometry("1600x1000")
        self.root.title("Landing Page")

        # load background image
        bg_photo = self.imageUtility.get_photo_image("images\\background.png", 1600,
                                                     1000, self.root)
        # create background label
        bg_label = Label(self.root, image=bg_photo)
        bg_label.place(x=0, y=0)

        # load signin button image
        signin_photo = self.imageUtility.get_photo_image('images\\LoginInupdate.png', 130, 65,
                                                         self.root)

        # create signin button
        signin_button = Button(self.root,bg="black",image=signin_photo, command=self.signin)
        signin_button.place(x=1234, y=10)

        # load signup button image
        signup_photo = self.imageUtility.get_photo_image("images\\SIGNUPP.png", 130, 65,
                                                         self.root)

        # create signup button
        signup_button = Button(self.root,bg="black",image=signup_photo, command=self.signup)
        signup_button.place(x=1380, y=10)

        # Label(self.root)
        heading = Label(self.root, text="Sky Tourism",width=10,height=2, fg="black", bg="cyan",
                        font=('Microsoft Yahei UI Light', 23, 'bold'))
        heading.place(x=650, y=5)

        self.root.mainloop()

    def signin(self):
        self.root.destroy()
        homeLambdaExp = lambda email: Home({"landing": lambda: Landing()}, email)
        Login({"signup": lambda: Signup({"landing": lambda: Landing()}), "home": homeLambdaExp})

    def signup(self):
        self.root.destroy()
        Signup({"landing": lambda: Landing()})


land = Landing()
