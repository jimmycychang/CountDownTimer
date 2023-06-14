from tkinter import *
from tkinter import messagebox
from base64 import b64decode
from os import remove

root = Tk()
root.title("Countdown")
root.geometry("350x100")

ico = b'AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAMMOAADDDgAAAAAAAAAAAAD//////////////////////////////////////////////////////////////////////////////////////////////////////Pv7/3p6d/9WVlH/KSwh/y0uJv9CQT3/QD87/0tMRf9dXFf/fn57//////////////////////////////////39/f+WlpH/AAAA/yQAVv8IACH/ISIb/yEiHP8JAhP/AAAA/5iXlP///////////////////////////////////////////wAAAP9CC4n/KABf/3d+cP8FAA3/RwqY/wIAIf/N0Mr/////////////////////////////////kJGP/wYMAP8PACX/PgqC/zUIb/8AAAD/AwAH/ygHVf8PADT/kpWO/////////////////////////////////wAAAP82BXb/EgIn/z0Kfv8/CHH/RAl8/z0Lg/9CCXb/JQBW/1xhV/////////////////////////////P28P8AABP/NAps/xUDLP9BCXj/BhW4/wAYx/8AGMn/ABjL/ykDe/8sMCP////////////////////////////y9e//AAAU/zMKav8ZAyv/JBCe/wAYx/8AF8T/ARjI/wAYyv8QDa3/FxcH///////////////////////////////9/wAACv81CWj/GwIo/xEUtv8AGdD/ABGn/wAGcv8AC5X/AAq7/0NBMP////////////////////////////////8AAAT/JA+K/x0CJP8HGM3/AAp3/w8JAP9DOx7/PzcY/w4LAP8NDhH/////////////////////////////////AAAA/wAAVv8eAR//ABne/wACFP9/c1D/rpx0/6qYbf+tnHH/EAsA/+zt7v///////////////////////////////v+np5r/AAAA/wAZ4/8AAAD/1sCI///1zv/////////z/wAAAP///////////////////////////////////////////wAAAP8IFtX/AApy/wICB/85Mhj/QTsu/wAAAP+rrK7///////////////////////////////////////////9zcmf/AABM/wAX5v8AFub/AA7f/wAANP83Ni///////////////////////////////////////////////////////1FQRP8HBwf/AgEA/xcUA/+CgXn/////////////////////////////////////////////////////////////////////////////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=='
icodata = b64decode(ico)
tempfile = "temp.ico"
iconfile = open(tempfile, "wb")
iconfile.write(icodata)
iconfile.close()
root.iconbitmap(tempfile)

def add_1():
    global btn2_1
    try:
        if int(e1.get()) >= 0:
            btn2_1["state"] = NORMAL
        a = int(e1.get())+1
        e1.delete(0, END)
        e1.insert(0, a)
    except ValueError:
        e1.insert(0,0)
def add_2():
    global btn2_2
    try:
        if int(e2.get()) >= 0:
            btn2_2["state"] = NORMAL
        a = int(e2.get())+1
        e2.delete(0, END)
        e2.insert(0, a)
    except ValueError:
        e2.insert(0,0)
def add_3():
    global btn2_3
    try:
        if int(e3.get()) >= 0:
            btn2_3["state"] = NORMAL
        a = int(e3.get())+1
        e3.delete(0, END)
        e3.insert(0, a)
    except ValueError:
        e3.insert(0,0)
def sub_1():
    global btn2_1
    try:
        if int(e1.get()) >= 1:
            b = int(e1.get())-1
            e1.delete(0, END)
            e1.insert(0, b)
            btn2_1["state"] = NORMAL      
        elif int(e1.get()) == 0:
            btn2_1["state"] = DISABLED
    except ValueError:
        e1.insert(0,0)
def sub_2():
    global btn2_2
    try:
        if int(e2.get()) >= 1:
            b = int(e2.get())-1
            e2.delete(0, END)
            e2.insert(0, b)
            btn2_2["state"] = NORMAL
        elif int(e2.get()) == 0:
            btn2_2["state"] = DISABLED
    except ValueError:
        e2.insert(0,0)
def sub_3():
    global btn2_3
    try:
        if int(e3.get()) >= 1:
            b = int(e3.get())-1
            e3.delete(0, END)
            e3.insert(0, b)
            btn2_3["state"] = NORMAL        
        elif int(e3.get()) == 0:
            btn2_3["state"] = DISABLED
    except ValueError:
        e3.insert(0,0)

def countdown():
    global angle, count, canvas_arc, top, angle_del, canvas, canvas_arc, time_now
    try:
        top = Toplevel()
        icodata = b64decode(ico)
        tempfile = "temp.ico"
        iconfile = open(tempfile, "wb")
        iconfile.write(icodata)
        iconfile.close()
        top.iconbitmap(tempfile)
        canvas = Canvas(top, width=350, height=350, bg="white")
        canvas_arc = canvas.create_oval(0,0,350,350, fill="grey", outline="black")
        canvas.create_oval(50,50,300,300, fill="lightgrey", outline="black")
        canvas.pack()
        angle = 360
        count = int(e1.get())*3600+int(e2.get())*60+int(e3.get())
        angle_del = 360/(count)        
        btn["state"] = DISABLED
        btn2 = Button(top, text="Exit", command=top.destroy)
        btn2.pack(fill="both")
        remove(tempfile)
        update()
    except ValueError:
        top.destroy()
        messagebox.showerror("Error", "Wrong number!!")
        remove(tempfile)
    except ZeroDivisionError:
        top.destroy()
        messagebox.showerror("Error", "Please enter number!!")
        remove(tempfile)

def update():
    global angle, count, canvas_arc, top, angle_del, canvas, canvas_arc, time_now
    try:
        if angle == 360:
            angle -= angle_del
        else:
            canvas.delete(canvas_arc)
            canvas_arc = canvas.create_arc(0,0,350,350,start=90,extent=angle,fill="grey",outline="black")
            angle -= angle_del
            count -= 1
            mins_raw, secs = divmod(count, 60)
            hours, mins = divmod(mins_raw, 60)
            time_now = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
            canvas.create_oval(50,50,300,300,fill="lightgrey",outline="black")
            canvas.create_text(175,175,text=time_now, font=("Ink Free", 40, "bold"), fill="black")            
        if count == 0:
            messagebox.showinfo("Time's up", "Time's up!!")
            top.destroy()
            btn["state"] = NORMAL
        else:
            root.after(1000,update)
    except Exception:
        btn["state"] = NORMAL
        top.destroy()

frame = Frame(root)
frame.pack()

btn = Button(root, text="Countdown", command=countdown, bg='lightblue')
btn.pack(fill="both")

e1 = Entry(frame, width=3, font=("Arial", 35), justify="center")
e1.grid(row=0, column=0, rowspan=2)
btn1 = Button(frame, text="▲", width=2, height=1, command=add_1)
btn1.grid(row=0, column=1)
btn2_1 = Button(frame, text="▼", width=2, height=1, state=DISABLED, command=sub_1)
btn2_1.grid(row=1, column=1)

e2 = Entry(frame, width=3, font=("Arial", 35), justify="center")
e2.grid(row=0, column=2, rowspan=2)
btn1_2 = Button(frame, text="▲", width=2, height=1, command=add_2)
btn1_2.grid(row=0, column=3)
btn2_2 = Button(frame, text="▼", width=2, height=1, state=DISABLED, command=sub_2)
btn2_2.grid(row=1, column=3)

e3 = Entry(frame, width=3, font=("Arial", 35), justify="center")
e3.grid(row=0, column=4, rowspan=2)
btn1_3 = Button(frame, text="▲", width=2, height=1, command=add_3)
btn1_3.grid(row=0, column=5)
btn2_3 = Button(frame, text="▼", width=2, height=1, state=DISABLED, command=sub_3)
btn2_3.grid(row=1, column=5)


remove(tempfile)


root.mainloop()

