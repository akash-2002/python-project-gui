from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json
import os

def delete():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    v.set(0)
    v1.set(0)
 
def save():
    msg()
    a = e1.get()
    b = e2.get()
    c1 = v.get()
    d = e3.get()
    e = e4.get()
    f = box_5.get()
    g = v1.get()
    print(a)
    print(b)
    print(c1)
    print(d)
    print(e)
    print(f)
    print(g)
    stu={}
    data = {}
    stu['students']=list()
    data['Name'] = a
    data['RollNo'] = b
    data['Gender'] = c1
    data['Address'] = d
    data['PhoneNo'] = e
    data['Batch'] = f
    data['Hostel'] = g
    if os.path.isfile("students.json"):
        with open(r'students.json','r') as f:
            stu=json.load(f)
            stu['students'].append(data)
        with open(r'students.json','w') as f:
            json.dump(stu,f)
    else:
        with open(r'students.json','w') as f:
            stu['students'].append(data)
            json.dump(stu,f)
    newdata()
    delete()
def newdata():
    with open(r'students.json','r') as f:
        tree1=json.load(f)
        print(tree1)
        x=len(tree1["students"])
        print(type(x))
        for i in range(1):
            treeview.insert('', index='end',
               values=(tree1['students'][-1]['RollNo'], tree1['students'][-1]['Name'], tree1['students'][-1]['Gender'], tree1['students'][-1]['Address'], tree1['students'][-1]['PhoneNo'], tree1['students'][-1]['Batch']))

    
def msg():
    messagebox.showinfo("showinfo", "Record has been save")
    
    
root = Tk()
root.geometry("1200x550")
root.title("STUDENT DATABASE")
# Creating Tab control below
tabctrl = ttk.Notebook(root)
tab1 = ttk.Frame(tabctrl)
tabctrl.add(tab1, text='New Student')
tab2 = ttk.Frame(tabctrl)
tabctrl.add(tab2, text='Display')

tabctrl.pack(expand=1, fill="both")



ttk.Label(tab1, text='Enter Your Name :').place(x=80, y=0)
box_1 = StringVar()
e1 = ttk.Entry(tab1, width=75, textvariable=box_1)
e1.place(x=500, y=0)

ttk.Label(tab1, text='Enter Your Roll No. :').place(x=80, y=40)
box_2 = StringVar()
e2 = ttk.Entry(tab1, width=75, textvariable=box_2)
e2.place(x=500, y=40)

# Radiobutton code below
_m = 'Male'
_f = 'Female'
ttk.Label(tab1, text='Choose your Gender :').place(x=80, y=80)
v = StringVar()
ttk.Radiobutton(tab1, text='Male', variable=v, value=_m).place(x=500, y=80)
ttk.Radiobutton(tab1, text='Female', variable=v, value=_f).place(x=895, y=80)
ttk.Label(tab1, text='Choose your Gender :').place(x=80, y=80)

ttk.Label(tab1, text='Address for Correspondence :').place(x=80, y=120)
box_3 = StringVar()
e3 = ttk.Entry(tab1, width=75, textvariable=box_3)
e3.place(x=500, y=120)

ttk.Label(tab1, text='Phone No. :').place(x=80, y=160)
box_4 = StringVar()
e4 = ttk.Entry(tab1, width=75, textvariable=box_4)
e4.place(x=500, y=160)

# Option menu code below
ttk.Label(tab1, text='Your Batch :').place(x=80, y=200)
box_5 = StringVar()
optlist = ['2016', '2017', '2018', '2019', '2020']
box_5.set(optlist[0])
opt = OptionMenu(tab1, box_5, *optlist)
opt.place(x=792, y=200)

# Checkbox code below
ttk.Label(tab1, text='Hostel[Y/N] :').place(x=80, y=240)
v1 = BooleanVar()
c = ttk.Checkbutton(tab1, text='Click if you need Hostel Facility', variable=v1)
c.place(x=770, y=240)


btn1 = ttk.Button(tab1, text='Save', width=15, command=save)
btn1.place(x=300, y=320)
ttk.Button(tab1, text='Clear', width=15, command=delete).place(x=450, y=320)








# Tree view widget below
columns = ('#1', '#2', '#3', '#4', '#5', '#6', '#7')
tree = ttk.Treeview(tab2, columns=columns, height=25)
# Heading
tree.heading('#0', text='S No.')
tree.heading('#1', text='Roll No.')
tree.heading('#2', text='Name')
tree.heading('#3', text='Gender')
tree.heading('#4', text='Address')
tree.heading('#5', text='PhoneNo')
tree.heading('#6', text='Batch')

# Columns
tree.column('#0', stretch=NO, width=0)
tree.column('#1', stretch=NO)
tree.column('#2', stretch=NO)
tree.column('#3', stretch=NO)
tree.column('#4', stretch=NO)
tree.column('#5', stretch=NO)

tree.column('#6', stretch=NO, width=65)

tree.grid(row=2, columnspan=2, sticky='nsew')
treeview = tree

if os.path.isfile("students.json"):
    tree1={}
    with open(r'students.json','r') as f:
        tree1=json.load(f)
        print(tree1)
        x=len(tree1["students"])
        print(type(x))
        for i in range(0,x):
            treeview.insert('', index='end',
               values=(tree1['students'][i]['RollNo'], tree1['students'][i]['Name'], tree1['students'][i]['Gender'], tree1['students'][i]['Address'], tree1['students'][i]['PhoneNo'], tree1['students'][i]['Batch']))


root.mainloop()