import tkinter as tk


root = tk.Tk()
c=tk.Canvas(root)

c.create_line(0, 100, root.winfo_width(), 100)

c.pack(expand=True, fill=tk.BOTH)



root.mainloop()