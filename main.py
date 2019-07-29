import tkinter as tk
from tkinter import ttk


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.goods_list = []


    def init_main(self):
        frameMain = tk.Frame(self, relief=tk.RAISED,borderwidth=1)
        frameMain.pack(side=tk.TOP, fill=tk.BOTH)

        # self.add_img = tk.PhotoImage(file="add.gif")
        btn_open_dialog = tk.Button(frameMain, text='Штрихкод (F7)', command=self.open_dialog, bg='#d7d8e0', bd=1,
                                    compound=tk.TOP,width=15)
        btn_open_dialog.grid(row=0,column=0)

        btn_addGood = tk.Button(frameMain, text='Добавить товар', command=self.open_addGood, bg='#d7d8e0', bd=1,
                                    compound=tk.TOP,width=15)
        btn_addGood.grid(row=0,column=1)

        btn_delGood = tk.Button(frameMain, text='Удалить',command=self.DeleteGood, bg='#d7d8e0', bd=1,
                                    compound=tk.TOP,width=15)
        btn_delGood.grid(row=0,column=2)

        btn_Seller = tk.Button(frameMain, text='Продавец',command=self.selectSeller, bg='#d7d8e0', bd=1,
                                    compound=tk.TOP,width=15)
        btn_Seller.grid(row=0,column=3)

        btn_CloseCheck = tk.Button(frameMain, text='Оплата',command=self.closeCheck, bg='#d7d8e0', bd=1,
                                    compound=tk.TOP,width=15)
        btn_CloseCheck.grid(row=0,column=4)

        #frmMain = ttk.Frame(self,borderwidth=1)
        #frmMain.pack(fill=tk.X)
        self.tree = ttk.Treeview(frameMain, columns=('No', 'barcode', 'description', 'price'),
                                 height=15, show='headings')
        self.tree.column("No", width=30, anchor=tk.CENTER)
        self.tree.column("barcode", width=150, anchor=tk.CENTER)
        self.tree.column("description", width=365, anchor=tk.CENTER)
        self.tree.column("price", width=100, anchor=tk.CENTER)

        self.tree.heading("No", text='#')
        self.tree.heading("barcode", text='Штрихкод')
        self.tree.heading("description", text='Описание')
        self.tree.heading("price", text='Цена')

        self.tree.grid(row=1,column=0,columnspan=5)

        self.seller_label=tk.Label(frameMain,text='Продавец:')
        self.seller=tk.Label(frameMain,fg='red',text='не выбран',font=('Arial',10,'bold'))
        self.total_label=tk.Label(frameMain,text='Итого:')
        self.total=tk.Label(frameMain,text='0,00')

        self.seller_label.grid(row=2)
        self.seller.grid(row=2,column=1)
        self.total_label.grid(row=2,column=2)
        self.total.grid(row=2,column=3)

        # statusbar = tk.Frame(bg='blue', bd=10)
        # statusbar.pack(side="bottom", fill= tk.X)

        # status_text = tk.Label(statusbar,text='Status text')
        # status_text.place(x=0, y= -10)
        statusbar = tk.Label(root, text='Подключено оборудование:', relief=tk.SUNKEN, anchor=tk.W)
        statusbar.pack(side=tk.BOTTOM, fill=tk.X)

    def closeCheck(self):
        CloseCheck()

    def selectSeller(self):
        Child()

    def DeleteGood(self):
        for item in self.tree.selection():
            elem = int(self.tree.item(item)['values'][0])
            del self.goods_list[elem-1]
            self.update_treeview()

    def add_good_in_check(self,barcode,desc,price):
        self.goods_list.append([barcode,desc,price])
        # self.tree.insert('','end',values=[len(self.goods_list),'',desc,price])
        self.update_treeview()

    def update_treeview(self):
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=[idx+1,self.goods_list[idx][0],self.goods_list[idx][1],self.goods_list[idx][2]]) for idx in range(len(self.goods_list))]

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
        self.geometry('430x140+100+100')
        self.resizable(True,True)

        label_Barcode = tk.Label(self, text='Штрихкод:')
        label_Barcode.place(x=10,y=10)

        self.Barcode = ttk.Entry(self,width=15)
        self.Barcode.place(x=110,y=10)

        label_GoodDescr = tk.Label(self, text='Наименование:')
        label_GoodDescr.place(x=10,y=40)

        self.GoodDescr = ttk.Entry(self,width=50)
        self.GoodDescr.place(x=110,y=40)

        label_Price = tk.Label(self, text='Цена:')
        label_Price.place(x=10,y=70)

        self.Price = ttk.Entry(self,width=10)
        self.Price.place(x=110,y=70)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=50, y=110)
        self.btn_ok.bind('<Button-1>', lambda event: self.mainwindow.add_good_in_check(self.Barcode.get(),self.GoodDescr.get(),self.Price.get()))

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=150, y=110)


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


class CloseCheck(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.initForm()

    def initForm(self):
        self.title('Закрытие чека')
        #self.geometry('420x360+400+300')
        self.resizable(True,True)
        #frame = ttk.Frame(self, relief=tk.RAISED, borderwidth=1)
        #frame.pack(fill=tk.BOTH, expand=True)
        # self.pack(fill=tk.BOTH, expand=True)

        label_total=ttk.Label(self,text='Всего к оплате:')
        label_change=ttk.Label(self,text='Сдача:')
        label_total.grid(row=0,column=0,sticky='W',padx=5, pady=5)
        label_change.grid(row=0,column=1,sticky='W',padx=5, pady=5)

        entry_total = ttk.Entry(self,width=15)
        entry_change = ttk.Entry(self,width=15)
        entry_total.grid(row=1,column=0,padx=5, pady=5,sticky='W')
        entry_change.grid(row=1, column=1,padx=5, pady=5,sticky='W')

        label_payed=ttk.Label(self,text='Вносимая сумма:')
        label_payed.grid(row=2,column=0,sticky='W',padx=5, pady=5,columnspan=2)
        entry_payed=ttk.Entry(self)
        entry_payed.grid(row=3,column=0,padx=5, pady=5,columnspan=2,sticky=tk.N+tk.S+tk.E+tk.W)

        closeButton = ttk.Button(self, text="Close")
        closeButton.grid(row=5,column=1,padx=5, pady=5)
        okButton = ttk.Button(self, text="OK")
        okButton.grid(row=5,column=0,padx=5, pady=5)

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
