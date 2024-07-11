import tkinter as tk

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

        self.button = tk.Button(root, text="Save")
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

    # set size function
        
    def setSize(self):
        print(self.slider.get())
        self.brushSize = self.slider.get()

    # paint function

    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_oval(x1, y1, x2, y2, fill="black", width=self.brushSize)

    # clear function

    def clear(self):
        print("clear")
        self.canvas.delete("all")
    
# run application

root = tk.Tk()
app = FontPainter(root)
root.mainloop()
