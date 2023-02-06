import tkinter as tk
import tkinter.ttk as ttk


class Application(tk.Frame):
  def __init__(self, master = None):
    super().__init__(master)

    self.master.title("Combobox")
    self.master.geometry("300x200")

    
    combobox = ttk.Combobox(
      self.master,
      state = 'readonly',
      value = ["生徒" + chr(ord('A') + i) for i in range(26)])
    combobox.pack()

if __name__ == "__main__":
  root = tk.Tk()

  app = Application(master = root)
  app.mainloop()

