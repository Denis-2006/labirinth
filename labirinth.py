from tkinter import *
import random
import time

red = "#ad7474"
white = "#ffffff"
grey = "#A9A9A9"
one = ()
def color(n, m):
    global red
    global white
    global grey
    for a in range(3, n-4):
        for b in range(3, m-4):
            if main[a][b]["bg"]== white:
                if main[a-2][b]["bg"] == grey:
                    main[a-2][b]["bg"] = red
                if main[a+2][b]["bg"] == grey:
                    main[a+2][b]["bg"] = red
                if main[a][b+2]["bg"] == grey:
                    main[a][b+2]["bg"] = red
                if main[a][b-2]["bg"] == grey:
                    main[a][b-2]["bg"] = red


def clearr(n, m):#если будут касяки заменить
    global red
    global white
    global grey
    for a in range(n):
        for b in range(m):
            if main[a][b]["bg"] == white:
                if main[a+1][b]["bg"] == red:
                    main[a+1][b]["bg"] = grey
                if main[a-1][b]["bg"] == red:
                    main[a-1][b]["bg"] = grey
                if main[a][b+1]["bg"] == red:
                    main[a][b+1]["bg"] = grey
                if main[a][b-1]["bg"] == red:
                    main[a][b-1]["bg"] = grey
                    
                if main[a+1][b+1]["bg"] == red:
                    main[a+1][b+1]["bg"] = grey
                if main[a-1][b+1]["bg"] == red:
                    main[a-1][b+1]["bg"] = grey
                if main[a+1][b-1]["bg"] == red:
                    main[a+1][b-1]["bg"] = grey
                if main[a-1][b-1]["bg"] == red:
                    main[a-1][b-1]["bg"] = grey
            
    for a in range(n):
        for b in range(m):
            if main[a][b]["bg"] == red:
                if main[a][b-1]["bg"] != grey and main[a][b+1]["bg"] != grey and main[a][b-1]["bg"] != main[a][b+1]["bg"] or main[a-1][b]["bg"] != grey and main[a+1][b]["bg"] != grey and main[a-1][b]["bg"] != main[a+1][b]["bg"] or main[a-1][b]["bg"] == white and main[a+1][b]["bg"] == white:
                    main[a][b]["bg"] = grey
def clearrr(n, m):#если будут касяки заменить
    global red
    global white
    global grey
    for a in range(n):
        for b in range(m):
            if main[a][b]["bg"] == red:
                main[a][b]["bg"] = grey
                
def rand(n,m):
    global red
    global white
    global grey
    temp = []
    for a in range(n):
        for b in range (m):
            if main[a][b]["bg"] == red:
                temp.append((a,b))
    return temp[random.randrange(len(temp))]
            
def contrand(one):
    global red
    global white
    global grey
    if main[one[0]][one[1] + 2]["bg"]== white:
        return (one[0], one[1] + 2)
    elif main[one[0]][one[1] - 2]["bg"] == white:
        return (one[0], one[1] - 2)
    elif main[one[0] + 2][one[1]]["bg"] == white:
        return (one[0] + 2 , one[1])
    elif main[one[0] - 2][one[1]]["bg"] == white:
        return (one[0] - 2 , one[1])
    else:
        return "None"
    
def picture(one, two):
    global red
    global white
    global grey
    if one[0] == two[0]:
        if one[1] < two[1]:
            main[one[0]][one[1]]["bg"] = white
            main[one[0]][one[1] + 1]["bg"] = white
            main[one[0]][one[1] + 2]["bg"] = white
        else:
            main[two[0]][two[1]]["bg"] = white
            main[two[0]][two[1] + 1]["bg"] = white
            main[two[0]][two[1] + 2]["bg"] = white
    else:
        if one[0] < two[0]:
            main[one[0]][one[1]]["bg"] = white
            main[one[0] + 1][one[1]]["bg"] = white
            main[one[0] + 1][one[1]]["bg"] = white
        else:
            main[two[0]][two[1]]["bg"] = white
            main[two[0] + 1][two[1]]["bg"] = white
            main[two[0] + 1][two[1]]["bg"] = white


def mainn(n, m):
    rrr = rand(n,m)
    picture(rrr, contrand(rrr))
    clearrr(n, m)
    color(n, m)
    clearr(n, m)
    root.after(1, mainn, n, m)

n = 30
m = 30

root = Tk()
root.resizable(width = False, height = False)
root.title("Лабиринт")

main = [[None for col in range(m)] for row in range(n)]

for row in range(n):
	for col in range(m):
		e = Button(width = 2, height = 1, state = DISABLED, font = "Verdana 6", bg="#A9A9A9")
		e.grid(row = row, column = col)
		main[row][col] = e
x, y = n//2, m//2
main[x][y]["bg"] = white
color(n, m)
root.after(1000, mainn, n, m)
#main[x + 12][y]["bg"] = "#ffffff"

root.mainloop()

