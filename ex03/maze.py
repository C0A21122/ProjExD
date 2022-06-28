import tkinter
from turtle import bgcolor



if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("迷えるこうかとん")
    

    canvas = tkinter.Canvas(root, width=1500, height=900, bg="BLACK")
    canvas.pack()

    root.mainloop()