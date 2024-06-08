# #Import the Tkinter module.
# import tkinter as tk
# #Create the GUI application main window
# root = tk.Tk()
# label = tk.Label(root, text="Welcome to Tkinter!")
# label.pack()
# #Enter the main event loop to take action against each event triggered by the user.
# root.mainloop()


# import tkinter as tk
#
# def on_submit():
#     result_label.config(text="Hello, " + entry.get())
#
# root = tk.Tk()
# entry = tk.Entry(root)
# submit_button = tk.Button(root, text="Submit", command=on_submit)
# result_label = tk.Label(root, text="")
#
# entry.pack()
# submit_button.pack()
# result_label.pack()
#
# root.mainloop()



# import tkinter as tk
#
# def exit_application():
#     root.destroy()
#
# root = tk.Tk()
# exit_button = tk.Button(root, text="Exit", command=exit_application)
# exit_button.pack()
#
# root.mainloop()

# import tkinter as tk
#
# root = tk.Tk()
# python_var = tk.BooleanVar()
# java_var = tk.BooleanVar()
#
# python_checkbox = tk.Checkbutton(root, text="Python", variable=python_var)
# java_checkbox = tk.Checkbutton(root, text="Java", variable=java_var)
#
# python_checkbox.pack()
# java_checkbox.pack()
#
# root.mainloop()


# import tkinter as tk
#
# root = tk.Tk()
# gender_var = tk.StringVar()
#
# male_radio = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
# female_radio = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
#
# male_radio.pack()
# female_radio.pack()
#
# root.mainloop()


# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
# day_var = tk.StringVar()
#
# days_combobox = ttk.Combobox(root, textvariable=day_var, values=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
# days_combobox.pack()
#
# root.mainloop()


# import tkinter
# from tkinter import messagebox
# top = tkinter.Tk()
# def helloCallBack():
# 	messagebox.showinfo( "Hello Python", "Hello World")
# B = tkinter.Button(top, text ="Hello", command = helloCallBack)
# B.pack()
# top.mainloop()



# import tkinter as tk
#
# def draw_circle():
#     canvas.create_oval(50, 50, 150, 150, fill="blue")
#
# def draw_rectangle():
#     canvas.create_rectangle(200, 50, 300, 150, fill="green")
#
# root = tk.Tk()
# canvas = tk.Canvas(root, width=400, height=200)
# canvas.pack()
#
# circle_button = tk.Button(root, text="Draw Circle", command=draw_circle)
# rectangle_button = tk.Button(root, text="Draw Rectangle", command=draw_rectangle)
#
# circle_button.pack()
# rectangle_button.pack()
#
# root.mainloop()





# import tkinter as tk
#
# def on_button_click():
#     label.config(text="Button Clicked!")
#
# # Create the main window
# root = tk.Tk()
# root.title("Frame Example")
#
# # Create a frame with a background color
# frame = tk.Frame(root, padx=20, pady=20, bg="lightblue")
# frame.pack(padx=10, pady=10)
#
# # Create a label and button inside the frame
# label = tk.Label(frame, text="Welcome to Tkinter!", bg="lightblue")
# button = tk.Button(frame, text="Click Me", command=on_button_click)
#
# # Pack the label and button inside the frame
# label.pack(pady=10)
# button.pack()
#
# # Run the main loop
# root.mainloop()





# import tkinter as tk
#
# def on_scale_change(value):
#     label.config(text=f"Selected Value: {value}")
#
# root = tk.Tk()
# scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=on_scale_change)
# scale.pack()
#
# label = tk.Label(root, text="Selected Value: 0")
# label.pack()
#
# root.mainloop()




# import tkinter as tk
#
# def on_spinbox_change():
#     selected_value = spinbox.get()
#     label.config(text=f"Selected Value: {selected_value}")
#
# # Create the main window
# root = tk.Tk()
# root.title("Spinbox Example")
#
# # Create a Spinbox with a range of 0 to 10
# spinbox = tk.Spinbox(root, from_=0, to=10, command=on_spinbox_change)
# spinbox.pack(pady=20)
#
# # Create a label to display the selected value
# label = tk.Label(root, text="Selected Value: 0")
# label.pack()
#
# # Run the main loop
# root.mainloop()




# import tkinter as tk
# from tkinter import scrolledtext
#
# # Create the main window
# root = tk.Tk()
# root.title("Nice Scrollbar Example")
#
# # Create a ScrolledText widget
# text = scrolledtext.ScrolledText(root, wrap="word", width=40, height=10)
# text.pack(padx=10, pady=10)
#
# # Add content to the ScrolledText widget
# text.insert("1.0", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. ")
#
# # Run the main loop
# root.mainloop()
