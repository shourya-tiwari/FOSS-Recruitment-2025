import tkinter as tk
import json
import os
from collections import defaultdict
from tkinter import messagebox

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

def show_summary():
    if not expenses:
        messagebox.showinfo("Summary", "No expenses recorded yet.")
        return

    total = sum(exp["amount"] for exp in expenses)
    summary_text = f"💡 Total Spent: ₹{total}\n\n"

    categories = defaultdict(float)
    for exp in expenses:
        categories[exp["category"]] += exp["amount"]

    summary_text += "📊 Spending by Category:\n"
    for cat, amt in categories.items():
        summary_text += f"{cat}: ₹{amt}\n"

    messagebox.showinfo("Expense Summary", summary_text)

def delete_expense():
    selected = expense_list.curselection()
    if not selected:
        status_label.config(text="⚠️ Select an expense to delete!")
        return
    idx = selected[0]
    removed = expenses.pop(idx)
    save_expenses()
    view_expenses()
    status_label.config(text=f"🗑️ Removed {removed['category']} - ₹{removed['amount']}")

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x550")

tk.Label(root, text="Amount (₹):").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Category:").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=10)
tk.Button(root, text="View Expenses", command=view_expenses).pack(pady=10)
tk.Button(root, text="Show Summary", command=show_summary).pack(pady=10)
tk.Button(root, text="Delete Selected", command=delete_expense).pack(pady=10)

expense_list = tk.Listbox(root, width=40, height=8)
expense_list.pack()

status_label = tk.Label(root, text="Ready", fg="blue")
status_label.pack(pady=10)

load_expenses()
view_expenses()

root.mainloop()
