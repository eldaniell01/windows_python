import tkinter as tk

class Principal:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.configure(bg="#202022")
        self.root.resizable(False,False)
        self.initUI()
        
    def initUI(self):
        self.label_title = tk.Label(self.root, text="Ventanas con TKINTER", fg='#CACACA', bg="#202022", font=('Arial', 24, 'bold'))
        self.label_title.grid(row=0, column=0, columnspan=3, pady=20)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.mi_frame = tk.LabelFrame(master=self.root, text='OPCIONES', font=('JetBrainsMono Nerd Font', 14, 'bold'), fg='#CACACA', width=700, height=400, padx=10, pady=10, bg="#16232E")
        self.mi_frame.grid(row=1, column=0, columnspan=3)
        self.mi_frame.propagate(0)
        self.buttom = tk.Button(master=self.mi_frame, text='ventana estática')
        self.buttom.grid(row=0, column=0, padx=10, pady=10)
        """
        
        def window(root):
    root.geometry("800x600")
    root.configure(bg="#202022")
    root. resizable(False,False)
    label_title = tk.Label(root, text="Ventanas con TKINTER", fg='#CACACA', bg="#202022", font=('Arial', 24, 'bold'))
    label_title.grid(row=0, column=0, columnspan=3, pady=20,)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.mainloop()
        
        """
