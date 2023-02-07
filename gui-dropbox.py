import tkinter as tk
import tkinter.ttk as ttk # imports Combobox

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master) 

        # creates the top level window
        self.master.title("入力画面‐生徒２人セット") # ウィンドウタイトル
        self.master.geometry("400x300") # ウィンドウサイズ(幅x高さ)

        #--------------------------------------------------------
        # ラベルフレーム1の作成
        labelframe1 = tk.LabelFrame(self.master, text = "追加")
        labelframe1.propagate(False) # 幅と高さを指定する場合はこの設定が必要

        # creates label widgets
        self.label_1 = tk.Label(self.master, text = '生徒を2人選んでください。')
        self.label_1.grid(column=0, row=0,columnspan=5)
        self.label_2 = tk.Label(self.master, text = '競技を選んでください。')
        self.label_2.grid(column=0, row=3,columnspan=5)
        self.label_3 = tk.Label(self.master, text = '回数を入力してください。')
        self.label_3.grid(column=0, row=5,columnspan=5)
        self.label_4 = tk.Label(self.master, text = '回')
        self.label_4.grid(column=2, row=6)
        self.label_5 = tk.Label(self.master, text = '居残った時間を入力してください。')
        self.label_5.grid(column=0, row=7, columnspan=5)
        self.label_6 = tk.Label(self.master, text = '時間')
        self.label_6.grid(column=2, row=8)


        # Studentリスト項目の生成 for dropbox1 & dropbox2
        studentID = ["student A", "student B", "student C"] 

        # dropbox1
        self.combobox1 = ttk.Combobox(
            self.master,
            #value = self.combobox.get() # valueにユーザーがドロップボックスから選択した内容を入れる
            #outputlabel = tk.Label(self.master, text=value)
            #outputlabel.grid(row=1, column=4) # これをコメントアウトするとウィンドウ上にユーザーがインプットした情報がでなくなる
            state = 'readonly',
            value = studentID) 
            #self.combobox = ttk.Combobox(self.master, state = 'readonly', value=list)
        self.combobox1.grid(column=1, row=1)

        # dropbox2
        self.combobox2 = ttk.Combobox(
            self.master,
            #value2 = self.combobox2.get() # value2にユーザーがドロップボックスから選択した内容を入れる
            #outputlabel2 = tk.Label(self.master, text=value2)
            #outputlabel2.grid(row=2, column=4)
            state = 'readonly',
            value = studentID)             
            #self.combobox2 = ttk.Combobox(self.master, state = 'readonly', values=list2)
        self.combobox2.grid(row=2, column=1)

        # Studentリスト項目の生成 for dropbox1 & dropbox2
        sport_discipline = ["ハードル50m走", "1000m走", "幅跳び"]

        # dropbox3
        self.combobox3 = ttk.Combobox(
            self.master,
            #value3 = self.combobox3.get() # value3にユーザーがドロップボックスから選択した内容を入れる
            #outputlabel3 = tk.Label(self.master, text=value3)
            #outputlabel3.grid(row=4, column=4)
            state = 'readonly',
            value = sport_discipline) 
            #combobox3 = ttk.Combobox(self.master, state = 'readonly', values=list3)
        self.combobox3.grid(row=4, column=1)

        # 回数 TODO: 実行時エラーあり。入力した情報がvalidな内容としてアウトプットされていない。
        self.entry1 = ttk.Entry(
            self.master,
            #self.value4 = self.txt.get() # value2にユーザーがドロップボックスから選択した内容を入れる
            #outputlabel4 = tk.Label(self.master, text=self.txt)
            #outputlabel4.grid(row=6, column=4)

            # Entry widget  
            #txt = tk.Entry(width=3)
            width=3)
        self.entry1.grid(row=6, column=1)

        #def click(self):
            #messagebox.showinfo(('確認画面'), self.times.get())

        # 居残り時間
        self.entry2 = ttk.Entry(
            self.master,
            width=3)
        self.entry2.grid(row=8, column=1)

        # ボタンウィジェット1
        self.button1 = tk.Button(
            self.master, 
            text = '追加',
            command = self.add_record)
        self.button1.grid(row=9, column=2)

        # ボタンウィジェット2
        self.button2 = tk.Button(
            self.master, 
            text = '削除',
            command = self.remove_data)
        self.button2.grid(row=9, column=3)

        # ボタンウィジェット3
        self.button3 = tk.Button(
            self.master, 
            text = '表示', 
            command = self.view_data)
        self.button3.grid(row=10, column=0, columnspan=5)
            
        # ラベルの配置
        #self.labelframe1.grid(row=7, column=3) #TODO: フレームが予期した形で配置されない。

        #--------------------------------------------------------

    def add_record(self):
        print("add_record()")
        print(self.combobox1.get())
        print(self.combobox2.get())
        print(self.combobox3.get())
        print(self.entry1.get())
        print(self.entry2.get())

        # キーと値を用意します(エラー処理は省略)
        key = (self.combobox1.get(), self.combobox2.get(), self.combobox3.get())
        val = (self.entry1.get(), self.entry2.get())

        # 辞書にデータを追加(キーが同じ場合は更新)
        data.update({key: val})

        # キーで昇順ソートをしたデータを出力します
        print(sorted(data.items()))

    def remove_data(self):
        # GUIで選択しているキーを取り出します
        key = (self.combobox1.get(), self.combobox2.get(), self.combobox3.get())

        # データを取り出すことで削除をします
        data.pop(key)

        # デバッグ用にキーで昇順ソートをしたデータを出力します
        print(sorted(data.items()))

    def view_data(self):
        subwindow = tk.Toplevel(self)
        subwindow.title("出力画面‐生徒２人セット")
        subwindow.geometry("640x380")

        records = []
        for i, (key, datum) in enumerate(sorted(data.items()), 1):
            records.append(f'{i} : {key[0]} と {key[1]} は {key[2]} を {datum[0]}回, 居残り:{datum[1]}時間')

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

        # 各列の割合を指定
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.master.columnconfigure(3, weight=1)
        self.master.columnconfigure(4, weight=1)

        # 各行の割合を指定
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)
        self.master.rowconfigure(3, weight=1)
        self.master.rowconfigure(4, weight=1)
        self.master.rowconfigure(5, weight=1)
        self.master.rowconfigure(6, weight=1)
        self.master.rowconfigure(7, weight=1)
        self.master.rowconfigure(8, weight=1)
        self.master.rowconfigure(9, weight=1)
        self.master.rowconfigure(10, weight=1)

if __name__ == "__main__":
      # データを保存する辞書
    data = {}

    root = tk.Tk()

    app = Application(master = root)
    # トップレベルウィンドウの表示
    app.mainloop()