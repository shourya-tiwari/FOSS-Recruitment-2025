import csv
import tkinter as tk

FILE_NAME = "expenses.csv"
expenses = []

def load_expenses():
    try:
        with open(FILE_NAME, newline="") as file:
            reader = csv.DictReader(file)
            return [{"amount": float(row["amount"]), "category": row["category"]} for row in reader]
    except FileNotFoundError:
        return []

def save_expenses():
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["amount", "category"])
        writer.writeheader()
        writer.writerows(expenses)

def add_expense():
    amount = amount_entry.get()
    category = category_entry.get()
    
    if amount and category:
        expenses.append({"amount": float(amount), "category": category})
        save_expenses()
        status_label.config(text=f"✅ Added: ₹{amount} ({category})")
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
    else:
        status_label.config(text="⚠️ Please fill all fields!")

root = tk.Tk()
root.title("Expense Tracker 💰")
root.geometry("400x300")

expenses = load_expenses()

tk.Label(root, text="Amount:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Category:").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
