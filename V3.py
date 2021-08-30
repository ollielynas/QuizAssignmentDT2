import tkinter as tk
import json

root = tk.Tk()
c=tk.Canvas(root)

Q_and_A = json.load(open("famousPersonv2.json", "r", encoding="utf-8"))


c.pack(expand=True, fill=tk.BOTH)



root.mainloop()