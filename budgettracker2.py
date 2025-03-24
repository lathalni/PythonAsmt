import matplotlib.pyplot as plt
import csv

# Input Annual Net Income
annual_net_income = float(input("Enter your annual net income (NZD): "))
monthly_income = round(annual_net_income / 12, 2)
print(f"Your monthly income is: {monthly_income} NZD")

months = []
monthly_expenses = []
monthly_savings = []

num_months = int(input("\nHow many months do you want to track? "))

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
    
    savings = round(monthly_income - total_expense, 2)
    monthly_savings.append(savings)
    
    print(f"Total expense for {month}: {total_expense} NZD")
    print(f"Savings for {month}: {savings} NZD")

# Save data to CSV
with open('monthly_budget_tracker.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Month', 'Total Expenses', 'Savings'])
    for month, expense, savings in zip(months, monthly_expenses, monthly_savings):
        writer.writerow([month, expense, savings])

# Plotting Monthly Expenses
plt.figure(figsize=(10, 6))
plt.bar(months, monthly_expenses, color='coral', label='Expenses')
plt.plot(months, monthly_savings, marker='o', color='green', label='Savings')
plt.title('Monthly Expenses and Savings Overview')
plt.xlabel('Month')
plt.ylabel('Amount in NZD')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()

# Show Total Yearly Savings if user wants
choice = input("\nDo you want to see total savings over the year? (yes/no): ").lower()
if choice == 'yes':
    total_yearly_savings = sum(monthly_savings)
    print(f"\nTotal Savings over {num_months} months: {total_yearly_savings} NZD")
else:
    print("Okay! Thank you for using the budget tracker.")
