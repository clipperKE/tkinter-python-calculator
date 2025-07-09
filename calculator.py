import tkinter as tk

# main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("335x460")
root.resizable(False, False)

# display expressions
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=10, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Global expression variable
expression = ""

# Function to update the entry field
def press(num):
    global expression
    expression += str(num)
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

# Function to evaluate the expression
def equal():
    global expression
    try:
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = result
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        expression = ""

# Function to clear the entry field
def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

# Button texts arranged in a grid
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create and place buttons on the window
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), bg="#4CAF50", fg="white", command=equal)
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=lambda t=text: press(t))
    btn.grid(row=row, column=col, sticky="nsew")

# Clear button
clear_btn = tk.Button(root, text="C", padx=20, pady=20, font=('Arial', 18), bg="#f44336", fg="white", command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, sticky="nsew", pady=5)

# Run the main event loop
root.mainloop()
