import matplotlib.pyplot as plt
import csv

months = []
monthly_expenses = []

num_months = int(input("How many months do you want to track? "))

for i in range(num_months):
    print(f"\n--- Month {i+1} ---")
    month = input("Enter month name: ")
    months.append(month)
    
    rent = float(input('Enter rent: '))
    electricity = float(input('Enter electricity expense: '))
    gas = float(input('Enter gas expense: '))
    medical = float(input('Enter medical expenses: '))
    groceries = float(input('Enter groceries expenses: '))
    petrol = float(input('Enter petrol expense: '))
    dineout = float(input('Enter dineout expenses: '))
    misc = float(input('Enter miscellaneous expenses: '))
    
    total_expense = rent + electricity + gas + medical + groceries + petrol + dineout + misc
    monthly_expenses.append(total_expense)
    print(f"Total expense for {month}: {total_expense}")

# Save data to CSV (optional)
with open('monthly_budget_tracker.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Month', 'Total Expenses'])
    for month, expense in zip(months, monthly_expenses):
        writer.writerow([month, expense])

# Plotting months vs expenses
plt.figure(figsize=(10, 6))
plt.bar(months, monthly_expenses, color='coral')
plt.title('Monthly Expenses Overview')
plt.xlabel('Month')
plt.ylabel('Total Expenses (NZD)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
