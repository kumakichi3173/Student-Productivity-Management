
# https://imagingsolution.net/program/python/tkinter/labelframe/

import tkinter as tk

class Application(tk.Frame):
  def __init__(self, master = None):
    super().__init__(master)

    self.master.title("ラベルフレームの作成")
    self.master.geometry("300x200")

    self.labelframe1 = tk.LabelFrame(self.master, text = "フレーム1")

    self.radio_value1 = tk.IntVar(value = 0)

    self.radio1 = tk.Radiobutton(self.labelframe1, text = "項目1", variable = self.radio_value1, value = 0)
    self.radio2 = tk.Radiobutton(self.labelframe1, text = "項目2", variable = self.radio_value1, value = 1)
    self.radio3 = tk.Radiobutton(self.labelframe1, text = "項目3", variable = self.radio_value1, value = 2)

    self.radio1.pack()
    self.radio2.pack()
    self.radio3.pack()

    self.labelframe1.pack()


    self.labelframe2 = tk.LabelFrame(self.master, text = "フレーム2", labelanchor = "nw", width = 200, height = 100)
    self.labelframe2.propagate(False)  # 幅と高さを指定する場合は、この設定が必要

    self.radio_value2 = tk.IntVar(value = 1)

    self.radio4 = tk.Radiobutton(self.labelframe2, text = "項目1", variable = self.radio_value2, value = 0)
    self.radio5 = tk.Radiobutton(self.labelframe2, text = "項目2", variable = self.radio_value2, value = 1)
    self.radio6 = tk.Radiobutton(self.labelframe2, text = "項目3", variable = self.radio_value2, value = 2)

    self.radio4.pack(anchor = tk.W)
    self.radio5.pack(anchor = tk.W)
    self.radio6.pack(anchor = tk.W)

    self.labelframe2.pack()


if __name__ == "__main__":
  root = tk.Tk()
  app = Application(master = root)
  app.mainloop()


