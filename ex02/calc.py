
import tkinter as tk
import tkinter.messagebox as tkm

#ボタンの処理
def button_click(event):
    btn = event.widget
    txt = btn["text"]
    #tkm.showinfo(txt, f"[{txt}]ボタンが押されました")
    if txt == "=":
        A1 = entry.get()
        result = eval(A1)
        entry.delete(0,tk.END)
        entry.insert(tk.END,result)
    else:
        entry.insert(tk.END,txt)

#Tkクラス
if __name__ == "__main__":
    root = tk.Tk()
    root.title("calc")  #タイトル
    #root.geometry("300x500")    #サイズ
    #root.resizable(width = 500,height = 800)

    #ボタンクラス
    r, c = 1, 0
    for i in range(9, -1, -1):
        button = tk.Button(root,        #0~9までのボタンを作成
                            text = f"{i}",
                            font = ("Times New Roman", 30),
                            width=4, height=2,
                            )
        button.bind("<1>",button_click)
        button.grid(row = r, column= c) #rowをrに、columnをcに
        c+=1
        if (i - 1) % 3 == 0:            #ボタンの配列
            r += 1
            c = 0
    button = tk.Button(root, text="+", font=("Times New Roman",30), width=4, height=2)  #"+"ボタンの作成
    button.grid(row=r, column=c)        #空いた位置に作成
    button.bind("<1>",button_click)     #"+"のクリック処理
    button = tk.Button(root, text="=", font=("Times New Roman",30), width=4, height=2)  #"="ボタンの作成
    button.grid(row=r, column=c+1)      #"+"の隣に作成
    button.bind("<1>",button_click)     #"="のクリック処理



    #Entryクラス
    entry = tk.Entry(root,justify="right", width="10", font=("Times New Roman",40))
    entry.grid(row=0, columnspan=5)

    root.mainloop()