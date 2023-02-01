import tkinter as tk
import random

omikuji = ['大吉', '中吉', '小吉', '吉末', '吉凶', '中凶', '大凶']

root = tk.Tk()
root.title('おみくじ')
root.geometry('300x150')

label = tk.Label(root,text = '運勢は'+ random.choice(omikuji)+'です。', padx = 10, pady = 10, relief = tk.RIDGE)

# ウィンドウと同じサイズの占領領域にする。
label.pack(expand=True)

root.mainloop()