import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont
from Utilities import ImageUtility


# Create a main window

class Aboutus():
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Sky Tourism")
        self.root.geometry("600x700")
        self.root.configure(bg="#F2F2F2")
        self.imageUtility = ImageUtility()


        # Define custom fonts
        font_title = tkFont.Font(family="Montserrat", size=24, weight="bold")
        font_subtitle = tkFont.Font(family="Open Sans", size=16)
        font_button = tkFont.Font(family="Montserrat", size=14)

        # Add background image
        self.bg_image = self.imageUtility.get_photo_image("images\\logo.png", 25, 15,self.root)
        bg_label = tk.Label(self.root, image=self.bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a frame
        frame = tk.Frame(self.root, bg="white", padx=20, pady=20, bd=5, relief="groove")
        frame.pack(fill="both", expand=True)

        # Add title and subtitle labels
        title_label = tk.Label(frame, text="About Us", font=font_title, fg="white", bg="#4E4CB8", padx=20, pady=10, bd=2, relief="solid")
        subtitle_label = tk.Label(frame, text="Guided Tours to Mumbai and Goa", font=font_subtitle, fg="#696969", bg="white", padx=20, pady=10)
        title_label.pack(fill="x")
        subtitle_label.pack(fill="x")

        # Add image
        self.photo = self.imageUtility.get_photo_image("images\\logo.png", 605,190,self.root)
        image_label = tk.Label(frame, image=self.photo)
        image_label.pack(pady=20)

        # Create a text widget
        text = tk.Text(frame, height=5, width=50, font=font_subtitle, bg="white", padx=10, pady=10, wrap="word", bd=2, relief="solid")
        text.pack(pady=20)
        text.insert(tk.END, "We have been running this organization since 2016. We specialize in providing guided "
                            "places and restaurant which you select  near Mumbai and Goa. We also offer a list of "
                            "recommended hotels which people most visited .")

        # Add button
        button = tk.Button(frame, text="Home Page", font=font_button, command=self.root.destroy, bg="#FCC91C", fg="white", padx=20, pady=10, relief="flat", bd=2, activebackground="#FCC91C", activeforeground="white")
        button.pack(pady=20)

        # Add shadow effects to title and subtitle labels
        title_label.config(highlightbackground="#666666", highlightthickness=2)
        subtitle_label.config(highlightbackground="#666666", highlightthickness=2)

        # Start the main loop
        self.root.mainloop()
# Abt = Aboutus()

