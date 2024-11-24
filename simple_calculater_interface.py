import tkinter as tk
from tkinter import messagebox


def click(event):
    global entry_text
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry_text.get())
            entry_text.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif text == "Clear":
        entry_text.set("")
    else:
        entry_text.set(entry_text.get() + text) 

# Create main application window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display numbers and results
entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, font=("Arial", 20), justify="right", bd=5)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, padx=10, pady=10)

# Calculator buttons layout
buttons = [
    ["1", "2", "3", "+"],
    ["4", "5", "6", "-"],
    ["7", "8", "9", "*"],
    ["0", ".", "Clear", "="],
    ["", "", "", "/"]
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text:  # Only create buttons for non-empty cells
            button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2)
            button.grid(row=i + 1, column=j, padx=5, pady=5)
            button.bind("<Button-1>", click)

# Run the application
root.mainloop()