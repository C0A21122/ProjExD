
import tkinter as tk
import tkinter.messagebox as tkm

from setuptools import Command

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"[{txt}]ボタンが押されました")

#Tkクラス
root = tk.Tk()
root.title("calc")  #タイトル
root.geometry("300x500")    #サイズ
root.resizable(width = 500,height = 800)

#ラベルクラス
"""label = tk.Label(root,
                
)"""

#ボタンクラス
r, c = 0, 0
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


"""button1 = tk.Button(root, text = "1", font=("Times New Roman", 30),command=button_click, width=4, height=2)
button2 = tk.Button(root, text = "2", font=("Times New Roman", 30), width=4, height=2)
button3 = tk.Button(root, text = "3", font=("Times New Roman", 30), width=4, height=2)
button4 = tk.Button(root, text = "4", font=("Times New Roman", 30), width=4, height=2)
button5 = tk.Button(root, text = "5", font=("Times New Roman", 30), width=4, height=2)
button6 = tk.Button(root, text = "6", font=("Times New Roman", 30), width=4, height=2)
button7 = tk.Button(root, text = "7", font=("Times New Roman", 30), width=4, height=2)
button8 = tk.Button(root, text = "8", font=("Times New Roman", 30), width=4, height=2)
button9 = tk.Button(root, text = "9", font=("Times New Roman", 30), width=4, height=2)
button0 = tk.Button(root, text = "0", font=("Times New Roman", 30), width=4, height=2)


#ウィジェットの設定
button1.grid(row=3, column=3)
button2.grid(row=3, column=2)
button3.grid(row=3, column=1)
button4.grid(row=2, column=3)
button5.grid(row=2, column=2)
button6.grid(row=2, column=1)
button7.grid(row=1, column=3)
button8.grid(row=1, column=2)
button9.grid(row=1, column=1)
button0.grid(row=4, column=1)"""


root.mainloop()