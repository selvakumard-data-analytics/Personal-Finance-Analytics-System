import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("data/finance_data.csv")

# Display Data
print("Finance Data:")
print(df)

# Total Income
income = df[df["Type"] == "Income"]["Amount"].sum()
print("\nTotal Income:")
print(income)

# Total Expense
expense = df[df["Type"] == "Expense"]["Amount"].sum()
print("\nTotal Expense:")
print(expense)

# Savings
savings = income - expense
print("\nSavings:")
print(savings)

# Savings Rate
savings_rate = (savings / income) * 100
print("\nSavings Rate:")
print(round(savings_rate, 2), "%")

# Category Wise Expense
category_expense = df[df["Type"] == "Expense"].groupby("Category")["Amount"].sum()

print("\nCategory Wise Expense:")
print(category_expense)

# Bar Chart
category_expense.plot(kind="bar")
plt.title("Category Wise Expenses")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.savefig("bar_chart.png")
plt.show()

# Pie Chart
category_expense.plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(6,6)
)

plt.title("Expense Distribution")
plt.ylabel("")
plt.savefig("expense_distribution.png")
plt.show()