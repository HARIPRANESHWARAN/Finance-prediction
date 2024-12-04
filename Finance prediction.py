import pandas as pd
import matplotlib.pyplot as plt

# Sample transaction data (replace with real data or load from a file)
data = {
    'Date': ['2024-11-01', '2024-11-05', '2024-11-10', '2024-11-15', '2024-11-20'],
    'Description': ['Grocery', 'Electricity Bill', 'Online Shopping', 'Dining Out', 'Salary'],
    'Amount': [-50, -100, -150, -80, 1000],
    'Category': ['Groceries', 'Utilities', 'Shopping', 'Entertainment', 'Income']
}

# Create a DataFrame
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Calculate total income and expenses
income = df[df['Amount'] > 0]['Amount'].sum()
expenses = df[df['Amount'] < 0]['Amount'].sum()
savings = income + expenses

# Categorize expenses
expense_data = df[df['Amount'] < 0].groupby('Category')['Amount'].sum()

# Display the analysis
print("==== Personal Finance Analysis ====")
print(f"Total Income: ${income:.2f}")
print(f"Total Expenses: ${abs(expenses):.2f}")
print(f"Savings: ${savings:.2f}\n")
print("Expenses by Category:")
print(expense_data)

# Plot the expense breakdown
expense_data.plot(kind='bar', title="Expenses by Category", ylabel="Amount ($)", xlabel="Category", color='orange')
plt.show()
