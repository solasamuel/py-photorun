from tkinter import ttk, Tk, PhotoImage, RIDGE, Canvas, GROOVE


class Interface:
    def __init__(self, master):
        self.master = master
        self.header = ttk.Frame(self.master)
        self.header.pack()

        self.logo = PhotoImage(file="logo.png").subsample(2, 2)

        ttk.Label(self.header, image=self.logo).grid(
            row=0, column=0, rowspan=2
        )

        ttk.Label(self.header, text="Photorun").grid(
            row=0, column=1, columnspan=1
        )
        ttk.Label(self.header, text="A light-weight photo editor").grid(
            row=1, column=1, columnspan=1
        )

        self.menu = ttk.Frame(self.master)
        self.menu.pack()
        self.menu.config(relief=RIDGE, padding=(50, 15))

        self.upload_icon = PhotoImage(file="icons/upload.png")

        ttk.Button(self.menu, image=self.upload_icon, command=self.upload_action).grid(
            row=0, column=0, columnspan=1
        )

        self.crop_icon = PhotoImage(file="icons/crop.png")

        ttk.Button(self.menu, image=self.crop_icon, command=self.crop_action).grid(
            row=1, column=0, columnspan=1
        )

        self.rotate_icon = PhotoImage(file="icons/rotate.png")

        ttk.Button(self.menu, image=self.rotate_icon, command=self.rotate_action).grid(
            row=2, column=0, columnspan=1
        )

        self.flip_icon = PhotoImage(file="icons/flip.png").subsample(14, 14)

        ttk.Button(self.menu, image=self.flip_icon, command=self.flip_action).grid(
            row=3, column=0, columnspan=1
        )

        self.filters_icon = PhotoImage(file="icons/filters.png")

        ttk.Button(self.menu, image=self.filters_icon, command=self.filters_action).grid(
            row=4, column=0, columnspan=1
        )

        self.blur_icon = PhotoImage(file="icons/drop.png")

        ttk.Button(self.menu, image=self.blur_icon, command=self.blur_action).grid(
            row=5, column=0, columnspan=1
        )

        self.levels_icon = PhotoImage(file="icons/controls.png")

        ttk.Button(self.menu, image=self.levels_icon, command=self.levels_action).grid(
            row=6, column=0, columnspan=1
        )

        self.draw_icon = PhotoImage(file="icons/draw.png")

        ttk.Button(self.menu, image=self.draw_icon, command=self.draw_action).grid(
            row=7, column=0, columnspan=1
        )

        self.text_icon = PhotoImage(file="icons/typography.png")

        ttk.Button(self.menu, image=self.text_icon, command=self.text_action).grid(
            row=8, column=0, columnspan=1
        )

        self.save_icon = PhotoImage(file="icons/save.png")

        ttk.Button(self.menu, image=self.save_icon, command=self.save_action).grid(
            row=9, column=0, columnspan=1
        )

        self.apply_and_cancel = ttk.Frame(self.master)
        self.apply_and_cancel.pack()

        self.apply_icon = PhotoImage(file="icons/apply.png")

        self.apply = ttk.Button(
            self.apply_and_cancel, image=self.apply_icon, command=self.apply_action
        )
        self.apply.grid(
            row=0, column=0,
            padx=5, pady=5, sticky='sw'
        )

        self.cancel_icon = PhotoImage(file="icons/cancel.png")

        ttk.Button(
            self.apply_and_cancel, image=self.cancel_icon, command=self.cancel_action
        ).grid(row=0, column=1,
               padx=5, pady=5, sticky='sw'
               )

        self.revert_icon = PhotoImage(file="icons/revert.png")

        ttk.Button(
            self.apply_and_cancel, image=self.revert_icon, command=self.revert_action
        ).grid(
            row=0, column=2,
            padx=5, pady=5, sticky='sw'
        )

        self.canvas = Canvas(self.menu, bg="gray", width=500, height=600)
        self.canvas.grid(row=0, column=1, rowspan=10)



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

    def save_action(self):
        pass

    def apply_action(self):
        pass

    def cancel_action(self):
        pass

    def revert_action(self):
        pass


root = Tk()
Interface(root)
root.mainloop()
