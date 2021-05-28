from tkinter import *
import random
red = "#ad7474"

def color(a,b):
    main[a-2][b]["bg"] = red
    main[a][b-2]["bg"] = red
    main[a+2][b]["bg"] = red
    main[a][b+2]["bg"] = red
    
n = 30
m = 30
a = n//2
b = m//2

root = Tk()
root.resizable(width = False, height = False)
root.title("Лабиринт")

main = [[None for col in range(m)] for row in range(n)]

for row in range(n):
	for col in range(m):
		e = Button(width = 2, height = 1, state = DISABLED, font = "Verdana 6", bg="#A9A9A9")
		e.grid(row = row, column = col)
		main[row][col] = e

for i in range(4):		
    if main[a][b]["bg"] == "ad7474":
        main[a-2][b]["bg"] = "#ffffff"
            
main[a][b]["bg"] = "#ffffff"
color(a,b)

