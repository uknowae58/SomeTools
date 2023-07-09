import tkinter as tk
from tkinter import filedialog
from Excelserstellung import excel

def select_path():

    path = filedialog.askdirectory()
    if path:
        print(' Pfad des ausgewählten Ordners lautet :', path)
        excel(path)

def select_file():

    path = filedialog.askopenfilename()
    if path:
        print(' Pfad des ausgewählten Ordners lautet :', path)


def get_input_value():
    user_input = input_field.get()
    excel(user_input)
    print(" Pfad des ausgewählten Ordners lautet :", user_input)

window = tk.Tk()
input_field = tk.Entry(window)
input_field.pack()
window.title("graphisches interface")
button = tk.Button(window, text = "Bestätigen Sie!", command=select_path)
input_button = tk.Button(window, text="Récupérer la valeur", command=get_input_value)
inputfile_button = tk.Button(window, text="Récupérer un fichier", command=select_file)
input_button.pack()
button.pack()
inputfile_button.pack()
window.mainloop()

