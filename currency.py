budget = float(input("Enter travel budget: "))
fee = float(input("Conversion fee percentage: "))

n = int(input("Number of expense categories: "))

total = 0
largest = 0
largest_category = ""

for i in range(n):
    category = input("Expense category: ")
    amount = float(input("Foreign currency amount: "))
    rate = float(input("Exchange rate: "))

    converted = amount * rate

    converted += converted * fee / 100

    total += converted

    print("Converted amount:", converted)

    if converted > largest:
        largest = converted
        largest_category = category

print("Total Expenses:", total)
print("Largest Expense:", largest_category)

if total <= budget:
    print("Within Budget")
    print("Remaining:", budget - total)
else:
    print("Over Budget")
    print("Extra Amount:", total - budget)