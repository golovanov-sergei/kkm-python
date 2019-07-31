import tkinter as tk

class MyDialog(object):
    def __init__(self, parent):
        self.toplevel = tk.Toplevel(parent)

        choices = ("one", "two","three")
        names = tk.StringVar(value=choices)

        label = tk.Label(self.toplevel, text="Pick something:")
        self.listbox = tk.Listbox(self.toplevel, listvariable=names, height=3,
            selectmode="single", exportselection=0)
        button = tk.Button(self.toplevel, text="OK", command=self.toplevel.destroy)

        label.pack(side="top", fill="x")
        self.listbox.pack(side="top", fill="x")
        button.pack()

        # add binding
        self.listbox.bind('<<ListboxSelect>>', self.getSelection)

    # function associated with binding
    def getSelection(self, event):
        widget = event.widget
        selection=widget.curselection()
        self.value = widget.get(selection[0])

    # separate function for wait_window and the return of the selection
    def returnValue(self):
        self.toplevel.wait_window()
        return self.value

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.button = tk.Button(self, text="Click me!", command=self.on_click)
        self.label = tk.Label(self, width=80)
        self.label.pack(side="top", fill="x")
        self.button.pack(pady=20)

    def on_click(self):
        result = MyDialog(self).returnValue()
        self.label.configure(text="your result: %s" % result)

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()