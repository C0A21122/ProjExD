import tkinter
import tkinter.messagebox as tkm
import maze_maker

def key_down(event):
    global key
    key = event.keysym
    main_proc()
    restart()
 
def restart():  #リスタートする関数
    if key == "r":  #Rキーが押されたら
        choose = tkm.askokcancel("メッセージ", "やり直しますか？" )
        #メッセージを表示して、OKボタンが押されたときだけ
        if choose == True:
            m_make()    #迷路をリセットする

def key_up(event):
    global key
    key = ""

def main_proc():
    global mx, my
    if key == "Up" and maze[my-1][mx] ==0:#上が押されたら
        my -= 1
    elif key == "Down"and maze[my+1][mx] ==0: #下が押されたら
        my += 1
    elif key == "Left"and maze[my][mx-1] ==0: #左が押されたら
        mx -= 1
    elif key == "Right"and maze[my][mx+1] ==0:#右が押されたら
        mx += 1
    cx, cy = mx*100+50, my*100+50   #マス目を移動
    canvas.coords("tori", cx, cy) #座標の更新
    root.after(5000, main_proc)  #リアルタイム処理

def m_make():
    global maze
    #迷路の生成
    maze = maze_maker.make_maze(15, 9)
    maze_maker.show_maze(canvas, maze)
   
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
    
    m_make()    #迷路の生成

    #PhotoImageクラス
    tori = tkinter.PhotoImage(file = "ex03/fig/3.png")
    cx, cy = 150, 150
    mx, my = 1, 1
    canvas.create_image(cx, #x座標
                        cy, #y座標
                        image=tori, #画像
                        tag="tori" #タグ 
                        )

    root.mainloop()
