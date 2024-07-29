import tkinter as tk
from tkinter import messagebox
import math

# Function to calculate and display factorial
def calculate_factorial():
    try:
        # Get the user input
        n = int(entry.get())
        if n < 0:
            raise ValueError("The number must be non-negative.")
        # Calculate factorial
        result = math.factorial(n)
        # Display the result
        messagebox.showinfo("Factorial Result", f"The factorial of {n} is {result}.")
    except ValueError as e:
        # Handle invalid input
        messagebox.showerror("Invalid Input", str(e))

# Create the main application window
root = tk.Tk()
root.title("Factorial Calculator")

# Create and place the label
label = tk.Label(root, text="Enter an integer:")
label.pack(pady=10)

# Create and place the entry widget
entry = tk.Entry(root)
entry.pack(pady=5)

# Create and place the calculate button
button = tk.Button(root, text="Calculate Factorial", command=calculate_factorial)
button.pack(pady=20)

# Run the application
root.mainloop()
