import random

#グローバル変数
global lets, lost_chars, max_nums
lets = 8 #文字数
lost_chars = 2 #欠損文字数
max_nums = 5 #最大繰り返し回数


def main():
    for i in range(max_nums):
        seikai = shutudai()
    #kaitou(seikai)
    

def shutudai():
    all_alphabet_list = [chr(i+65) for i in range(26)]
    all_chars = random.sample(all_alphabet_list,lost_chars)
    print("対象文字：\n"+str(all_chars))
    #lost_alphabet = all_chars()

def kaitou(seikai):
    answer = input("欠損文字はいくつあるでしょうか？：")
    if (answer == lost_chars):
        print("正解です。それでは、具体的に欠損文字を1つずつ入力してください。")

    else:
        print("不正解です。再チャレンジしましょう。")
        

if __name__ == "__main__":
    main()