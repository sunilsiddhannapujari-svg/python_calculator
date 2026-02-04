import tkinter as tk
import math

# ---------- Functions ----------
def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def equal():
    try:
        expr = entry.get()
        result = eval(expr)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def sqrt():
    try:
        value = float(entry.get())
        clear()
        entry.insert(tk.END, math.sqrt(value))
    except:
        entry.insert(tk.END, "Error")

def trig(func):
    try:
        value = eval(entry.get())  # allows 45+5
        value = float(value)
        clear()

        if func == "sin":
            entry.insert(tk.END, math.sin(math.radians(value)))
        elif func == "cos":
            entry.insert(tk.END, math.cos(math.radians(value)))
        elif func == "tan":
            entry.insert(tk.END, math.tan(math.radians(value)))

    except Exception:
        clear()
        entry.insert(tk.END, "Error")

def log():
    try:
        value = float(entry.get())
        clear()
        entry.insert(tk.END, math.log10(value))
    except:
        entry.insert(tk.END, "Error")

# ---------- Window ----------
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("350x500")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 22), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10, sticky="nsew")

# ---------- Button layout ----------
buttons = [
    ('√', sqrt), ('sin', lambda: trig("sin")), ('cos', lambda: trig("cos")), ('tan', lambda: trig("tan")),
    ('log', log), ('C', clear), ('(', lambda: press("(")), (')', lambda: press(")")),

    ('7', lambda: press('7')), ('8', lambda: press('8')), ('9', lambda: press('9')), ('/', lambda: press('/')),
    ('4', lambda: press('4')), ('5', lambda: press('5')), ('6', lambda: press('6')), ('*', lambda: press('*')),
    ('1', lambda: press('1')), ('2', lambda: press('2')), ('3', lambda: press('3')), ('-', lambda: press('-')),
    ('0', lambda: press('0')), ('.', lambda: press('.')), ('=', equal), ('+', lambda: press('+')),
]

row = 1
col = 0

for text, cmd in buttons:
    tk.Button(root, text=text, font=("Arial", 14), width=6, height=2,
              command=cmd).grid(row=row, column=col, padx=3, pady=3)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()

