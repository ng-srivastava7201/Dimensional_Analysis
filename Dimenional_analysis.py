import tkinter as tk
import mysql.connector as sql

d = sql.connect(host='localhost', user='root', password='family123')
cr = d.cursor()

window = tk.Tk()
window.title("Dimensional Analysis")
window.geometry("1547x650")
window.config(bg='#C1D7C9')

Title = tk.Label(window, text='DIMENSIONAL-ANALYSIS', bg='#C1D7C9', fg='#2F2F2F', font=('bold', 30))
Title.pack(side = tk.TOP, fill = tk.X)

textLable = tk.Label(window, text='Enter the formula', bg='#C1D7C9', fg='#2F2F2F', font=('bold', 30))
textLable.pack()

Dimensions = {"M": "Mass", "L" : "Length", "T" : "Time", "ɵ" : "Temperature" ,"I" : "Current", "N" : "Amount of Substance", "J" : "Luminous Intensity"}
input_dimensions = {"kg" : "Mass", "m" : "Length", "sec" : "Time", "K" : "Temperature", "A" : "Current", "mol" : "Amount of Substance", "cd": "Luminous Intensity"}

text_output = "\n".join([f"{key} : {value}" for key, value in Dimensions.items()])

Dimension_Label = tk.Label(window, text=text_output ,bg='#C1D7C9', fg='#1D3557', font=('bold', 30))
Dimension_Label.pack()
e = tk.Entry(window)
e.pack()
window.mainloop()