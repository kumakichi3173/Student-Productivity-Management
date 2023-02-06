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


  def add_record(self):
    print("add_record()")
    print(self.combobox1.get())
    print(self.combobox2.get())
    print(self.entry1.get())
    print(self.entry2.get())


if __name__ == "__main__":
  root = tk.Tk()

  app = Application(master = root)
  app.mainloop()

