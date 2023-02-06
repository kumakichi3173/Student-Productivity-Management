import tkinter as tk
import tkinter.ttk as ttk


class Application(tk.Frame):
  def __init__(self, master = None):
    super().__init__(master)

    self.master.title("Combobox")
    self.master.geometry("400x200")

    self.combobox1 = ttk.Combobox(
      self.master,
      state = 'readonly',
      value = ["生徒" + chr(ord('A') + i) for i in range(26)])
    self.combobox1.pack(side=tk.LEFT)


    sport_discipline = ["ハードル50m走", "1000m走", "幅跳び"]

    self.combobox2 = ttk.Combobox(
      self.master,
      state = 'readonly',
      value = sport_discipline)
    self.combobox2.pack(side=tk.LEFT)


    self.entry1 = ttk.Entry(
      self.master,
      justify=tk.RIGHT,
      width=5)
    self.entry1.pack(side=tk.LEFT)

    self.entry2 = ttk.Entry(
      self.master,
      justify=tk.RIGHT,
      width=5)
    self.entry2.pack(side=tk.LEFT)


    button = tk.Button(
      self.master,
      text = "追加",
      command = self.add_record)
    button.pack()

    button_view = tk.Button(
      self.master,
      text = "表示",
      command = self.view_data)
    button_view.pack()


  def add_record(self):
    print("add_record()")
    print(self.combobox1.get())
    print(self.combobox2.get())
    print(self.entry1.get())
    print(self.entry2.get())

    # キーと値を用意します(エラー処理は省略)
    key = (self.combobox1.get(), self.combobox2.get())
    val = (self.entry1.get(), self.entry2.get())

    # 辞書にデータを追加(キーが同じ場合は更新)
    data.update({key: val})

    # キーで昇順ソートをしたデータを出力します
    print(sorted(data.items()))


  def view_data(self):
    subwindow = tk.Toplevel(self)
    subwindow.title("List")
    subwindow.geometry("640x380")

    records = []
    for i, (key, datum) in enumerate(sorted(data.items()), 1):
      records.append(f'{i} : {key[0]} - {key[1]} = {datum[0]}回, 居残り:{datum[1]}分')

    listvar = tk.StringVar(value=tuple(records))

    listbox = tk.Listbox(
      subwindow,
      width = 100,
      height = 20,
      selectmode = 'single',
      listvariable=listvar
    )
    listbox.pack()

    # モーダルに設定する
    subwindow.grab_set()
    subwindow.focus_set()
    subwindow.transient(self.master)

    app.wait_window(subwindow)


if __name__ == "__main__":
  # データを保存する辞書
  data = {}

  root = tk.Tk()

  app = Application(master = root)
  app.mainloop()
