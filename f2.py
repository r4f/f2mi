from tkinter import *
from tkinter import ttk
from math import *
import random

def new_game():
	global lights_goal
	global lights_state
	lights_goal=[0]*m
	lights_state=[0]*m
	tries.set(0)
	successes.set(0)
	new_round()

def new_round():
	global tries
	global wires
	global lights_goal
	wires=[[random.randint(0,1) for _ in range(m)] for _ in range(m)]
	buttons_goal=[random.randint(0,1) for _ in range(m)]
	apply(buttons_goal,lights_goal)
	redraw_goal()
	redraw_buttons()

def apply(buttons_state, output):
	for button in range(m):
		if buttons_state[button]==True:
			for i in range(m):
				output[i]=wires[button][i]!=output[i]

def ok():
	apply(buttons_state, lights_state)
	turnoff_buttons()
	tries.set(int(tries.get())+1)
	redraw_state()
	check()

def check():
	if lights_goal==lights_state:
		successes.set(int(successes.get())+1)
		new_round()

def redraw_goal():
	for i in range(len(lights_goal)):
		y=floor(i/2)
		x=i%2
		if lights_goal[i]==1:
			color="black"
		else:
			color="white"
		lights_goal_c.create_rectangle((x*100, y*100, x*100+100, y*100+100), fill=color)


def redraw_state():
	for i in range(len(lights_state)):
		y=floor(i/2)
		x=i%2
		if lights_state[i]==1:
			color="black"
		else:
			color="white"
		lights_state_c.create_rectangle((x*100, y*100, x*100+100, y*100+100), fill=color)

def redraw_buttons():
	turnoff_buttons()
	for i in range(len(wires)):
		offset=i*110
		for j in range(len(wires[i])):
			x=j%2
			y=floor(j/2)
			if wires[i][j]==1:
				color="black"
			else:
				color="white"
			buttons_c.create_rectangle((x*50+offset, y*50, x*50+50+offset, y*50+50), fill=color)

def turnoff_buttons():
	global buttons_state
	buttons_c.create_rectangle((0, 100, 440, 120), fill="blue")
	buttons_state=[0]*m

def press_button(event):
	global buttons_state
	offset=floor(event.x/110)
	buttons_state[offset]= not buttons_state[offset]
	if buttons_state[offset]:
		color="green"
	else:
		color="blue"
	buttons_c.create_rectangle((offset*110, 100, 100+offset*110, 120), fill=color)

n=2
m=n*n
wires=[[0]*m for j in range(m)]
lights_goal=[0]*m
lights_state=[0]*m
buttons_state=[0]*m

root = Tk()
root.title("F2Mi")

tries = StringVar()
tries.set(0)
successes = StringVar()
successes.set(0)

mainframe = ttk.Frame(root, padding="0 0 0 0")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

tries_label = ttk.Label(mainframe, textvariable=tries)
tries_label.grid(column=0, row=0, sticky=(W, E))
succ_label = ttk.Label(mainframe, textvariable=successes)
succ_label.grid(column=1, row=0, sticky=(W, E))

newgame_button=ttk.Button(mainframe, text="New Game", command=new_game)
newgame_button.grid(column=2, row=0, columnspan=2, sticky=(W, E))

lights_state_c=Canvas(mainframe, background="blue",  width=200, height=200)
lights_state_c.grid(column=0, row=1, columnspan=2, sticky=(W, E, S, N))

lights_goal_c=Canvas(mainframe, background="blue",  width=200, height=200)
lights_goal_c.grid(column=2, row=1, columnspan=2, sticky=(W, E, S, N))

buttons_c=Canvas(mainframe, background="blue",  width=440, height=120)
buttons_c.grid(column=0, row=2, columnspan=4, sticky=(W, E, S, N))
buttons_c.bind("<Button-1>", press_button)

ok_button=ttk.Button(mainframe, text="ok", command=ok)
ok_button.grid(column=0, row=3, columnspan=4, sticky=(W, E))

ok_button.focus()
root.bind('<Return>', ok)

redraw_state()
new_round()
root.mainloop()
