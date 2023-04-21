
from datetime import date
import tkinter as tk
import os
top = tk.Tk()
top.config(bg='white')

l1= tk.Label(top, text='Tracking my Websites', bg="white")
l1.pack()
# no e1 only e2/l1 to e5/l5
l2 = tk.Label(top, text='URL of company', bg="white")
l2.pack()
e2 = tk.Entry(top, bg="white")
e2.pack(fill=None)

l3 = tk.Label(top, text='Name of company', bg="white")
l3.pack()
e3 = tk.Entry(top, bg="white")
e3.pack()

l4 = tk.Label(top, text='Position of job', bg="white")
l4.pack()
e4 = tk.Entry(top, bg="white")
e4.pack()

l5 = tk.Label(top, text='Location for job', bg="white")
l5.pack()
e5 = tk.Entry(top, bg="white")
e5.pack()

new_field = tk.Label(top, text='other info', bg="white")
new_field.pack()

l6 = tk.Label(top, text='URL for other', bg="white")
l6.pack()
e6 = tk.Entry(top, bg="white")
e6.pack()

l7 = tk.Label(top, text='Name for other', bg="white")
l7.pack()
e7 = tk.Entry(top, bg="white")
e7.pack()

def on_submit():
    dir_path = '/Users/danielhaycraft/Desktop/my_program'
    file_path = os.path.join(dir_path, 'my_file.txt')
    with open(file_path, 'a') as f:
        f.write('\n')
        f.writelines(e2.get()+', ')
        
        e2.delete(0, "end")
        f.writelines(e3.get()+', ')
        
        e3.delete(0, "end")
        f.writelines(e4.get()+', ')
        e4.delete(0, "end")
        f.writelines(e5.get()+', ')
        
        e5.delete(0, "end")
        f.write('other info')
        f.writelines(e6.get()+', ')
        
        e6.delete(0, "end")
        f.writelines(e7.get()+', ' )
        
        e7.delete(0, "end")
        
        c_date = date.today()
        f.write(str(c_date)+', ')


button = tk.Button(top, text="Save", command=on_submit)
button.pack()

top.mainloop()

