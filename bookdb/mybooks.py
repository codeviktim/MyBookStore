#!/usr/bin/python
from tkinter import Tk, Button, Label, Scrollbar, Listbox, StringVar,Entry, W,E,N,S,END
from tkinter import ttk
from tkinter import messagebox

root = Tk()

root.title("MyBookStore Application")
root.configure(background="light green")
root.geometry("1000x600")
root.resizable(width=False, height=False)

# title label
title_label = ttk.Label(root, text="Title", background="light green", font=("TkDefaultFont", 16))
title_label.grid(row=0, column=0, sticky=W)
title_text = StringVar()
title_entry = ttk.Entry(root, width=24, textvariable=title_text)
title_entry.grid(row=0, column=1, sticky=W)

# author label
author_label = ttk.Label(root, text="Author", background="light green", font=("TkDefaultFont", 16))
author_label.grid(row=0, column=2, sticky=W)
author_text = StringVar()
author_entry= ttk.Entry(root, width=24,textvariable=author_text)
author_entry.grid(row=0, column=3, sticky=W)

# Isbn label
isbn_label = ttk.Label(root, text="ISBN", background="light green", font=("TkDefaultFont", 14))
isbn_label.grid(row=0, column=4, sticky=W)
isbn_text = StringVar()
isbn_entry = ttk.Entry(root, width=24, textvariable= isbn_text)
isbn_entry.grid(row=0, column=5, sticky=W)

# button
add_button = Button(root, text="Add Book", bg="blue", fg="white",font="helvetica 10 bold", command="")
add_button.grid(row=0, column=6, sticky=W)

# listbox
list_bx = Listbox(root, height=20, width=35, font="helvetica 13", bg="light blue")
list_bx.grid(row=3, column=1, columnspan=14, sticky=W + E, pady=40, padx=15)

# Scroll bar
scroll_bar = Scrollbar(root)
scroll_bar.grid(row=1, column=8, rowspan=14, sticky=W)

list_bx.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_bx.yview)

# Buttons
edit_btn = Button(root, text="Edit Record", bg="purple", fg="white", font="helvetica 10 bold", command="")
edit_btn.grid(row=17, column=4)

view_btn = Button(root, text="View All Records", bg="black", fg="white", font="helvetica 10 bold", command="")
view_btn.grid(row=17, column=1) # sticky=Tk.N

clear_btn = Button(root, text="Clear Screen", bg="maroon", fg="white", font="helvetica 10 bold", command="")
clear_btn.grid(row=17, column=2) # sticky=W

exit_btn = Button(root, text="Close App", bg="blue", fg="white", font="helvetica 10 bold", command="")
exit_btn.grid(row=17, column=3)

root.mainloop()