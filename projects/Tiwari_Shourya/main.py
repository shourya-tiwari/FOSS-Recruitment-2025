import tkinter as tk

expenses = []

def add_expense():
    amount = amount_entry.get()
    category = category_entry.get()
    
    if amount and category:
        expenses.append({"amount": float(amount), "category": category})
        status_label.config(text=f"✅ Added: ₹{amount} ({category})")
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
    else:
        status_label.config(text="⚠️ Please fill all fields!")

root = tk.Tk()
root.title("Expense Tracker 💰")
root.geometry("400x300")

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
