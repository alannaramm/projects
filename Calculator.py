import tkinter as tk

equation = ""

def add_to_equation(symbol):
    global equation
    equation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, equation)

def solve_equation():
    global equation
    try:
        equation = str(eval(equation))  # Evaluate the equation
        text_result.delete(1.0, "end")
        text_result.insert(1.0, equation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")
        
def clear_field():
    global equation
    equation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("500x300")

# Create a display box 
text_result = tk.Text(root, height=4, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

# Create buttons for the numbers 0-9
button_1 = tk.Button(root, text="1", command=lambda: add_to_equation(1), width=5, font=("Arial", 18))
button_1.grid(row=2, column=0)

button_2 = tk.Button(root, text="2", command=lambda: add_to_equation(2), width=5, font=("Arial", 18))
button_2.grid(row=2, column=1)

button_3 = tk.Button(root, text="3", command=lambda: add_to_equation(3), width=5, font=("Arial", 18))
button_3.grid(row=2, column=2)

button_4 = tk.Button(root, text="4", command=lambda: add_to_equation(4), width=5, font=("Arial", 18))
button_4.grid(row=1, column=0)

button_5 = tk.Button(root, text="5", command=lambda: add_to_equation(5), width=5, font=("Arial", 18))
button_5.grid(row=1, column=1)

button_6 = tk.Button(root, text="6", command=lambda: add_to_equation(6), width=5, font=("Arial", 18))
button_6.grid(row=1, column=2)

button_7 = tk.Button(root, text="7", command=lambda: add_to_equation(7), width=5, font=("Arial", 18))
button_7.grid(row=0, column=0)

button_8 = tk.Button(root, text="8", command=lambda: add_to_equation(8), width=5, font=("Arial", 18))
button_8.grid(row=0, column=1)

button_9 = tk.Button(root, text="9", command=lambda: add_to_equation(9), width=5, font=("Arial", 18))
button_9.grid(row=0, column=2)

button_0 = tk.Button(root, text="0", command=lambda: add_to_equation(0), width=5, font=("Arial", 18))
button_0.grid(row=3, column=1)

# Create +-=* buttons 
button_add = tk.Button(root, text="+", command=lambda: add_to_equation('+'), width=5, font=("Arial", 18))
button_add.grid(row=0, column=3)

button_subtract = tk.Button(root, text="-", command=lambda: add_to_equation('-'), width=5, font=("Arial", 18))
button_subtract.grid(row=1, column=3)

button_multiply = tk.Button(root, text="*", command=lambda: add_to_equation('*'), width=5, font=("Arial", 18))
button_multiply.grid(row=2, column=3)

button_divide = tk.Button(root, text="/", command=lambda: add_to_equation('/'), width=5, font=("Arial", 18))
button_divide.grid(row=3, column=3)

# Clear and equal buttons 
button_clear = tk.Button(root, text="C", command=clear_field, width=5, font=("Arial", 18))
button_clear.grid(row=3, column=0)

button_equals = tk.Button(root, text="=", command=solve_equation, width=5, font=("Arial", 18))  # Corrected function name
button_equals.grid(row=3, column=2)

# Run the application
root.mainloop()
