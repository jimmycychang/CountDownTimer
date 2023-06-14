from tkinter import *
from tkinter import messagebox
from base64 import b64decode
from os import remove
from sys import exit

root = Tk()
root.title("Countdown")
root.geometry("250x50")


ico = b'AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAMMOAADDDgAAAAAAAAAAAAD//////////////////////////////////////////////////////////////////////////////////////////////////////Pv7/3p6d/9WVlH/KSwh/y0uJv9CQT3/QD87/0tMRf9dXFf/fn57//////////////////////////////////39/f+WlpH/AAAA/yQAVv8IACH/ISIb/yEiHP8JAhP/AAAA/5iXlP///////////////////////////////////////////wAAAP9CC4n/KABf/3d+cP8FAA3/RwqY/wIAIf/N0Mr/////////////////////////////////kJGP/wYMAP8PACX/PgqC/zUIb/8AAAD/AwAH/ygHVf8PADT/kpWO/////////////////////////////////wAAAP82BXb/EgIn/z0Kfv8/CHH/RAl8/z0Lg/9CCXb/JQBW/1xhV/////////////////////////////P28P8AABP/NAps/xUDLP9BCXj/BhW4/wAYx/8AGMn/ABjL/ykDe/8sMCP////////////////////////////y9e//AAAU/zMKav8ZAyv/JBCe/wAYx/8AF8T/ARjI/wAYyv8QDa3/FxcH///////////////////////////////9/wAACv81CWj/GwIo/xEUtv8AGdD/ABGn/wAGcv8AC5X/AAq7/0NBMP////////////////////////////////8AAAT/JA+K/x0CJP8HGM3/AAp3/w8JAP9DOx7/PzcY/w4LAP8NDhH/////////////////////////////////AAAA/wAAVv8eAR//ABne/wACFP9/c1D/rpx0/6qYbf+tnHH/EAsA/+zt7v///////////////////////////////v+np5r/AAAA/wAZ4/8AAAD/1sCI///1zv/////////z/wAAAP///////////////////////////////////////////wAAAP8IFtX/AApy/wICB/85Mhj/QTsu/wAAAP+rrK7///////////////////////////////////////////9zcmf/AABM/wAX5v8AFub/AA7f/wAANP83Ni///////////////////////////////////////////////////////1FQRP8HBwf/AgEA/xcUA/+CgXn/////////////////////////////////////////////////////////////////////////////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=='
icodata = b64decode(ico)
tempfile = "temp.ico"
iconfile = open(tempfile, "wb")
iconfile.write(icodata)
iconfile.close()

root.iconbitmap(tempfile)


def countdown():
    global angle, count, canvas_arc, top, angle_del, canvas, canvas_arc
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
        count = int(e.get())
        angle_del = 360/count
        btn2 = Button(top, text="Exit", command=exit)
        btn2.pack(fill="both")
        remove(tempfile)
        update()

    except ValueError:
        top.destroy()
        messagebox.showerror("Error", "Wrong number!!")
        remove(tempfile)



def update():
    global angle, count, canvas_arc, top, angle_del, canvas, canvas_arc
    btn["state"] = DISABLED

    if angle == 360:
        angle -= angle_del
    else:
        canvas.delete(canvas_arc)
        canvas_arc = canvas.create_arc(0,0,350,350,start=90,extent=angle,fill="grey",outline="black")
        angle -= angle_del
        count -= 1
        canvas.create_oval(50,50,300,300,fill="lightgrey",outline="black")
        canvas.create_text(175,175,text=count, font=("Ink Free", 64, "bold"), fill="black")
    if count == 0:
        messagebox.showinfo("Time's up", "Time's up!!")
        top.destroy()
        btn["state"] = NORMAL
    else:
        root.after(1000,update)
    



e = Entry(root)
e.insert(0, "Enter time here...")
e.pack(fill="both")
btn = Button(root, text="Countdown", command=countdown, bg='lightblue')
btn.pack(fill="both")

remove(tempfile)


root.mainloop()

