import tkinter as tk

class Application(tk.Frame):
  def __init__(self, master = None):
    super().__init__(master)

    self.master.title("List UI")
    self.master.geometry("640x380")

    records = []
    for i, (key, datum) in enumerate(sorted(data.items()), 1):
      records.append(f'{i} : {key[0]} - {key[1]} = {datum[0]}回, 居残り:{datum[1]}分')

    listvar = tk.StringVar(value=tuple(records))

    listbox = tk.Listbox(
      self.master,
      width = 100,
      height = 20,
      selectmode = 'single',
      listvariable=listvar
    )
    listbox.pack()

if __name__ == "__main__":
  data = {
    ('生徒B', '幅跳び'): (30, 0),
    ('生徒A', 'ハードル50m走'): (5, 90)
  }

  root = tk.Tk()

  app = Application(master = root)
  app.mainloop()

