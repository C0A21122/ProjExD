
import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    #tkm.showinfo(txt, f"[{txt}]ボタンが押されました")
    entry.insert(tk.END,txt)

#Tkクラス
if __name__ == "__main__":
    root = tk.Tk()
    root.title("calc")  #タイトル
    #root.geometry("300x500")    #サイズ
    #root.resizable(width = 500,height = 800)

    #ラベルクラス
    """label = tk.Label(root,
                
    )"""

    #ボタンクラス
    r, c = 1, 0
    for i in range(9, -1, -1):
        button = tk.Button(root,
                            text = f"{i}",
                            font = ("Times New Roman", 30),
                            width=4, height=2,
                            )
        button.bind("<1>",button_click)
        button.grid(row = r, column= c) #rowをrに、columnをcに
        c+=1
        if (i - 1) % 3 == 0:
            r += 1
            c = 0

    #Entryクラス
    entry = tk.Entry(root,justify="right", width="10", font=("Times New Roman",40))
    entry.grid(row=0, columnspan=5)

    root.mainloop()