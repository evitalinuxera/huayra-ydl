import tkinter as tk 
from tkinter import ttk
import os

# Funciones
def bajar():
    os.system("youtube-dl -o ~/Videos/ https://www.youtube.com/watch?v=9_o0TaDnynQ")
    #os.system(f"os {url}")

# Ventana ppal
root = tk.Tk()
root.geometry("600x300")
root.title("Huayra YDL")
root.columnconfigure(0,weight=1)

# Variables
url = tk.StringVar()

# Encabezado
headerFrm = ttk.Frame(root, padding=(20, 10, 20, 30))
headerFrm.grid(row=0, column=0, sticky="EW")

tituloLbl = ttk.Label(headerFrm, text="Huayra-ydl... bajando ansiedades")
tituloLbl.grid(row=0, column=0)


# Entrada
entradaFrm = ttk.Frame(root, padding=(20, 10, 20, 50))
entradaFrm.grid(row=1, column=0, sticky="EW")

urlLabel = ttk.Label(entradaFrm, text="URL del video: ")
urlLabel.grid(row=0, column=0)

urlEnt = ttk.Entry(entradaFrm, width="45", textvariable=url)
urlEnt.grid(row=0, column=1)
urlEnt.focus()

# Botones
botonesFrm = ttk.Frame(root, padding=(20, 10))
botonesFrm.grid(row=2, column=0, sticky="EW")
botonesFrm.columnconfigure(0, weight=1)
botonesFrm.columnconfigure(1, weight=1)

bajarBtn = ttk.Button(botonesFrm, text="Bajar video", command=bajar())
bajarBtn.grid(row=0, column=0, sticky="EW")

salirBtn = ttk.Button(botonesFrm, text="Salir", command=root.destroy)
salirBtn.grid(row=0, column=1, sticky="EW")

# Mainloop
root.mainloop()