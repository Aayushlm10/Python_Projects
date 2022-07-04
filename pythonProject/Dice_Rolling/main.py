import tkinter
#from PIL import Image,ImageTk
import random
root=tkinter.Tk()
root.geometry('700x450')
root.title('DICE ROLLING SIMULATOR')
Blank_line=tkinter.Label(root,text="")
Head_line=tkinter.Label(root,text="ROLL THE DICE!",
    fg="red",
       bg="black",
       font="Helvetica 16 bold italic")
Blank_line.pack()
Head_line.pack()
l1= tkinter.Label(root, text='', font=("times", 200))
def roll():
    num=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(num)}{random.choice(num)}')
    l1.pack()
# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll the Dice', fg='blue', command=roll)
# pack a widget in the parent widget
button.pack( expand=True)
root.mainloop()
