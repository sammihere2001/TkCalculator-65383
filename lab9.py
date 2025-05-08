import tkinter as tk
from tkinter import messagebox
import math

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get()) if entry2.get() else 0  # default 0 for unary ops

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        elif operation == "Square":
            result = num1 ** 2
        elif operation == "Square Root":
            if num1 < 0:
                raise ValueError("Cannot take square root of negative number")
            result = math.sqrt(num1)

        result_label.config(text=f"Result: {round(result, 2)}")
    except ValueError as ve:
        messagebox.showerror("Input Error", f"Invalid input: {ve}")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")

# GUI setup
window = tk.Tk()
window.title("Advanced Calculator")
window.geometry("400x370")
window.resizable(False, False)

tk.Label(window, text="Advanced Calculator", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(window)
frame.pack(pady=10)

tk.Label(frame, text="Number 1:").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(frame, width=15)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Number 2:").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(frame, width=15)
entry2.grid(row=1, column=1, padx=5, pady=5)

btn_frame = tk.Frame(window)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", width=10, bg="#4CAF50", fg="white", command=lambda: calculate("Add")).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Subtract", width=10, bg="#f44336", fg="white", command=lambda: calculate("Subtract")).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Multiply", width=10, bg="#2196F3", fg="white", command=lambda: calculate("Multiply")).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Divide", width=10, bg="#FF9800", fg="white", command=lambda: calculate("Divide")).grid(row=1, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Square", width=10, bg="#9C27B0", fg="white", command=lambda: calculate("Square")).grid(row=2, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Square Root", width=10, bg="#009688", fg="white", command=lambda: calculate("Square Root")).grid(row=2, column=1, padx=5, pady=5)

result_label = tk.Label(window, text="Result:", font=("Arial", 12))
result_label.pack(pady=10)

window.mainloop()
