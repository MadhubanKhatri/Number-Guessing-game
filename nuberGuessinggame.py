from tkinter import *
from random import randint
root = Tk()
root.geometry("500x300")
root.title("Number Guessing Game")

random_num = randint(1,10)

def guess():
    entry_val = int(num_entry.get())
    try:
        if entry_val>random_num:
            msg["text"] = "Too High"
            msg["fg"] = "red"
        elif entry_val<random_num:
            msg["text"] = "Too Low"
            msg["fg"] = "red"
        else:
            msg["text"] = "Correct"
            msg["fg"] = "green"

    except:
        msg["text"] = "Please enter a number"


heading = Label(root, text="Number Guessing Game", font=("Helvetica", 15, "bold"))
heading.pack()

lbl_intro = Label(root, text="!Guess a number between 1 to 10!")
lbl_intro.pack()

lbl_number = Label(root, text="Guess Number")
lbl_number.pack()

num_entry = Entry(root, font=("lucida", 30, "bold"),border=10, bg="steelblue", fg="white")
num_entry.pack()

cal_btn = Button(root, text="Guess", width=50, height=2, bg="black",font=("lucida", 13, "bold"),
                 fg="white", relief=RIDGE,command=guess)
cal_btn.pack(pady=10)

msg = Label(root,text="", font=("Helvetica", 15,"bold"))
msg.pack()



root.mainloop()