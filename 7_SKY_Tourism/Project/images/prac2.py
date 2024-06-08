from tkinter import *
top = Tk()

top.title("seit")
c = Canvas(top,bg="blue",height=1000,width=1000)
fnt=('times','22','bold italic underline')
text =c.create_text(250,40,text="Canvas app",font=fnt,fill='red',activefill='cyan3')
line=c.create_line(80,80,200,80,200,200,width = 6,fill='cyan3')
line=c.create_line(80,80,300,80,300,300,width = 6,fill='cyan3')
oval = c.create_oval(120,120,400,300,width=6,fill="red",outline="green",activefill="cyan3")
poly=c.create_polygon(320,320,320,420,420,320,width = 6,fill='yellow',outline="green",activefill="cyan3")
rect=c.create_rectangle(360,460,550,550,width=6,fill='green',outline='green',activefill='cyan3')
arc=c.create_arc(500,100,600,300,start=0,extent=180,width=6,outline='green',style='arc')
file1=PhotoImage(file="login.png",height=300,width=300)
file2=PhotoImage(file="signup.png",height=300,width=300)
id=c.create_image(300,400,anchor=NE,image=file1,activeimage=file2)
c.pack()
top.mainloop()
