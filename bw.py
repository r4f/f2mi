import random
import sys
import math

n=2
m=n*n
buttons_state=[0]*m
wires=[[0]*m for j in range(m)]
task=[0]*m

def new_task():
	global wires
	global task
	wires=[[random.randint(0,1) for i in range(m)] for j in range(m)]
#	for i in range(m):
#		print(wires[i])
	solution=[random.randint(0,1) for i in range(m)]
#	print(solution)
#	draw(task)
	for button in range(m):
		if solution[button]:
			for i in range(m):
				task[i]=wires[button][i]!=task[i]
	print("New task:")
	draw(task)
	print("Buttons:")
	draw_buttons()
	print("you:")
	draw(buttons_state)

def draw(vector):
	out='+'+'-'*n+'+\n'
	for i in range(n):
		out=out+'|'
		for j in range(n):
			if vector[i*n+j]:
				out=out+"x"
			else:
				out=out+" "
		out=out+'|\n'
	out=out+'+'+'-'*n+'+'
	print(out)

def draw_buttons():
	o=" "
	p=''
	q=''
	r=''
	for i in range(m):
		o=o+" "*int(math.trunc(0.5*n-0.5))+str(i+1)+" "*int(math.ceil(0.5*n+0.5))
		p=p+'+'+'-'*n
		q=q+'+'+'-'*n
	for i in range(n):
		for j in range(m):
			r=r+'|'
			for k in range(n):
				if wires[j][i*n+k]:
					r=r+'*'
				else:
					r=r+" "
		r=r+'|\n'
	o=o+'\n'
	p=p+'+\n'
	q=q+'+'
	print(o+p+r+q)

def state():
	draw(buttons_state)

def show_task():
	print("task:")
	draw(task)
	print("you:")
	draw(buttons_state)

def press(button):
	for i in range(m):
		buttons_state[i]=wires[button][i]!=buttons_state[i]
	state()

new_task()

goon=True
parsed=False
while goon:
	inp = input("Press button: ")
	for i in range(1,m+1):
		if str(i)==inp:
			press(i-1)
			if buttons_state==task:
				print("Congratulations!")
				new_task()
			parsed=True
	if parsed == False:
		if str(0) == inp:
			show_task()
		elif inp == 'n':
			new_task()
		elif inp == 'b':
			draw_buttons()
		elif inp == 'h':
			print("for buttons action, press 1 to "+str(m)+"\nor press 0 to show task,\nor b to see how the buttons behave\nor n for new round\nor x if you don't want to play anymore!")
		elif inp == 'x':
			goon=False
		else:
			print("did not understand")
	parsed=False
