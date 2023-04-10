import tkinter as tk

# Create the window
root = tk.Tk()

# Create the color palette
c = tk.Canvas(root, width=200, height=200)
c.pack()

# Create a list of colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white"]

# Create the color picker
for i, color in enumerate(colors):
    x = i * 25
    c.create_rectangle(x, 0, x+25, 25, fill=color, tags=color)

# Set the window background color
def set_background_color(event):
    color = event.widget.find_withtag(tk.CURRENT)[0]
    root.configure(background=colors[color])

c.bind("<Button-1>", set_backgroun_color)



# Run the window
root.mainloop()
