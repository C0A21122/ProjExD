import tkinter

if __name__ == "__main__":
    global key
    key = ""
    root = tkinter.Tk()
    root.title("迷えるこうかとん")
    
    #Canvasクラス
    canvas = tkinter.Canvas(root, 
                            width=1500, #幅
                            height=900, #高さ
                            bg="BLACK"
                            ) #背景色
    
    #PhotoImageクラス
    tori = tkinter.PhotoImage(file = "ex03/fig/3.png")
    cx, cy = 300, 400
    canvas.create_image(cx, #x座標
                        cy, #y座標
                        image=tori #画像
                        )
    canvas.pack()

    root.mainloop()