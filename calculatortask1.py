import tkinter as tk

# Function to handle button click and append numbers or operators
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

# Function to evaluate the expression
def evaluate():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        animate_result(result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the display
def clear():
    entry.delete(0, tk.END)

# Animation for showing the result (typing effect)
def animate_result(result):
    current_text = ""
    def animate():
        nonlocal current_text
        if len(current_text) < len(result):
            current_text += result[len(current_text)]
            entry.delete(0, tk.END)
            entry.insert(tk.END, current_text)
            root.after(100, animate)  # Update every 100ms for typing effect
    animate()

# Button click animation (Button color change effect)
def animate_button(button):
    original_bg = button.cget('bg')
    button.config(bg="#3a3a3a")  # Darker grey when clicked
    root.after(100, lambda: button.config(bg=original_bg))  # Reset after 100ms

# Create the main window (root) with black background
root = tk.Tk()
root.title("Black-Themed Animated Calculator")
root.geometry("400x600")
root.config(bg="#1e1e1e")  # Set background to dark black

# Entry widget for displaying the calculation and result
entry = tk.Entry(root, font=("Arial", 24), width=15, borderwidth=2, relief="solid", bg="#222222", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Button layout (numbers and operators)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Create buttons with styles and add click animations
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, bg="#4c4c4c", fg="white", command=evaluate)
    elif text == "C":
        button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, bg="#ff4747", fg="white", command=clear)
    else:
        button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, bg="#333333", fg="white", command=lambda t=text: button_click(t))
    
    # Add click animation to buttons
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", lambda event, b=button: animate_button(b))  # Button click animation

# Start the Tkinter event loop
root.mainloop()
