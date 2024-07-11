import tkinter as tk

class FontPainter:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing App")

        self.canvas = tk.Canvas(root, bg="white", width=500, height=500)
        self.canvas.pack()

        self.button = tk.Button(root, text="Save")
        self.button.pack()

        self.button = tk.Button(root, text="Clear", command=self.clear)
        self.button.pack()

        self.canvas.bind("<B1-Motion>", self.paint)

    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_oval(x1, y1, x2, y2, fill="black", width=2)

    def clear(self):
        print("clear")


root = tk.Tk()
app = FontPainter(root)
root.mainloop()
