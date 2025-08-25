import tkinter as tk
import json
import os

FILE = "expenses.json"
expenses = []

def load_expenses():
    global expenses
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            expenses = json.load(f)

def save_expenses():
    with open(FILE, "w") as f:
        json.dump(expenses, f)

def add_expense():
    try:
        amount = float(amount_entry.get())
        category = category_entry.get()
        expenses.append({"amount": amount, "category": category})
        save_expenses()
        view_expenses()
        status_label.config(text=f"✅ Added {category}: ₹{amount}")
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
    except ValueError:
        status_label.config(text="⚠️ Enter a valid amount!")

def view_expenses():
    expense_list.delete(0, tk.END)
    for exp in expenses:
        expense_list.insert(tk.END, f"₹{exp['amount']} - {exp['category']}")

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x500")

tk.Label(root, text="Amount (₹):").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Category:").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=10)
tk.Button(root, text="View Expenses", command=view_expenses).pack(pady=10)

expense_list = tk.Listbox(root, width=40, height=8)
expense_list.pack()

status_label = tk.Label(root, text="Ready", fg="blue")
status_label.pack(pady=10)

load_expenses()
view_expenses()

root.mainloop()
