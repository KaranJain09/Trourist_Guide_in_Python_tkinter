from PIL import Image, ImageTk


class ImageUtility:

    def __init__(self):
        pass

    def get_photo_image(self, imagepath,width,height, master):
        bg_image = Image.open(imagepath)
        bg_image = bg_image.resize((width,height), Image.LANCZOS)
        bg_photo = ImageTk.PhotoImage(image=bg_image, master=master)
        return bg_photo
