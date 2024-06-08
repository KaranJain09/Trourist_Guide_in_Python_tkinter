import tkinter as tk
from tkinter import ttk

from Utilities import ImageUtility


# Create the main window
class Hotel():
    def __init__(self):
        self.imageUtility = ImageUtility();
        self.root = tk.Tk()
        self.root.title("SKY Tourism Hotel GUI")
        self.root.geometry("1600x1300")

        # Add a button
        button_frame = tk.Frame(self.root, bg="#1E90FF")
        button_frame.pack(side="top", fill='x')
        button = tk.Button(button_frame, text="Home Page ", width=10, bg="#00BFFF", fg="white", font=("Arial", 14),
                           relief="groove",command=self.home_page)
        button.pack(padx=50, pady=10, side="left")

        # Add a label
        label = tk.Label(self.root, text="Hotels and their Location", font=("Arial", 20, "bold"), fg="#1E90FF")
        label.pack(pady=10)

        # Create a frame for the scrollbar and images
        frame = tk.Frame(self.root)
        frame.pack(side="left", fill="y")

        frame = frame

        # Create a canvas for the scrollbar
        canvas = tk.Canvas(frame, width=1500, height=800)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame to hold the images
        image_frame = tk.Frame(canvas)
        canvas.create_window((1200, 500), window=image_frame, anchor="nw")

        # Load the images and display them in the image frame

        images = ["images\\h1.png",
                  "images\\h2.png",
                  "images\\h3.png",
                  "images\\h4.png",
                  "images\\h5.png",
                  "images\\h10.png",
                  "images\\h6.png",
                  "images\\h7.png",
                  "images\\h8.png"]
        labels = [
                  "\nHotel Sahara Star "
                  "\n Mohan Koppikar Road, Teen Hath Naka Flyover, opposite Raheja Garden,"
                  "\n Thane, Maharashtra 40060", "Hotel JW Marriott "
                                                 "\n Nehru Rd, opp. Domestic Airport, Navpada,Greater  Nagar,"
                                                 "\n Vile Parle East, Mumbai, Maharashtra 400099", "Hotel Lightbridge "
                                                                                                   "\n Sahar Airport Road, Andheri - Kurla Rd, near Mumbai International Airport,"
                                                                                                   "\n Andheri East, Mumbai, Maharashtra 400059",
                  "Hotel Lake City "
                  "\n Chhatrapati Shivaji Maharaj Int'l Airport Rd, Ashok Nagar,"
                  "\n  Andheri East, Mumbai, Maharashtra 400099", "Hotel Oberoi "
                                                                  "\n  Oberoi Garden City, International Business Park, Yashodham,"
                                                                  "\n Goregaon, Mumbai, Maharashtra 40006",
                  "Hotel Eastin "
                  "\n  Candolim Beach Rd, Fadtewada, Nerul, Goa 403114", "Hotel Regias "
                                                                         "\n  Near, Baga Beach Tambudki, Arpora, Goa 403518",
                  "Hotel Hard Rock "
                  "\n   Vainguinim Beach, Dona Paula, Panaji, Goa 403004", "Hotel Miramar "
                                                                           "\n  Miramar Cir, Miramar, Panaji, Goa 403001\n"]
        photos = []
        for i in range(len(images)):
            temp_fr = tk.Frame(image_frame)
            temp_fr.pack()
            # image = Image.open(images[i])
            # image = image.resize((700, 300), Image.LANCZOS)
            # self.photo = ImageTk.PhotoImage(image)
            photo = self.imageUtility.get_photo_image(images[i],700,300,self.root)
            photos.append(photo)
            label = tk.Label(temp_fr, image=photo, bg="white", relief="groove")
            label.pack(padx=50, pady=10, side="left", fill="both", expand=True)
            info_label = tk.Label(temp_fr, width=80, text=labels[i], border=0, font=("Arial", 12), fg="#1E90FF",
                                  relief="groove")
            info_label.pack(side="left", fill="both", expand=True)
        # Update the canvas scroll region
        image_frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

        # Run the main loop
        self.root.mainloop()

    def home_page(self):
        self.root.destroy()
# Hotel()
