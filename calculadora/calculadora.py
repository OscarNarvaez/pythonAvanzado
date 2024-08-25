import tkinter as tk

def click(event):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + event.widget.cget("text"))

def clear():
    entry.delete(0, tk.END)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculadora")

entry = tk.Entry(root, width=10, font=('Arial', 24), borderwidth=5, relief="groove")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        btn = tk.Button(root, text=button, width=4, height=2, font=('Arial', 18), command=evaluate)
    elif button == "C":
        btn = tk.Button(root, text=button, width=4, height=2, font=('Arial', 18), command=clear)
    else:
        btn = tk.Button(root, text=button, width=4, height=2, font=('Arial', 18))
        btn.bind("<Button-1>", click)
    
    btn.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()


