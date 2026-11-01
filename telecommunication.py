usage = float(input("Enter expected data usage: "))
days = int(input("Enter required validity: "))
budget = float(input("Enter budget: "))

n = int(input("Enter number of plans: "))

best_cost = float('inf')
best_plan = ""

for i in range(n):
    name = input("Plan name: ")
    price = float(input("Plan price: "))
    data = float(input("Included data: "))
    validity = int(input("Validity days: "))
    extra_rate = float(input("Extra data charge per GB: "))

    extra = max(0, usage - data)
    total = price + extra * extra_rate

    print("Total cost:", total)

    if validity >= days and total <= budget:
        if total < best_cost:
            best_cost = total
            best_plan = name

if best_plan:
    print("Best Plan:", best_plan)
    print("Total Cost:", best_cost)
else:
    print("No suitable plan found")