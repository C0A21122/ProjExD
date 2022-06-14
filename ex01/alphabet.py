import random

#グローバル変数
lets = 8 #文字数
lost_chars = 2 #欠損文字数
max_nums = 5 #最大繰り返し回数


def main():
    for i in range(max_nums):
        seikai = shutudai()
    #kaitou(seikai)
    

def shutudai():
    all_alphabet_list = [chr(i+65) for i in range(26)]
    all_chars = random.sample(all_alphabet_list, lets)
    print("対象文字：")
    for i in all_alphabet_list:
        print(i)
    
    print("\n欠損文字")
    lost_alphabet = random.sample(all_alphabet_list, lost_chars)
    for i in lost_alphabet:
        print(i)
    
    print("\n表示文字")



def kaitou(seikai):
    answer = input("欠損文字はいくつあるでしょうか？：")
    if (answer == lost_chars):
        print("正解です。それでは、具体的に欠損文字を1つずつ入力してください。")
        for i in range(lost_chars):
            ans = input("1つ目の文字を入力してください：")
            if ans not in seikai:
                print("不正解です。再チャレンジしましょう。")
                return 0
            else:
                return 1

    else:
        print("不正解です。再チャレンジしましょう。")
        

if __name__ == "__main__":
    main()