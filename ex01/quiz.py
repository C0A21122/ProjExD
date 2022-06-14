import random

x = (random.randint(1,4))

#一問目 
if (x == 1):
    print("問題：\nサザエの旦那の名前は？")
    answer = input("答えを入力してください：")
    if (answer == "マスオ"):
        print("正解です！")
    elif (answer == "ますお"): #マスオTVです。
        print("正解です！")
    else:
        print("不正解です")
#二問目 
if (x == 2):
    print("問題：\nカツオの妹の名前は？")
    answer = input("答えを入力してください：")
    if (answer == "ワカメ"):
        print("正解です！")
    elif (answer == "わかめ"):
        print("正解です！")
    else:
        print("不正解です")
#三問目 
if (x == 3):
    print("問題：\nタラオはカツオから見てどんな関係？")
    answer = input("答えを入力してください：")
    if (answer == "甥"):
        print("正解です！")
    elif (answer == "おい"):
        print("正解です！")
    elif (answer == "甥っ子"):
        print("正解です！")
    elif (answer == "おいっこ"):
        print("正解です！")
    else:
        print("不正解です")
