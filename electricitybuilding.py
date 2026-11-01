n = int(input("Enter number of months: "))

previous_bill = 0

for i in range(n):
    units = float(input("Enter units consumed: "))

    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    bill += 50
    bill += bill * 5 / 100

    if units <= 100:
        bill -= bill * 10 / 100

    print("Electricity Bill: Rs.", round(bill, 2))

    if previous_bill > 0:
        increase = (bill - previous_bill) / previous_bill * 100

        if increase > 20:
            print("Unusual increase detected!")

    previous_bill = bill