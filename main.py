from tkinter import ttk, Tk, PhotoImage, RIDGE, Canvas, GROOVE, HORIZONTAL, ROUND, Scale, filedialog, colorchooser
from PIL import Image, ImageTk
import cv2
import numpy as np

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

        ttk.Button(self.menu, image=self.text_icon, command=self.top_text_action).grid(
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

        self.canvasHeight = 600
        self.canvasWidth = 500
        self.canvas = Canvas(self.menu, bg="gray", width=self.canvasWidth, height=self.canvasHeight)
        self.canvas.grid(row=0, column=1, rowspan=10)


    def refresh_side(self):
        try:
            self.side.grid_forget()
        except:
            pass

        # self.canvas.unbind("<ButtonPress>")
        # self.canvas.unbind("<B1-Motion>")
        # self.canvas.unbind("<ButtonRelease>")
        self.display_image(self.edited_image)
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
        self.rectangle_id = 0
        # self.ratio = 0
        self.crop_start_x = 0
        self.crop_start_y = 0
        self.crop_end_x = 0
        self.crop_end_y = 0
        self.canvas.bind("<ButtonPress>", self.start_crop)
        self.canvas.bind("<B1-Motion>", self.crop)
        self.canvas.bind("<ButtonRelease>", self.end_crop)

    def start_crop(self, event):
        self.crop_start_x = event.x
        self.crop_start_y = event.y

    def crop(self, event):
        if self.rectangle_id:
            self.canvas.delete(self.rectangle_id)

        self.crop_end_x = event.x
        self.crop_end_y = event.y

        self.rectangle_id = self.canvas.create_rectangle(self.crop_start_x, self.crop_start_y,
                                                        self.crop_end_x, self.crop_end_y, width=1)

    def end_crop(self, event):
        if self.crop_start_x <= self.crop_end_x and self.crop_start_y <= self.crop_end_y:
            start_x = int(self.crop_start_x * self.ratio)
            start_y = int(self.crop_start_y * self.ratio)
            end_x = int(self.crop_end_x * self.ratio)
            end_y = int(self.crop_end_y * self.ratio)
        elif self.crop_start_x > self.crop_end_x and self.crop_start_y <= self.crop_end_y:
            start_x = int(self.crop_end_x * self.ratio)
            start_y = int(self.crop_start_y * self.ratio)
            end_x = int(self.crop_start_x * self.ratio)
            end_y = int(self.crop_end_y * self.ratio)
        elif self.crop_start_x <= self.crop_end_x and self.crop_start_y > self.crop_end_y:
            start_x = int(self.crop_start_x * self.ratio)
            start_y = int(self.crop_end_y * self.ratio)
            end_x = int(self.crop_end_x * self.ratio)
            end_y = int(self.crop_start_y * self.ratio)
        else:
            start_x = int(self.crop_end_x * self.ratio)
            start_y = int(self.crop_end_y * self.ratio)
            end_x = int(self.crop_start_x * self.ratio)
            end_y = int(self.crop_start_y * self.ratio)

        x = slice(start_x, end_x, 1)
        y = slice(start_y, end_y, 1)

        self.filtered_image = self.edited_image[y, x]
        self.display_image(self.filtered_image)

    def text_action(self):
        self.rectangle_id = 0
        # self.ratio = 0
        self.crop_start_x = 0
        self.crop_start_y = 0
        self.crop_end_x = 0
        self.crop_end_y = 0
        self.canvas.bind("<ButtonPress>", self.start_crop)
        self.canvas.bind("<B1-Motion>", self.crop)
        self.canvas.bind("<ButtonRelease>", self.end_text_crop)

    def end_text_crop(self, event):
        if self.crop_start_x <= self.crop_end_x and self.crop_start_y <= self.crop_end_y:
            start_x = int(self.crop_start_x * self.ratio)
            start_y = int(self.crop_start_y * self.ratio)
            end_x = int(self.crop_end_x * self.ratio)
            end_y = int(self.crop_end_y * self.ratio)
        elif self.crop_start_x > self.crop_end_x and self.crop_start_y <= self.crop_end_y:
            start_x = int(self.crop_end_x * self.ratio)
            start_y = int(self.crop_start_y * self.ratio)
            end_x = int(self.crop_start_x * self.ratio)
            end_y = int(self.crop_end_y * self.ratio)
        elif self.crop_start_x <= self.crop_end_x and self.crop_start_y > self.crop_end_y:
            start_x = int(self.crop_start_x * self.ratio)
            start_y = int(self.crop_end_y * self.ratio)
            end_x = int(self.crop_end_x * self.ratio)
            end_y = int(self.crop_start_y * self.ratio)
        else:
            start_x = int(self.crop_end_x * self.ratio)
            start_y = int(self.crop_end_y * self.ratio)
            end_x = int(self.crop_start_x * self.ratio)
            end_y = int(self.crop_start_y * self.ratio)

        if self.text_on_image.get():
            self.text_extracted = self.text_on_image.get()
        start_font = start_x, start_y
        print(self.color_code)#((r,g,b),'#ff00000')
        r, g, b = tuple(map(int, self.color_code[0]))

        self.filtered_image = cv2.putText(
            self.edited_image, self.text_extracted, start_font, cv2.FONT_HERSHEY_SIMPLEX, 2, (b, g, r), 5)
        self.display_image(self.filtered_image)

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
            self.side, from_=0, to_=2,  resolution=0.1, orient=HORIZONTAL, command=self.brightness_action)
        self.brightness_slider.grid(row=1, column=2, padx=5,  sticky='sw')
        self.brightness_slider.set(1)

        ttk.Label(
            self.side, text="Saturation").grid(
            row=2, column=2,
            padx=5, pady=5, sticky='sw'
        )

        self.saturation_slider = Scale(
            self.side, from_=-200, to=200, resolution=0.5, orient=HORIZONTAL, command=self.saturation_action)
        self.saturation_slider.grid(row=3, column=2, padx=5,  sticky='sw')
        self.saturation_slider.set(0)


    def draw_action(self):
        self.color_code = ((255, 0, 0), '#ff0000')
        self.refresh_side()
        self.canvas.bind("<ButtonPress>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.draw_color_button = ttk.Button(
            self.side, text="Pick A Color", command=self.choose_color)
        self.draw_color_button.grid(
            row=0, column=2, padx=5, pady=5, sticky='sw')

    def choose_color(self):
        self.color_code = colorchooser.askcolor(title="Choose color")

    def start_draw(self, event):
        self.x = event.x
        self.y = event.y
        self.draw_ids = []

    def draw(self, event):
        print(self.draw_ids)
        self.draw_ids.append(self.canvas.create_line(self.x, self.y, event.x, event.y, width=2,
                                                    fill=self.color_code[-1], capstyle=ROUND, smooth=True))

        cv2.line(self.filtered_image, (int(self.x * self.ratio), int(self.y * self.ratio)),
                 (int(event.x * self.ratio), int(event.y * self.ratio)),
                 (0, 0, 255), thickness=int(self.ratio * 2),
                lineType=8)

        self.x = event.x
        self.y = event.y

    def top_text_action(self):
        self.refresh_side()
        ttk.Label(self.side, text="Enter a text").grid(row=0, column=0)

    def save_action(self):
        pass

    def apply_action(self):
        self.edited_image = self.filtered_image
        self.display_image(self.edited_image)

    def cancel_action(self):
        self.display_image(self.edited_image)

    def revert_action(self):
        self.edited_image = self.original_image.copy()
        self.display_image(self.original_image)

    def negative_action(self):
        self.filtered_image = cv2.bitwise_not(self.edited_image)
        self.display_image(self.filtered_image)

    def bw_action(self):
        self.filtered_image = cv2.cvtColor(
            self.edited_image, cv2.COLOR_BGR2GRAY)
        self.filtered_image = cv2.cvtColor(
            self.filtered_image, cv2.COLOR_GRAY2BGR)
        self.display_image(self.filtered_image)

    def stylisation_action(self):
        self.filtered_image = cv2.stylization(
            self.edited_image, sigma_s=150, sigma_r=0.25)
        self.display_image(self.filtered_image)

    def sketch_action(self):
        ret, self.filtered_image = cv2.pencilSketch(
            self.edited_image, sigma_s=60, sigma_r=0.5, shade_factor=0.02)
        self.display_image(self.filtered_image)

    def emboss_action(self):
        kernel = np.array([[0, -1, -1],
                            [1, 0, -1],
                            [1, 1, 0]])
        self.filtered_image = cv2.filter2D(self.original_image, -1, kernel)
        self.display_image(self.filtered_image)

    def erosion_action(self):
        kernel = np.ones((5, 5), np.uint8)
        self.filtered_image = cv2.erode(
            self.edited_image, kernel, iterations=1)
        self.display_image(self.filtered_image)

    def dilation_action(self):
        kernel = np.ones((5, 5), np.uint8)
        self.filtered_image = cv2.dilate(
            self.edited_image, kernel, iterations=1)
        self.display_image(self.filtered_image)

    def sepia_action(self):
        kernel = np.array([[0.272, 0.534, 0.131],
                            [0.349, 0.686, 0.168],
                            [0.393, 0.769, 0.189]])

        self.filtered_image = cv2.filter2D(self.original_image, -1, kernel)
        self.display_image(self.filtered_image)

    def binary_thresholding_action(self):
        ret, self.filtered_image = cv2.threshold(
            self.edited_image, 127, 255, cv2.THRESH_BINARY)
        self.display_image(self.filtered_image)

    def averaging_action(self, value):
        value = int(value)
        if value % 2 == 0:
            value += 1
        self.filtered_image = cv2.blur(self.edited_image, (value, value))
        self.display_image(self.filtered_image)

    def median_action(self, value):
        value = int(value)
        if value % 2 == 0:
            value += 1
        self.filtered_image = cv2.GaussianBlur(
            self.edited_image, (value, value), 0)
        self.display_image(self.filtered_image)

    def gaussian_action(self, value):
        value = int(value)
        if value % 2 == 0:
            value += 1
        self.filtered_image = cv2.medianBlur(self.edited_image, value)
        self.display_image(self.filtered_image)

    def rotate_left_action(self):
        self.filtered_image = cv2.rotate(
            self.filtered_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        self.display_image(self.filtered_image)

    def rotate_right_action(self):
        self.filtered_image = cv2.rotate(
            self.filtered_image, cv2.ROTATE_90_CLOCKWISE)
        self.display_image(self.filtered_image)

    def vertical_action(self):
        self.filtered_image = cv2.flip(self.filtered_image, 0)
        self.display_image(self.filtered_image)

    def horizontal_action(self):
        self.filtered_image = cv2.flip(self.filtered_image, 2)
        self.display_image(self.filtered_image)
    def brightness_action(self, value):
        self.filtered_image = cv2.convertScaleAbs(
            self.filtered_image, alpha=self.brightness_slider.get())
        self.display_image(self.filtered_image)

    def saturation_action(self, event):
        self.filtered_image = cv2.convertScaleAbs(
            self.filtered_image, alpha=1, beta=self.saturation_slider.get())
        self.display_image(self.filtered_image)

    def display_image(self, image=None):
        # Destroys old canvas widget
        self.canvas.delete("all")

        # Render recent edited image is image is not passed
        if image is None:
            image = self.edited_image.copy()
        else:
            image = image

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channels = image.shape
        ratio = height / width

        new_width = width
        new_height = height

        # if the image size is larger than the canvas, resize it to fit
        if height > self.canvasHeight or width >self.canvasWidth:
            if ratio < 1:
                new_width = self.canvasWidth
                new_height = int(new_width * ratio)
            else:
                new_height = self.canvasHeight
                new_width = int(new_height * (width / height))

        self.ratio = height / new_height
        self.new_image = cv2.resize(image, (new_width, new_height))

        self.new_image = ImageTk.PhotoImage(
            Image.fromarray(self.new_image))

        self.canvas.config(width=new_width, height=new_height)
        self.canvas.create_image(
            new_width / 2, new_height / 2,  image=self.new_image)


root = Tk()
Interface(root)
root.mainloop()
