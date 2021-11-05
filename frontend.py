from tkinter import *
from tkinter.font import names
from backend import library

database = library()


def view_books():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

## Function for Search the book
def btn_search():
    list1.delete(0,END)
    for row in database.search(title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get()):
        list1.insert(END,row)

def btn_addbook():
    database.insert(title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get()))

# get select
def get_selected_book(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])



## function update
def btn_update():
    database.update(selected_tuple[0],title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get())


## function delete
def btn_delete():
    database.delete(selected_tuple[0])




window = Tk()
window.title('My Books manager')






l1 = Label(window,text="Title")
l1.grid(row = 0, column=0)

l2 = Label(window,text="Author")
l2.grid(row = 0, column=2)

l3 = Label(window,text="Year")
l3.grid(row = 1, column=0)

l4 = Label(window,text="ISBN")
l4.grid(row = 1, column=2)

title_text = StringVar()
e1 = Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

Author_text = StringVar()
e2 = Entry(window,textvariable=Author_text)
e2.grid(row=0,column=3)

Year_text = StringVar()
e3 = Entry(window,textvariable=Year_text)
e3.grid(row=1,column=1) 

ISBN_text = StringVar()
e4 = Entry(window,textvariable=ISBN_text)
e4.grid(row=1,column=3)

list1 = Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_book)

b1= Button(window,text="View all", width=12,command = view_books)
b1.grid(row=2,column=3)

b2= Button(window,text="search", width=12,command=btn_search)
b2.grid(row=3,column=3)

b3= Button(window,text="add book", width=12,command=btn_addbook)
b3.grid(row=4,column=3)

b4= Button(window,text="update all", width=12,command=btn_update)
b4.grid(row=5,column=3)

b5= Button(window,text="delete", width=12,command=btn_delete)
b5.grid(row=6,column=3)

b6= Button(window,text="close", width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()