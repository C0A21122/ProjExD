import tkinter
import maze_maker

def key_down(event):
    global key
    key = event.keysym
    main_proc()

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy
    if key == "Up":     #上が押されたら
        cy -= 20
    elif key == "Down": #下が押されたら
        cy += 20
    elif key == "Left": #左が押されたら
        cx -= 20
    elif key == "Right":#右が押されたら
        cx += 20
    canvas.coords("tori", cx, cy) #座標の更新
    root.after(1000, main_proc)  #リアルタイム処理

if __name__ == "__main__":
    global key
    key = ""
    root = tkinter.Tk()
    root.title("迷えるこうかとん")

    #bindクラス
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    
    #Canvasクラス
    canvas = tkinter.Canvas(root, 
                            width=1500, #幅
                            height=900, #高さ
                            bg="BLACK"  #背景色
                            ) 
    canvas.pack()

    #迷路の生成
    maze = maze_maker.make_maze(15, 9)
    maze_maker.show_maze(canvas, maze)
    
    #PhotoImageクラス
    tori = tkinter.PhotoImage(file = "ex03/fig/3.png")
    cx, cy = 300, 400
    canvas.create_image(cx, #x座標
                        cy, #y座標
                        image=tori, #画像
                        tag = "tori" #タグ
                        )

    root.mainloop()
