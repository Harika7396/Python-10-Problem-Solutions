quantity = int(input("Enter quantity: "))
material = float(input("Material cost per unit: "))
wastage = float(input("Wastage percentage: "))
labour = float(input("Labour cost: "))
machine = float(input("Machine cost: "))
selling = float(input("Selling price per unit: "))
target = float(input("Target profit percentage: "))

material_cost = quantity * material

wastage_cost = material_cost * wastage / 100

total_cost = material_cost + wastage_cost + labour + machine

revenue = quantity * selling

profit = revenue - total_cost

profit_percent = profit / total_cost * 100

print("Total Cost:", total_cost)
print("Revenue:", revenue)
print("Profit:", profit)
print("Profit Percentage:", profit_percent)

if profit_percent >= target:
    print("Target Profit Achieved")
else:
    print("Target Profit Not Achieved")