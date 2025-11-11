from tkinter import *

root = Tk()
root.title("Restaurant Bill Generator")
root.geometry("800x600")
root.configure(bg="white")


headingLabel = Label(root, text="Restaurant Billing System",
                     font=('times new roman', 20, 'bold'),
                     bg="gray20", fg="gold",
                     bd=12, relief=RIDGE)
headingLabel.pack(fill=X, pady=10)

menu = {
    "Paneer Tikka": 180,
    "Veg Biryani": 220,
    "Butter Naan": 40,
    "Cold Drink": 60,
    "French Fries": 100,
    "Gulab Jamun": 80
}
qty_vars = {item: IntVar(value=0) for item in menu}

menuFrame = Frame(root, bd=8, relief=RIDGE, bg="white")
menuFrame.place(x=20, y=100, width=350, height=400)

menuTitle = Label(menuFrame, text="Menu",
                  font=('times new roman', 18, 'bold'),
                  bg="gray20", fg="gold",
                  bd=6, relief=RIDGE)
menuTitle.pack(fill=X)


for i, (item, price) in enumerate(menu.items()):
    Label(menuFrame, text=f"{item} (₹{price})",
          font=('times new roman', 13),
          bg="white", anchor="w").place(x=20, y=50 + i*50)
    Entry(menuFrame, textvariable=qty_vars[item], width=5,
          font=('times new roman', 13),
          bd=2, relief=RIDGE, justify=CENTER).place(x=250, y=50 + i*50)


billFrame = Frame(root, bd=8, relief=RIDGE, bg="white")
billFrame.place(x=400, y=100, width=380, height=400)

billTitle = Label(billFrame, text="Bill Area",
                  font=('times new roman', 18, 'bold'),
                  bg="gray20", fg="gold",
                  bd=6, relief=RIDGE)
billTitle.pack(fill=X)

billArea = Text(billFrame, font=('Courier New', 12),
                bg="white", fg="black")
billArea.pack(fill=BOTH, expand=True)


def calculate_total():
    total = 0
    billArea.delete(1.0, END)
    billArea.insert(END, "\t   Radhey's Restaurant\n")
    billArea.insert(END, "------------------------------------\n")
    billArea.insert(END, f"{'Item':<15}{'Qty':<10}{'Price'}\n")
    billArea.insert(END, "------------------------------------\n")

    for item, price in menu.items():
        qty = qty_vars[item].get()
        if qty > 0:
            amt = qty * price
            total += amt
            billArea.insert(END, f"{item:<15}{qty:<10}{amt}\n")

    tax = round(total * 0.05, 2)
    final = total + tax

    billArea.insert(END, "------------------------------------\n")
    billArea.insert(END, f"Subtotal: ₹{total}\n")
    billArea.insert(END, f"Tax (5%): ₹{tax}\n")
    billArea.insert(END, f"Total: ₹{final}\n")
    billArea.insert(END, "------------------------------------\n")
    billArea.insert(END, "THANK YOU FOR VISITING!")

def reset():
    for var in qty_vars.values():
        var.set(0)
    billArea.delete(1.0, END)

def exit_app():
    root.destroy()

btnFrame = Frame(root, bd=8, relief=RIDGE, bg="white")
btnFrame.place(x=100, y=520, width=600, height=60)

Button(btnFrame, text="Subtotal", font=('times new roman', 14, 'bold'),
       bg="lightblue", fg="black", width=10,
       command=calculate_total).grid(row=0, column=0, padx=20)

Button(btnFrame, text="Reset", font=('times new roman', 14, 'bold'),
       bg="orange", fg="black", width=10,
       command=reset).grid(row=0, column=1, padx=20)

Button(btnFrame, text="Exit", font=('times new roman', 14, 'bold'),
       bg="red", fg="black", width=10,
       command=exit_app).grid(row=0, column=2, padx=20)


root.mainloop()
