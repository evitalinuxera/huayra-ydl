import tkinter as tk 
from tkinter import ttk
from tkinter.filedialog import askdirectory
import os

root = tk.Tk()
root.title("Huayra - Youtube bajanding")
root.filename = ""

ppal_Frame = ttk.Frame(root, padding=(30, 15))
ppal_Frame.pack()

global path 
path = ""

def archivos():
    path = askdirectory(title = "Seleccionar directorio....", initialdir="~/Videos")
    guardar_path = ttk.Label(ppal_Frame, text=path)
    guardar_path.grid(row=1, column=2)

url_Lbl = ttk.Label(ppal_Frame, text="URL: ", )
url_Ent = ttk.Entry(ppal_Frame, width=32)
soloAudio_Lbl = ttk.Label(ppal_Frame, text="Solo bajar audio")
soloAudio_Chk = ttk.Checkbutton(ppal_Frame, text="")
guardar_Lbl = ttk.Label(ppal_Frame, text="Guardar en ...")
guardar_Ent = ttk.Button(ppal_Frame, text="Elegir...", command=archivos)
bajar_Btn = ttk.Button(ppal_Frame, text="Bajar")


url_Lbl.grid(row=0, column=0, sticky="W")
url_Ent.grid(row=0, column=1, padx=10, pady=10 )
guardar_Lbl.grid(row=1, column=0, sticky="W")
guardar_Ent.grid(row=1, column=1, sticky="W", padx=10, pady=10)
soloAudio_Lbl.grid(row=2, column=0, sticky="W")
soloAudio_Chk.grid(row=2, column=1, sticky="W", padx=10, pady=10)
bajar_Btn.grid(row=3, column=1, columnspan=2, sticky="E", padx=10)



root.mainloop()