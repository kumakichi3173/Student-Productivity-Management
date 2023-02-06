
# https://imagingsolution.net/program/python/tkinter/create_windows_modal_modeless/

import tkinter as tk

class Application(tk.Frame):
  def __init__(self, master = None):
    super().__init__(master)

    self.master.title("Main")
    self.master.geometry("300x200")

    btn_modeless = tk.Button(
      self.master,
      text = "Modeles dialog",
      command = self.create_modeless_dialog)
    btn_modeless.pack()

    btn_modal = tk.Button(
      self.master,
      text = "Modal dialog",
      command = self.create_modal_dialog)
    btn_modal.pack()

  def create_modeless_dialog(self):
    dlg_modeless = tk.Toplevel(self)
    dlg_modeless.title("Modeless Dialog")
    dlg_modeless.geometry("300x200")

  def create_modal_dialog(self):
    dlg_modal = tk.Toplevel(self)
    dlg_modal.title("Modal Dialog")
    dlg_modal.geometry("300x200")

    dlg_modal.grab_set()
    dlg_modal.focus_set()
    dlg_modal.transient(self.master)

    app.wait_window(dlg_modal)
    print("ダイアログが閉じられた")


if __name__ == "__main__":
  root = tk.Tk()
  app = Application(master = root)
  app.mainloop()

