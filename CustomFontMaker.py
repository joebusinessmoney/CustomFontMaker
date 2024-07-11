import tkinter as tk
import PIL
from PIL import Image, ImageDraw
from tkinter import filedialog

class FontPainter:
    brushSize = 7

    def __init__(self, root):
        
        # create window

        self.root = root
        self.root.title("Drawing App")

        # create canvas

        self.canvas = tk.Canvas(root, bg="white", width=500, height=500)
        self.canvas.pack()

        # create widgets used for saving, clearing and changing brush stize

        self.button = tk.Button(root, text="Save", command=self.save)
        self.button.pack()

        self.button = tk.Button(root, text="Clear", command=self.clear)
        self.button.pack()

        self.slider = tk.Scale(root, from_=1, to=50, orient="horizontal")
        self.slider.set(7) #default brush size
        self.slider.pack()

        self.button = tk.Button(root, text="Set brush size", command=self.setSize)
        self.button.pack()

        # bind mouse movement to paint function

        self.canvas.bind("<B1-Motion>", self.paint)

        # create image to draw on

        self.image = Image.new("RGB", (500, 500), "white")
        self.draw = ImageDraw.Draw(self.image)

    # set size function
        
    def setSize(self):
        print(self.slider.get())
        self.brushSize = self.slider.get()

    # paint function

    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_oval(x1, y1, x2, y2, fill="black", width=self.brushSize)
        self.draw.circle([x1, y1, x2, y2], fill="black", outline="black", radius=self.brushSize)

    # clear function

    def clear(self):
        print("clear")
        self.canvas.delete("all")
        self.image = Image.new("RGB", (500, 500), "white")
        self.draw = ImageDraw.Draw(self.image)

    # save function

    def save(self):
        filePath = filedialog.asksaveasfilename(defaultextension=".png")
        if filePath:
            self.image.save(filePath)
    
# run application

root = tk.Tk()
app = FontPainter(root)
root.mainloop()
