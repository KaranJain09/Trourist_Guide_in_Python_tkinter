from tkinter import *
import requests
from Utilities import ImageUtility

class Places:
    def __init__(self):
        self.imageUtility = ImageUtility()
        self.root = Tk()
        self.root.geometry("1600x3500")
        self.root.title('Nearby Restaurants')

        photo = self.imageUtility.get_photo_image("images\\building.png", 1550, 850,
                                                  self.root)
        Label(self.root, width=1000, height=800, image=photo, bg="white").pack(fill="both", expand=True)

        frame = Frame(self.root, width=850, height=600, bg="yellow")
        frame.place(x=280, y=30)

        # create a label and an entry field for the location
        my_labelframe = LabelFrame(frame, text="Enter any place in goa and mumbai",bg="yellow")
        my_labelframe.pack(padx=300,pady=10,anchor='w')

        self.location_entry = Entry(my_labelframe, font=("Helvetica", 15),bg="cyan")
        self.location_entry.grid(row=0, column=0, padx=10, pady=10)
        # green color=#29a329
        # create a button to submit the location
        submit_button = Button(my_labelframe, text='Submit', width=15, command=self.submit_location,activebackground="white",activeforeground="blue",bg="white",fg="blue")
        submit_button.grid(row=0, column=1, padx=10)
        #mustard=#FFDB58
        self.my_text = Text(frame, height=30, width=100, wrap=WORD,bg="cyan")
        self.my_text.pack(padx=10, pady=10)

        back = Button(frame, text="Back", width="15", height="2", command=self.go_to_main,cursor="hand2",activebackground="white",activeforeground="blue",bg="white",fg="blue")
        back.pack(padx=85, pady=10,anchor="w")

        # start the main loop
        self.root.mainloop()

    # create a function to get the list of nearby areas
    def get_nearby_areas(self, nearby_place):
        self.my_text.delete(1.0,END)
        # set up the Foursquare API endpoint and parameters
        url = 'https://api.foursquare.com/v3/places/search'
        params = {
            'client_id': 'AWUNXFTOLPEQZCONUVDLLQO5TLLIBJBUQER1KWDRZGAOH2TL',
            'client_secret': 'W3QCCLVU2PZ4QEEZTHU0TQPAMKGSND5H1GMKIKIOWUV4W51J',
            'near': nearby_place,
            'query': 'place',
            'limit': 10
        }
        headers = {
            "accept": "application/json",
            "Authorization": "fsq3MU4z0ijYJq0fYBXRDI7DUHCmceNu32QYeSxgvhj4KoM="
        }
        # Foursquare API
        response = requests.get(url, params=params, headers=headers).json()
        # extract the list of nearby areas from the response
        try:
            nearby_places = response['results']
            for nearby_place in nearby_places:
                self.my_text.insert(END, f"Name:{nearby_place['name']}"
                                         f"\nAddress:{nearby_place['location']['formatted_address']}"
                                         f"\nDistance:{nearby_place['distance'] } meters "
                                         f"\nGeocode:latitude({nearby_place['geocodes']['main']['latitude']}),"
                                         f"longitude({nearby_place['geocodes']['main']['longitude']})\n\n")

                self.my_text.insert(END,"----------------------------------------------------------------------------------------------------")

        except KeyError:
            print('No areas found.')

    def submit_location(self):
        loc = self.location_entry.get()

        # get the list of nearby areas
        self.get_nearby_areas(loc)
        # create a label to display the list of nearby areas

    def go_to_main(self):
        self.root.destroy()


# Places()
