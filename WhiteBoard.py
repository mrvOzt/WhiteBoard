from tkinter import*
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk


def locate_xy(work):
    global current_x,current_y
    current_x = work.x
    current_y = work.y

def addLine(work):
    global current_x,current_y
    canvas.create_line((current_x,current_y,work.x,work.y),width=get_current_value(),fill=color,capstyle=ROUND,smooth = TRUE)
    current_x,current_y = work.x,work.y

def show_color(new_color):
    global color
    color = new_color

def new_canvas():
    canvas.delete('all')
    display_palette()


def display_palette():
    id = colors.create_rectangle((10,10,30,30),fill = "black")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('black'))

    id = colors.create_rectangle((10,40,30,60),fill = "gray")
    colors.tag_bind(id,"<Button-1>",lambda x: show_color('gray')),

    id = colors.create_rectangle((10,70,30,90),fill = "brown")
    colors.tag_bind(id,"<Button-1>",lambda x: show_color('brown'))

    id = colors.create_rectangle((10,100,30,120),fill = "red")
    colors.tag_bind(id,"<Button-1>",lambda x: show_color('red'))

    id = colors.create_rectangle((10,130,30,150),fill = "orange")
    colors.tag_bind(id,"<Button-1>",lambda x: show_color('orange'))

    id = colors.create_rectangle((10,160,30,180),fill = "yellow")
    colors.tag_bind(id,"<Button-1>",lambda x: show_color('yellow'))

    id = colors.create_rectangle((10,190,30,210),fill = "green")
    colors.tag_bind(id,"<Button-1>",lambda x: show_color('green'))

    id = colors.create_rectangle((10,220,30,240),fill = "blue")
    colors.tag_bind(id,"<Button-1>",lambda x: show_color('blue'))

    id = colors.create_rectangle((10,250,30,270),fill = "purple")
    colors.tag_bind(id,"<Button-1>",lambda x: show_color('purple'))


root = Tk()
root.title("White Board")
root.geometry("850x570+150+50")
root.configure(bg = "#f2f3f5")
root.resizable(False,False)

current_x = 0
current_y = 0
color = "black"

icon_image = PhotoImage(file = "icon.png")
root.iconphoto(False,icon_image)
color_box = PhotoImage(file= "minus.png")
Label(root,image = color_box , bg = "#f2f3f5").place(x = 10, y = 20)

eraser = PhotoImage(file = "eraser.png")
Button(root,image = eraser,bg = "#f2f3f5",command=new_canvas ,width=28,height=30).place(x = 20,y = 440)

colors= Canvas(root,bg ="#ffffff",width=35,height=300,bd = 0)
colors.place(x = 20, y= 70)



display_palette()

canvas = Canvas(root,width =930,height=500,background="white",cursor="hand2")
canvas.place(x = 100,y=10)

canvas.bind('<Button-1>',locate_xy)
canvas.bind('<B1-Motion>',addLine)

##### pen scale ####
def get_current_value():
    return '{:.2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())

current_value = tk.DoubleVar()

slider = ttk.Scale(root,from_ = 0,to = 100,orient = "horizontal",command = slider_changed,variable = current_value)
slider.place(x = 30,y = 530)

value_label = ttk.Label(root,text = get_current_value())
value_label.place(x = 27,y =550)

root.mainloop()
