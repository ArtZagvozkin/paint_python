#!/usr/bin/python3
#Artem Zagvozkin

from tkinter import *


def canvasMouseDown(event):
    global lastX, lastY, figure
    lastX, lastY = event.x, event.y
    figure = ""


def canvasDraw(event):
    global figure

    if paint.getMode() == 'pen':
        canvas.create_line((lastX, lastY, event.x, event.y), width=paint.getThickness(),
                           fill=paint.getColor())
        canvasMouseDown(event)
    if paint.getMode() == 'line':
        canvas.delete(figure)
        figure = canvas.create_line((lastX, lastY, event.x, event.y), width=paint.getThickness(),
                                        dash=(paint.getDash(), paint.getDash()),
                                    fill=paint.getColor())
    if 'circle' in paint.getMode():
        canvas.delete(figure)

        curX = event.x
        curY = event.y
        sizeX = abs(lastX - event.x)
        sizeY = abs(lastY - event.y)
        if curX < lastX and curY < lastY:
            curX = lastX - sizeX
            curY = lastY - sizeX
            if sizeX < sizeY:
                curX = lastX - sizeY
                curY = lastY - sizeY
        elif curX > lastX and curY < lastY:
            curX = lastX + sizeX
            curY = lastY - sizeX
            if sizeX < sizeY:
                curX = lastX + sizeY
                curY = lastY - sizeY
        elif curX > lastX and curY > lastY:
            curX = lastX + sizeX
            curY = lastY + sizeX
            if sizeX < sizeY:
                curX = lastX + sizeY
                curY = lastY + sizeY
        elif curX < lastX and curY > lastY:
            curX = lastX - sizeX
            curY = lastY + sizeX
            if sizeX < sizeY:
                curX = lastX - sizeY
                curY = lastY + sizeY

        if paint.getMode() == 'circle1':
            figure = canvas.create_oval((lastX, lastY, curX, curY), width=paint.getThickness(),
                                        dash=(paint.getDash(), paint.getDash()),
                                        outline=paint.getColor())
        else:
            figure = canvas.create_oval((lastX, lastY, curX, curY),
                                        fill=paint.getColor(),
                                        outline=paint.getColor())
    if paint.getMode() == 'oval1':
        canvas.delete(figure)
        figure = canvas.create_oval((lastX, lastY, event.x, event.y), width=paint.getThickness(),
                                        dash=(paint.getDash(), paint.getDash()),
                                    outline=paint.getColor())
    if paint.getMode() == 'oval2':
        canvas.delete(figure)
        figure = canvas.create_oval((lastX, lastY, event.x, event.y),
                                    fill=paint.getColor(),
                                    outline=paint.getColor())
    if 'square' in paint.getMode():
        canvas.delete(figure)

        curX = event.x
        curY = event.y
        sizeX = abs(lastX - event.x)
        sizeY = abs(lastY - event.y)

        if curX < lastX and curY < lastY:
            curX = lastX - sizeX
            curY = lastY - sizeX
            if sizeX < sizeY:
                curX = lastX - sizeY
                curY = lastY - sizeY
        elif curX > lastX and curY < lastY:
            curX = lastX + sizeX
            curY = lastY - sizeX
            if sizeX < sizeY:
                curX = lastX + sizeY
                curY = lastY - sizeY
        elif curX > lastX and curY > lastY:
            curX = lastX + sizeX
            curY = lastY + sizeX
            if sizeX < sizeY:
                curX = lastX + sizeY
                curY = lastY + sizeY
        elif curX < lastX and curY > lastY:
            curX = lastX - sizeX
            curY = lastY + sizeX
            if sizeX < sizeY:
                curX = lastX - sizeY
                curY = lastY + sizeY
        if paint.getMode() == 'square1':
            figure = canvas.create_rectangle((lastX, lastY, curX, curY), width=paint.getThickness(),
                                        dash=(paint.getDash(), paint.getDash()),
                                             outline=paint.getColor())
        else:
            figure = canvas.create_rectangle((lastX, lastY, curX, curY),
                                             fill=paint.getColor(),
                                             outline=paint.getColor())
    if paint.getMode() == 'rectangle1':
        canvas.delete(figure)
        figure = canvas.create_rectangle((lastX, lastY, event.x, event.y), width=paint.getThickness(),
                                        dash=(paint.getDash(), paint.getDash()),
                                         outline=paint.getColor())
    if paint.getMode() == 'rectangle2':
        canvas.delete(figure)
        figure = canvas.create_rectangle((lastX, lastY, event.x, event.y),
                                         fill=paint.getColor(),
                                         outline=paint.getColor())


class Paint:
    def __init__(self):
        self.__mode = 'pen'
        self.__color = 'black'
        self.__thickness = 10
        self.__dash = 250

    def setMode(self, inp):
        self.__mode = inp

    def getMode(self):
        return self.__mode

    def setColor(self, inp):
        self.__color = inp

    def getColor(self):
        return self.__color

    def getThickness(self):
        return self.__thickness

    def setThickness(self, value):
        self.__thickness = value

    def getDash(self):
        return self.__dash

    def setDash(self, value):
        self.__dash = value


def set_thick(value):
    paint.setThickness(value)

def set_dash(value):
    paint.setDash(value)

paint = Paint()

main_window = Tk()
main_window.title("Графический редактор")
main_window.geometry('1000x650')
main_window.columnconfigure(1, weight=1)
main_window.rowconfigure(tuple(range(1)), weight=1)

main_menu = Menu(main_window)
main_window.config(menu=main_menu)
main_menu.add_command(label='Open')
main_menu.add_command(label='Save')

# Canvas
canvas = Canvas(main_window, bg='white')
canvas.grid(row=0, column=1, sticky=N + E + S + W, padx=2, pady=2)
canvas.bind("<Button-1>", canvasMouseDown)
canvas.bind("<B1-Motion>", canvasDraw)


# ToolBox
tools = PanedWindow(main_window, width=100)
tools.grid(row=0, column=0, sticky=N + S)

tool_box = PanedWindow(tools, width=100)
tool_box.grid(row=0, column=0, sticky=N)

btnTool = Button(tool_box, borderwidth=0, bd=0, font='Arial 15', text="🖊", command=lambda: paint.setMode('pen'))
btnTool.grid(row=0, column=0, columnspan=2, sticky=W+E)
btnTool = Button(tool_box, borderwidth=0, font='Arial 15', text="/", command=lambda: paint.setMode('line'))
btnTool.grid(row=1, column=0, columnspan=2, sticky=W+E)
btnTool = Button(tool_box, borderwidth=0, font='Arial 15', text="🧺",
                 command=lambda: (canvas.delete("all"), canvas.config(bg=paint.getColor())))
btnTool.grid(row=2, column=0, columnspan=2, sticky=W+E)
btnTool = Button(tool_box, borderwidth=0, font='Arial 15', text="⭘", command=lambda: paint.setMode('circle1'))
btnTool.grid(row=3, column=0, sticky=W+E)
btnTool = Button(tool_box, borderwidth=0, font='Arial 15', text="●", command=lambda: paint.setMode('circle2'))
btnTool.grid(row=3, column=1, sticky=W+E)
btnTool = Button(tool_box, borderwidth=0, font='Arial 15', text="⬭", command=lambda: paint.setMode('oval1'))
btnTool.grid(row=4, column=0, sticky=W+E)
btnTool = Button(tool_box, borderwidth=0, font='Arial 15', text="⬬", command=lambda: paint.setMode('oval2'))
btnTool.grid(row=4, column=1, sticky=W+E)
btnTool = Button(tool_box, borderwidth=0, font='Arial 15', text="□", command=lambda: paint.setMode('square1'))
btnTool.grid(row=5, column=0, sticky=W+E)
btnTool = Button(tool_box, borderwidth=0, font='Arial 15', text="⯀", command=lambda: paint.setMode('square2'))
btnTool.grid(row=5, column=1, sticky=W+E)
btnTool = Button(tool_box, borderwidth=0, font='Arial 15', text="▯", command=lambda: paint.setMode('rectangle1'))
btnTool.grid(row=6, column=0, sticky=W+E)
btnTool = Button(tool_box, borderwidth=0, font='Arial 15', text="▮", command=lambda: paint.setMode('rectangle2'))
btnTool.grid(row=6, column=1, sticky=W+E)


# Gap Box
gap_box = PanedWindow(tools, height=185)
gap_box.grid(row=7, column=0, columnspan=2, rowspan=2, sticky=W+E+N+S)
gap_box.columnconfigure(tuple(range(8)), weight=1)
gap_box.rowconfigure(tuple(range(8)), weight=1)


# Color Box
color_box = PanedWindow(tools)
color_box.grid(row=10, column=0, columnspan=2, sticky=W+E+S)
color_box.columnconfigure(tuple(range(8)), weight=1)
color_box.rowconfigure(tuple(range(8)), weight=1)

btnChangeColor = Button(color_box, bg='white', command=lambda: paint.setColor('white'))
btnChangeColor.grid(row=0, column=0, columnspan=4, sticky=W + E)
btnChangeColor = Button(color_box, bg='black', command=lambda: paint.setColor('black'))
btnChangeColor.grid(row=0, column=4, columnspan=4, sticky=W + E)
btnChangeColor = Button(color_box, bg='Silver', command=lambda: paint.setColor('Silver'))
btnChangeColor.grid(row=1, column=0, columnspan=4, sticky=W + E)
btnChangeColor = Button(color_box, bg='Gray', command=lambda: paint.setColor('Gray'))
btnChangeColor.grid(row=1, column=4, columnspan=4, sticky=W + E)
btnChangeColor = Button(color_box, bg='yellow', command=lambda: paint.setColor('yellow'))
btnChangeColor.grid(row=2, column=0, columnspan=4, sticky=W + E)
btnChangeColor = Button(color_box, bg='orange', command=lambda: paint.setColor('orange'))
btnChangeColor.grid(row=2, column=4, columnspan=4, sticky=W + E)
btnChangeColor = Button(color_box, bg='Lime', command=lambda: paint.setColor('Lime'))
btnChangeColor.grid(row=3, column=0, columnspan=4, sticky=W + E)
btnChangeColor = Button(color_box, bg='Green', command=lambda: paint.setColor('Green'))
btnChangeColor.grid(row=3, column=4, columnspan=4, sticky=W + E)
btnChangeColor = Button(color_box, bg='Teal', command=lambda: paint.setColor('Teal'))
btnChangeColor.grid(row=4, column=0, columnspan=4, sticky=W + E)
btnChangeColor = Button(color_box, bg='Olive', command=lambda: paint.setColor('Olive'))
btnChangeColor.grid(row=4, column=4, columnspan=4, sticky=W + E)
btnChangeColor = Button(color_box, bg='red', command=lambda: paint.setColor('red'))
btnChangeColor.grid(row=5, column=0, columnspan=4, sticky=W + E)
btnChangeColor = Button(color_box, bg='#92000A', command=lambda: paint.setColor('#92000A'))
btnChangeColor.grid(row=5, column=4, columnspan=4, sticky=W + E)
btnChangeColor = Button(color_box, bg='Fuchsia', command=lambda: paint.setColor('Fuchsia'))
btnChangeColor.grid(row=6, column=0, columnspan=4, sticky=W + E)
btnChangeColor = Button(color_box, bg='Purple', command=lambda: paint.setColor('Purple'))
btnChangeColor.grid(row=6, column=4, columnspan=4, sticky=W + E)
btnChangeColor = Button(color_box, bg='Blue', command=lambda: paint.setColor('Blue'))
btnChangeColor.grid(row=7, column=0, columnspan=4, sticky=W + E)
btnChangeColor = Button(color_box, bg='Navy', command=lambda: paint.setColor('Navy'))
btnChangeColor.grid(row=7, column=4, columnspan=4, sticky=W + E)

# Top box
top_box = PanedWindow(main_window, height=25)
top_box.grid(row=0, column=1, columnspan=1, sticky=W + E + N)
top_box.columnconfigure(tuple(range(8)), weight=1)
top_box.rowconfigure(tuple(range(8)), weight=1)

label = Label(top_box, text="Thickness: ")
label.grid(sticky=W)
scale = Scale(top_box, from_=1, to=50, orient=HORIZONTAL, command=set_thick)
scale.grid(row=1, sticky=W)
scale.set(10)

label = Label(top_box, text="Dash: ")
label.grid(column=1, row=0, sticky=W)
scale = Scale(top_box, from_=1, to=250, orient=HORIZONTAL, command=set_dash)
scale.grid(column=1, row=1, sticky=W)
scale.set(250)

main_window.mainloop()
