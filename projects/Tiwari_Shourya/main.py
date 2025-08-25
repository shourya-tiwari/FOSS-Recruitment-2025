# expense_tracker_gui.py
import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Expense Tracker 💰")
    root.geometry("400x300")
    
    label = tk.Label(root, text="Welcome to Expense Tracker 💰", font=("Arial", 14))
    label.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main()