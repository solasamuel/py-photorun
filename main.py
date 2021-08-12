from tkinter import ttk, Tk, PhotoImage, RIDGE, Canvas, GROOVE, HORIZONTAL, Scale, filedialog
from PIL import Image, ImageTk
import cv2


class Interface:
    def __init__(self, master):
        self.master = master
        self.master.geometry('950x800+250+10')
        self.master.title('Image Editor app with Tkinter and OpenCV')
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


    def refresh_side(self):
        try:
            self.side.grid_forget()
        except:
            pass

        # self.canvas.unbind("<ButtonPress>")
        # self.canvas.unbind("<B1-Motion>")
        # self.canvas.unbind("<ButtonRelease>")
        # self.display_image(self.edited_image)


        self.side = ttk.Frame(self.menu)
        self.side.grid(row=0, column=2, rowspan=10)
        self.side.config(relief=GROOVE, padding=(50, 15))

    def upload_action(self):
        self.canvas.delete("all")

        self.filename = filedialog.askopenfilename()
        self.original_image = cv2.imread(self.filename)

        self.edited_image = cv2.imread(self.filename)
        self.filtered_image = cv2.imread(self.filename)

        self.display_image(self.edited_image)

    def crop_action(self):
        pass

    def rotate_action(self):
        self.refresh_side()
        ttk.Button(self.side, text="Rotate Left", command=self.rotate_left_action).grid(
            row=0, column=2,
            padx=5, pady=5, sticky='sw'
        )

        ttk.Button(self.side, text="Rotate Right", command=self.rotate_right_action).grid(
            row=1, column=2,
            padx=5, pady=5, sticky='sw'
        )

    def flip_action(self):
        self.refresh_side()
        ttk.Button(self.side, text="Vertical", command=self.vertical_action).grid(
            row=0, column=2,
            padx=5, pady=5, sticky='sw'
        )

        ttk.Button(self.side, text="Horizontal", command=self.horizontal_action).grid(
            row=1, column=2,
            padx=5, pady=5, sticky='sw'
        )

    def filters_action(self):
        self.refresh_side()
        ttk.Button(self.side, text="Negative", command=self.negative_action).grid(
            row=0, column=2,
            padx=5, pady=5, sticky='sw'
        )

        ttk.Button(self.side, text="Black and White", command=self.bw_action).grid(
            row=1, column=2,
            padx=5, pady=5, sticky='sw'
        )

        ttk.Button(self.side, text="Stylisation", command=self.stylisation_action).grid(
            row=2, column=2,
            padx=5, pady=5, sticky='sw'
        )

        ttk.Button(self.side, text="Sketch", command=self.sketch_action).grid(
            row=3, column=2,
            padx=5, pady=5, sticky='sw'
        )

        ttk.Button(self.side, text="Emboss", command=self.emboss_action).grid(
            row=4, column=2,
            padx=5, pady=5, sticky='sw'
        )

        ttk.Button(self.side, text="Sepia", command=self.sepia_action).grid(
            row=5, column=2,
            padx=5, pady=5, sticky='sw'
        )

        ttk.Button(self.side, text="Binary Thresholding", command=self.binary_thresholding_action).grid(
            row=6, column=2,
            padx=5, pady=5, sticky='sw'
        )

        ttk.Button(self.side, text="Erosion", command=self.erosion_action).grid(
            row=7, column=2,
            padx=5, pady=5, sticky='sw'
        )

        ttk.Button(self.side, text="Dilation", command=self.dilation_action).grid(
            row=8, column=2,
            padx=5, pady=5, sticky='sw'
        )

    def blur_action(self):
        self.refresh_side()

        ttk.Label(self.side, text="Averaging Blur").grid(
            row=0, column=0, padx=5, sticky='sw'
        )
        self.average_slider = Scale(
            self.side, from_=0, to_=256, orient=HORIZONTAL, command=self.averaging_action
        )
        self.average_slider.grid(
            row=1, column=2, padx=5, sticky='sw'
        )

        ttk.Label(self.side, text="Gaussian Blur").grid(
            row=2, column=0, padx=5, sticky='sw'
        )
        self.gaussian_slider = Scale(
            self.side, from_=0, to_=256, orient=HORIZONTAL, command=self.gaussian_action
        )
        self.gaussian_slider.grid(
            row=3, column=2, padx=5, sticky='sw'
        )

        ttk.Label(self.side, text="Median Blur").grid(
            row=4, column=0, padx=5, sticky='sw'
        )
        self.median_slider = Scale(
            self.side, from_=0, to_=256, orient=HORIZONTAL, command=self.median_action
        )
        self.median_slider.grid(
            row=5, column=2, padx=5, sticky='sw'
        )

    def levels_action(self):
        self.refresh_side()
        ttk.Label(
            self.side, text="Brightness").grid(
            row=0, column=2,
            padx=5, pady=5, sticky='sw'
        )

        self.brightness_slider = Scale(
            self.side, from_=0, to_=2, resolution=0.1, orient=HORIZONTAL, command=self.brightness_action
        )
        self.brightness_slider.grid(row=1, column=2, padx=5, sticky='sw')
        self.brightness_slider.set(1)

        ttk.Label(
            self.side, text="Saturation").grid(
            row=2, column=2,
            padx=5, pady=5, sticky='sw'
        )

        self.saturation_slider = Scale(
            self.side, from_=-200, to_=200, resolution=0.5, orient=HORIZONTAL, command=self.brightness_action
        )
        self.saturation_slider.grid(row=3, column=2, padx=5, sticky='sw')
        self.saturation_slider.set(0)


    def draw_action(self):
        pass

    def text_action(self):
        self.refresh_side()
        ttk.Label(self.side, text="Enter a text").grid(row=0, column=0)

    def save_action(self):
        pass

    def apply_action(self):
        pass

    def cancel_action(self):
        pass

    def revert_action(self):
        pass

    def negative_action(self):
        pass

    def bw_action(self):
        pass

    def stylisation_action(self):
        pass

    def sketch_action(self):
        pass

    def emboss_action(self):
        pass

    def erosion_action(self):
        pass

    def dilation_action(self):
        pass

    def sepia_action(self):
        pass

    def binary_thresholding_action(self):
        pass

    def averaging_action(self):
        pass

    def median_action(self):
        pass

    def gaussian_action(self):
        pass

    def rotate_left_action(self):
        pass

    def rotate_right_action(self):
        pass

    def vertical_action(self):
        pass

    def horizontal_action(self):
        pass

    def brightness_action(self):
        pass

    def saturation_action(self):
        pass

    def display_image(self, image=None):
        self.canvas.delete("all")

        if image is None:
            image = self.edited_image.copy()
        else:
            image = image

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channels = image.shape
        ratio = height /width

        new_width = width
        new_height = height

        if height > 400 or width >300:
            if ratio < 1:
                new_width = 300
                new_height = int(new_width * ratio)
            else:
                new_height = 400
                new_width = int(new_height * (width / height))

        self.ratio = height / new_height
        self.new_image = cv2.resize(image, (new_width, new_height))

        self.new_image = ImageTk.PhotoImage(
            Image.fromarray(self.new_image)
        )

        self.canvas.config(width=new_width, height=new_height)
        self.canvas.create_image(
            new_width / 2, new_height / 2, image=self.new_image
        )




root = Tk()
Interface(root)
root.mainloop()
