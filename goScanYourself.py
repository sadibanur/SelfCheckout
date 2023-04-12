from tkinter import *
from tkmacosx import Button

root = Tk()
root.title("GoScanYourself")
root.geometry("800x700")
root["bg"] = "yellow"

title = Label(root, text="Start Scanning...",font=("Arial", 35, "bold"),bg="yellow")
title.place(x=100, y=20)

def scan():
    item = ["banana","bread","apple","milk","tomato"]
    price = [2.18, 1.98, 3.69, 2.69, 4.49]
    y=150
    j=0
    total = 0
    for i in item:
        label = Label(root,text= i + "             $" + str(price[j]),font=("Arial", 25))
        label.place(x=30, y=y)
        total += price[j]
        y += 80
        j += 1
    total_label = Label(root, text="Total          $" + str(total),font=("Arial", 30))
    total_label.place(x=30,y=580)

barcode = PhotoImage(file="barcode_scan.png")
barcode_button = Button(root,image=barcode,height=220,width=250,command=scan)
barcode_button.place(x=460,y=40)

def lookup_item():
    new = Toplevel(root)
    new.geometry("800x700")
    new["bg"] = "yellow"
    new.title("Find Your Items")
    fruits = Button(new, text="Fruits",font=("Arial",20, "bold"),fg="White", bg="Blue",height=100,width=150)
    fruits.place(x=100, y=100)
    veg = Button(new, text="Vegetables",font=("Arial",20, "bold"),fg="White", bg="Blue",height=100,width=150)
    veg.place(x=300, y=100)
    organic = Button(new, text="Shop \n organic",font=("Arial",20, "bold"),fg="White", bg="Blue",height=100,width=150)
    organic.place(x=500, y=100)
    dairy = Button(new, text="Dairy & \n Eggs",font=("Arial",20, "bold"),fg="White", bg="Blue",height=100,width=150)
    dairy.place(x=100, y=250)
    bread = Button(new, text="Bread & \n Bakery",font=("Arial",20, "bold"),fg="White", bg="Blue",height=100,width=150)
    bread.place(x=300, y=250)
    cereal = Button(new, text="Breakfast & \n Cereal",font=("Arial",20, "bold"),fg="White", bg="Blue",height=100,width=150)
    cereal.place(x=500, y=250)
    coffee = Button(new, text="Coffee & \n Tea",font=("Arial",20, "bold"),fg="White", bg="Blue",height=100,width=150)
    coffee.place(x=100, y=400)
    drink = Button(new, text="Beverages",font=("Arial",20, "bold"),fg="White", bg="Blue",height=100,width=150)
    drink.place(x=300, y=400)
    snack = Button(new, text="Snacks & \n Candy",font=("Arial",20, "bold"),fg="White", bg="Blue",height=100,width=150)
    snack.place(x=500, y=400)
    back = Button(new, text="Back",font=("Arial",20, "bold"),fg="White", bg="Blue",height=80,width=120,command=new.destroy)
    back.place(x=450, y=550)
    next = Button(new, text="Next",font=("Arial",20, "bold"),fg="White", bg="Blue",height=80,width=120)
    next.place(x=600, y=550)

def help():
    new = Toplevel(root)
    new.geometry("300x200")
    new.title("Help")
    message = Label(new, text="Someone will be \n with you soon..",font=("Arial", 20, "bold"))
    message.place(x=50,y=50)
    back = Button(new, text="Back",font=("Arial",11, "bold"),fg="White", bg="Blue",height=45,width=55,command=new.destroy)
    back.place(x=220, y=140)


def pay():
    new = Toplevel(root)
    new.geometry("500x550")
    new.title("Pay")
    new["bg"] = "yellow"
    message = Label(new, text="Choose Payment Method...",font=("Arial", 20, "bold"),bg="yellow")
    message.place(x=50,y=50)
    credit = Button(new, text="Credit Card",font=("Arial",20, "bold"),fg="White", bg="Green",height=100,width=150)
    credit.place(x=80, y=100)
    debit = Button(new, text="Debit Card", font=("Arial", 20, "bold"), fg="White", bg="Green", height=100, width=150)
    debit.place(x=280, y=100)
    debit = Button(new, text="Debit Card", font=("Arial", 20, "bold"), fg="White", bg="Green", height=100, width=150)
    debit.place(x=280, y=100)
    cash = Button(new, text="Cash", font=("Arial", 20, "bold"), fg="White", bg="Green", height=100, width=150)
    cash.place(x=80, y=250)
    check = Button(new, text="Pay by \n Check", font=("Arial", 20, "bold"), fg="White", bg="Green", height=100, width=150)
    check.place(x=280, y=250)
    receipt = Button(new,text="Print / Email Receipt", font=("Arial", 18, "bold"), fg="White", bg="Blue", height=70, width=220)
    receipt.place(x=80, y=380)
    back = Button(new, text="Back",font=("Arial",15, "bold"),fg="White", bg="Blue",height=60,width=70,command=new.destroy)
    back.place(x=320, y=480)
    done = Button(new, text="Done",font=("Arial",15, "bold"),fg="White", bg="Blue",height=60,width=70,command=root.destroy)
    done.place(x=410, y=480)

item = Button(root, text="Look Up Item",font=("Arial",20, "bold"),fg="White", bg="Blue",height=100, width=150,command=lookup_item)
item.place(x=420, y=280)

key = Button(root, text="Enter \n Item Number",font=("Arial",20, "bold"),fg="White", bg="Blue",height=100,width=150)
key.place(x=600, y=280)

help = Button(root, text="Help",font=("Arial",22, "bold"),fg="White", bg="Blue",height=100,width=150,command=help)
help.place(x=420, y=400)

cancel = Button(root, text="Cancel Item",font=("Arial",20, "bold"),fg="White", bg="Blue",height=100,width=150)
cancel.place(x=600, y=400)

pay = Button(root, text="Finish & Pay",font=("Arial",25, "bold"),fg="White", bg="Green",height=100,width=330,command=pay)
pay.place(x=420, y=520)

root.mainloop()
