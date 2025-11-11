btn_frame = Frame(root, bd=6, relief=GROOVE, bg="#f7f3e9")
btn_frame.place(x=20, y=550, width=850, height=50)

Button(btn_frame, text="Total", font=("Bahnschrift", 12, "bold"),
       bg="#5cb85c", fg="white", width=12, command=calculate_total).grid(row=0, column=0, padx=20, pady=6)
Button(btn_frame, text="Reset", font=("Bahnschrift", 12, "bold"),
       bg="#f0ad4e", fg="white", width=12, command=reset).grid(row=0, column=1, padx=20)
Button(btn_frame, text="Exit", font=("Bahnschrift", 12, "bold"),
       bg="#d9534f", fg="white", width=12, command=exit_app).grid(row=0, column=2, padx=20)

root.mainloop()