import tkinter as tk
from tkinter import messagebox
ventana = tk.Tk()
ventana.title("ejemplo listBox")
sintonasLabel=tk.Label(ventana, text="Sintonas")
sintonasLabel.grid(row=0, column=0, padx=5, pady=5, sticky="w")
#crear listBox
lista =tk. Listbox(ventana, selectmode=tk.SINGLE)
lista.insert(1, "dolor de cabeza")
lista.insert(2, "Fiebre")
lista.insert(3, "tos ")
lista.insert(4, "Fatiga")
lista.insert(5, "Dificultad al Respirar")
lista.grid(row=0, column=1, pady=10, sticky="we")
#boton para mostrar seleccion
def mostrar():
    seleccionado= lista.get(lista.curselection())
    tk.messagebox.showinfo("mostrar seleccion",comand=mostrar)
boton=tk.Button(ventana, text="mostrar seleccion", command=mostrar)
boton.grid(row=1, column=0, padx=10, pady=10)
ventana.mainloop()
