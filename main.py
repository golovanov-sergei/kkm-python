import tkinter as tk
from tkinter import ttk


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.goods_list = []


    def init_main(self):
        toolbar = tk.Frame(bg='red', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # self.add_img = tk.PhotoImage(file="add.gif")
        btn_open_dialog = tk.Button(toolbar, text='Штрихкод (F7)', command=self.open_dialog, bg='#d7d8e0', bd=1,
                                    compound=tk.TOP)
        btn_open_dialog.pack(side=tk.LEFT)

        btn_addGood = tk.Button(toolbar, text='Добавить товар', command=self.open_addGood, bg='#d7d8e0', bd=1,
                                    compound=tk.TOP)
        btn_addGood.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('No', 'barcode', 'description', 'price'),
                                 height=15, show='headings')
        self.tree.column("No", width=30, anchor=tk.CENTER)
        self.tree.column("barcode", width=150, anchor=tk.CENTER)
        self.tree.column("description", width=365, anchor=tk.CENTER)
        self.tree.column("price", width=100, anchor=tk.CENTER)

        self.tree.heading("No", text='#')
        self.tree.heading("barcode", text='Штрихкод')
        self.tree.heading("description", text='Описание')
        self.tree.heading("price", text='Цена')

        self.tree.pack(side=tk.BOTTOM)

        # statusbar = tk.Frame(bg='blue', bd=10)
        # statusbar.pack(side="bottom", fill= tk.X)

        # status_text = tk.Label(statusbar,text='Status text')
        # status_text.place(x=0, y= -10)
        statusbar = tk.Label(root, text='KKM', relief=tk.SUNKEN, anchor=tk.W)
        statusbar.pack(side=tk.BOTTOM, fill=tk.X)

    def add_good_in_check(self,desc,price):
        self.goods_list.append([desc,price])
        # self.tree.insert('','end',values=[len(self.goods_list),'',desc,price])
        self.update_treeview()

    def update_treeview(self):
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=[idx+1,'',self.goods_list[idx][0],self.goods_list[idx][1]]) for idx in range(len(self.goods_list))]

    def open_dialog(self):
        Child()

    def open_addGood(self):
        addGood()

class addGood(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_form()
        self.mainwindow = app


    def init_form(self):
        self.title('Добавление товара')
        self.geometry('430x110+100+100')
        self.resizable(True,True)

        label_GoodDescr = tk.Label(self, text='Наименование:')
        label_GoodDescr.place(x=10,y=10)

        self.GoodDescr = ttk.Entry(self,width=50)
        self.GoodDescr.place(x=110,y=10)

        label_Price = tk.Label(self, text='Цена:')
        label_Price.place(x=10,y=40)

        self.Price = ttk.Entry(self,width=10)
        self.Price.place(x=110,y=40)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=150, y=70)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=50, y=70)
        self.btn_ok.bind('<Button-1>', lambda event: self.mainwindow.add_good_in_check(self.GoodDescr.get(),self.Price.get()))


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Ввести штрихкод')
        self.geometry('400x380+400+300')
        self.resizable(False, False)

        label_barcode = tk.Label(self, text='Штрихкод:')
        label_barcode.place(x=50, y=20)

        self.entry_barcode = ttk.Entry(self)
        self.entry_barcode.place(x=120, y=20)

        # self.combobox = ttk.Combobox(self, values=[u"Доход", u"Расход"])
        # self.combobox.current(0)
        # self.combobox.place(x=200, y=80)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        btn_ok = ttk.Button(self, text='Добавить')
        btn_ok.place(x=220, y=170)
        btn_ok.bind('<Button-1>')

        self.grab_set()
        self.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Регистрация продажи в ККМ")
    root.geometry("650x450+300+200")
    root.resizable(True, True)
    root.mainloop()
