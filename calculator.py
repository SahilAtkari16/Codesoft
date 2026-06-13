from tkinter import *

windows=Tk()
windows.title("CALCULATOR")
windows.geometry("375x475")
windows.config(bg="black")

display=Entry(windows,font="arial 40 bold",width=15,justify=LEFT)
display.pack(side=TOP)
def button_click(num):
    current=display.get()
    display.delete(0,END)
    display.insert(0,str(current)+str(num))
def button_cal(num):
    current=display.get()
    try:
         res=eval(current)
    except:
         res="Error"
    display.delete(0,END)
    display.insert(0,str(res))

but_7=Button(windows,text="7",fg="red",font="arial 20 bold",command =lambda: button_click(7))
but_7.place(x=10,y=170,width=60,height=50)

but_8=Button(windows,text="8",fg="red",font="arial 20 bold",command=lambda: button_click(8))
but_8.place(x=100,y=170,width=60,height=50)

but_9=Button(windows,text="9",fg="red",font="arial 20 bold",command=lambda: button_click(9))
but_9.place(x=190,y=170,width=60,height=50)

but_6=Button(windows,text="6",fg="red",font="arial 20 bold",command=lambda: button_click(6))
but_6.place(x=190,y=240,width=60,height=50)

but_5=Button(windows,text="5",fg="red",font="arial 20 bold",command=lambda: button_click(5))
but_5.place(x=100,y=240,width=60,height=50)

but_4=Button(windows,text="4",fg="red",font="arial 20 bold",command=lambda: button_click(4))
but_4.place(x=10,y=240,width=60,height=50)

but_3=Button(windows,text="3",fg="red",font="arial 20 bold",command=lambda: button_click(3))
but_3.place(x=190,y=310,width=60,height=50)

but_2=Button(windows,text="2",fg="red",font="arial 20 bold",command=lambda: button_click(2))
but_2.place(x=100,y=310,width=60,height=50)

but_1=Button(windows,text="1",fg="red",font="arial 20 bold",command=lambda: button_click(1))
but_1.place(x=10,y=310,width=60,height=50)

but_0=Button(windows,text="0",fg="red",font="arial 20 bold",command=lambda: button_click(0))
but_0.place(x=10,y=380,width=60,height=50)

but_d=Button(windows,text=".",fg="red",font="arial 20 bold",command=lambda: button_click("."))
but_d.place(x=100,y=380,width=60,height=50)

but_e=Button(windows,text="=",fg="red",font="arial 20 bold",command=lambda: button_cal("="))
but_e.place(x=190,y=380,width=60,height=50)

but_add=Button(windows,text="+",fg="red",font="arial 20 bold",command=lambda: button_click("+"))
but_add.place(x=280,y=380,width=60,height=50)

but_sub=Button(windows,text="-",fg="red",font="arial 20 bold",command=lambda: button_click("-"))
but_sub.place(x=280,y=310,width=60,height=50)

but_multi=Button(windows,text="*",fg="red",font="arial 20 bold",command=lambda: button_click("*"))
but_multi.place(x=280,y=240,width=60,height=50)

but_div=Button(windows,text="/",fg="red",font="arial 20 bold",command=lambda: button_click("/"))
but_div.place(x=280,y=170,width=60,height=50)

but_open=Button(windows,text="(",fg="red",font="arial 20 bold",command=lambda: button_click("("))
but_open.place(x=10,y=100,width=60,height=50)

but_close=Button(windows,text=")",fg="red",font="arial 20 bold",command=lambda: button_click(")"))
but_close.place(x=100,y=100,width=60,height=50)

but_per=Button(windows,text="%",fg="red",font="arial 20 bold",command=lambda: button_click("%"))
but_per.place(x=190,y=100,width=60,height=50)

but_allclear=Button(windows,text="AC",fg="red",font="arial 20 bold",command=lambda: display.delete(0,END))
but_allclear.place(x=280,y=100,width=60,height=50)

but_clear=Button(windows,text="x",fg="red",font="arial 20 bold",command=lambda: display.delete(len(display.get())-1,END))
but_clear.place(x=340,y=40,width=30,height=20)

windows.mainloop()