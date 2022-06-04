from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x570")
root.resizable(0,0)
root.title("Calculator")
root.wm_iconbitmap('calculator.ico')

########## Function ##########
def click (event):
	global entr
	text = event.widget.cget("text") 
	print(text)
	
	if text == "C":
	 	entr.set("")
	 	entry.update()

	elif text == "=":
	 	if entr.get().isdigit():
	 		value = int(ent.get())
	 	else:
	 		value = eval(entry.get())

	 	entr.set(value)
	 	entry.update()


	else:
	 	entr.set(entr.get() + text)
	 	entry.update()

########## Entry ##########
entr = StringVar()
entr.set(" ")
entry = Entry(root, textvariable=entr, bg="black", fg="cyan", font=("DS-Digital", 35), width=200)
entry.pack(side=TOP, fill=X, padx=8, pady=10)

########## Buttons ##########
f = Frame(root)

btn = Button(f, text="C", bg="black", fg="cyan", font=("DS-Digital", 35), padx=8)
btn.pack(side=LEFT, padx=15, pady=12)
btn.bind("<Button-1>", click)

btn = Button(f, text="1", bg="black", fg="cyan", font=("DS-Digital", 35), padx=14)
btn.pack(side=LEFT, padx=15, pady=12)
btn.bind("<Button-1>", click)

btn = Button(f, text="2", bg="black", fg="cyan", font=("DS-Digital", 35), padx=8)
btn.pack(side=LEFT, padx=15, pady=12)
btn.bind("<Button-1>", click)

btn = Button(f, text="+", bg="black", fg="cyan", font=("DS-Digital", 35), padx=8)
btn.pack(side=LEFT, padx=15, pady=12)
btn.bind("<Button-1>", click)

f.pack()


f1 = Frame(root)

btn1 = Button(f1, text="3", bg="black", fg="cyan", font=("DS-Digital", 35), padx=8)
btn1.pack(side=LEFT, padx=15, pady=12)
btn1.bind("<Button-1>", click)

btn1 = Button(f1, text="4", bg="black", fg="cyan", font=("DS-Digital", 35), padx=8)
btn1.pack(side=LEFT, padx=15, pady=12)
btn1.bind("<Button-1>", click)

btn1 = Button(f1, text="5", bg="black", fg="cyan", font=("DS-Digital", 35), padx=8)
btn1.pack(side=LEFT, padx=15, pady=12)
btn1.bind("<Button-1>", click)

btn1 = Button(f1, text="-", bg="black", fg="cyan", font=("DS-Digital", 35), padx=8)
btn1.pack(side=LEFT, padx=15, pady=12)
btn1.bind("<Button-1>", click)

f1.pack()

f2 = Frame(root)

btn2 = Button(f2, text="6", bg="black", fg="cyan", font=("DS-Digital", 35), padx=8)
btn2.pack(side=LEFT, padx=15, pady=12)
btn2.bind("<Button-1>", click)

btn2 = Button(f2, text="7", bg="black", fg="cyan", font=("DS-Digital", 35), padx=8)
btn2.pack(side=LEFT, padx=15, pady=12)
btn2.bind("<Button-1>", click)

btn2 = Button(f2, text="8", bg="black", fg="cyan", font=("DS-Digital", 35), padx=8)
btn2.pack(side=LEFT, padx=15, pady=12)
btn2.bind("<Button-1>", click)

btn2 = Button(f2, text="*", bg="black", fg="cyan", font=("DS-Digital", 35), padx=8)
btn2.pack(side=LEFT, padx=15, pady=12)
btn2.bind("<Button-1>", click)

f2.pack()

f3 = Frame(root)

btn3 = Button(f3, text="9", bg="black", fg="cyan", font=("DS-Digital", 35), padx=8)
btn3.pack(side=LEFT, padx=15, pady=12)
btn3.bind("<Button-1>", click)

btn3 = Button(f3, text="0", bg="black", fg="cyan", font=("DS-Digital", 35), padx=8)
btn3.pack(side=LEFT, padx=15, pady=12)
btn3.bind("<Button-1>", click)

btn3 = Button(f3, text=".", bg="black", fg="cyan", font=("DS-Digital", 35), padx=16)
btn3.pack(side=LEFT, padx=15, pady=12)
btn3.bind("<Button-1>", click)

btn3 = Button(f3, text="/", bg="black", fg="cyan", font=("DS-Digital", 35), padx=7)
btn3.pack(side=LEFT, padx=15, pady=12)
btn3.bind("<Button-1>", click)

f3.pack()

f4 = Frame(root)

btn4 = Button(f4, text="**", bg="black", fg="cyan", font=("DS-Digital", 35), padx=5)
btn4.pack(side=LEFT, padx=8, pady=10)
btn4.bind("<Button-1>", click)

btn4 = Button(f4, text="=", bg="black", fg="cyan", font=("DS-Digital", 35), padx=25, width=200)
btn4.pack(side=LEFT, padx=8, pady=10)
btn4.bind("<Button-1>", click)

f4.pack()

def message():
	if messagebox.askyesnocancel("Close", "Do you want to close?"):
		root.destroy()

root.protocol("WM_DELETE_WINDOW",message)

root.mainloop()

