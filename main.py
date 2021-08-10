from tkinter import ttk, Tk, PhotoImage, RIDGE


class Interface:
    def __init__(self, master):
        self.master = master
        self.header = ttk.Frame(self.master)
        self.header.pack()

        self.logo = PhotoImage(file="logo.png").subsample(5,5)

        ttk.Label(self.header, image=self.logo).grid(
            row=0, column=0, rowspan=2
        )

        ttk.Label(self.header, text="Photorun").grid(
            row=0, column=1, columnspan=1
        )
        ttk.Label(self.header, text="A lightweight photo editor").grid(
            row=1, column=1, columnspan=1
        )

        self.menu = ttk.Frame(self.master)
        self.menu.pack()
        self.menu.config(relief=RIDGE, padding=(50, 15))

        self.upload_icon = PhotoImage(file="icons/upload.svg")

        ttk.Button(self.menu, image=self.upload_icon, command=self.upload_action).grid(
            row=0, column=1, columnspan=1
        )

        self.crop_icon = PhotoImage(file="icons/crop.svg")

        ttk.Button(self.menu, image=self.crop_icon, command=self.crop_action).grid(
            row=1, column=1, columnspan=1
        )

        self.rotate_icon = PhotoImage(file="icons/rotate.svg")

        ttk.Button(self.menu, image=self.rotate_icon, command=self.rotate_action).grid(
            row=2, column=1, columnspan=1
        )

        self.flip_icon = PhotoImage(file="icons/flip.svg")

        ttk.Button(self.menu, image=self.flip_icon, command=self.flip_action).grid(
            row=3, column=1, columnspan=1
        )

        self.filters_icon = PhotoImage(file="icons/filters.svg")

        ttk.Button(self.menu, text="Apply filters", command=self.filters_action).grid(
            row=4, column=1, columnspan=1
        )
        ttk.Button(self.menu, text="Blur", command=self.blur_action).grid(
            row=5, column=1, columnspan=1
        )
        ttk.Button(self.menu, text="Levels", command=self.levels_action).grid(
            row=6, column=1, columnspan=1
        )
        ttk.Button(self.menu, text="Draw", command=self.draw_action).grid(
            row=7, column=1, columnspan=1
        )
        ttk.Button(self.menu, text="Text", command=self.text_action).grid(
            row=8, column=1, columnspan=1
        )

    def upload_action(self):
        pass

    def crop_action(self):
        pass

    def rotate_action(self):
        pass

    def flip_action(self):
        pass

    def filters_action(self):
        pass

    def blur_action(self):
        pass

    def levels_action(self):
        pass

    def draw_action(self):
        pass

    def text_action(self):
        pass





root = Tk()
Interface(root)
root.mainloop()