from tkinter import *
from tkinter import ttk
from math import *
import random

def newgame():
	print("new game")
def enter(args):
	print("enter")
def change_state():
	state = [random.randint(0,1) for _ in range(4)]
	for i in range(len(state)):
		x=floor(i/2)
		y=i%2
		if state[i]==1:
			color="black"
		else:
			color="white"
		cv.create_rectangle((x*200, y*200, x*200+200, y*200+200), fill=color)
	tries.set(int(tries.get())+1)
def callback(event):
	offset=floor(event.x/100)
	if buttons_state[offset]:
		buttons_state[offset]=0
		color="blue"
	else:
		buttons_state[offset]=1
		color="green"
	row.create_rectangle((offset*100, 100, 100+offset*100, 120), fill=color)

buttons_state=[0,0,0,0]

root = Tk()
root.title("F2Mi")

mainframe = ttk.Frame(root, padding="0 0 0 0")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

tries = StringVar()
tries.set(00)

tries_label = ttk.Label(mainframe, textvariable=tries)
tries_label.grid(column=0, row=0, columnspan=2, sticky=(W, E))

newgame_button=ttk.Button(mainframe, text="New Game", command=newgame)
newgame_button.grid(column=2, row=0, columnspan=2, sticky=(W, E))
cv=Canvas(mainframe, background="blue",  width=400, height=400)
cv.grid(column=0, row=1, columnspan=4, sticky=(W, E, S, N))

row=Canvas(mainframe, background="blue",  width=400, height=120)
row.grid(column=0, row=2, columnspan=4, sticky=(W, E, S, N))

states = [[0,1,1,0],[1,1,1,0],[0,0,1,0],[0,1,0,1]]
for i in range(len(states)):
	offset=i*100
	for j in range(len(states[i])):
		x=j%2
		y=floor(j/2)
		if states[i][j]==1:
			color="black"
		else:
			color="white"
		row.create_rectangle((x*50+offset, y*50, x*50+50+offset, y*50+50), fill=color)

row.bind("<Button-1>", callback)

ok_button=ttk.Button(mainframe, text="ok", command=change_state)
ok_button.grid(column=0, row=3, columnspan=4, sticky=(W, E))
#for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

newgame_button.focus()
root.bind('<Return>', enter)


root.mainloop()
