n = int(input("Enter number of products: "))

subtotal = 0

for i in range(n):
    name = input("Product name: ")
    category = input("Category: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    tax = float(input("Tax percentage: "))

    amount = price * quantity
    tax_amount = amount * tax / 100
    total = amount + tax_amount

    subtotal += total

    print(name, "Total:", total)

if subtotal >= 1000:
    discount = min(subtotal * 10 / 100, 150)
else:
    discount = 0

final = subtotal - discount

print("\nSubtotal:", subtotal)
print("Discount:", discount)
print("Final Bill:", final)