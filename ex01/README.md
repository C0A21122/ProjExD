# 第1回
## アルファベットゲーム（ex01/alphabet.py）
### 遊び方
* alphabet.pyを実行すると、標準出力に問題が表示されます。
* 標準入力から欠損文字数と欠損した文字の答えを入力してください。
* 欠損文字数を正解した場合は、欠損文字の答えを同じ場所に入力してください。
* 欠損文字数、欠損文字を間違えた場合は再チャレンジとなり、別の文字列が表示されます。
* 5回まで再チャレンジできます。
### プログラム内の解説
* main関数でゲーム全体の流れを制御します。
* shutudai関数で問題の出力をします。
* kaitou関数で入力された解答を検証し結果を出力します。