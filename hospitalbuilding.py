consultation = float(input("Consultation charge: "))
diagnostic = float(input("Diagnostic charge: "))
treatment = float(input("Treatment charge: "))
paid = float(input("Amount paid: "))

if min(consultation, diagnostic, treatment, paid) < 0:
    print("Invalid charges")
else:
    total = consultation + diagnostic + treatment

    if total >= 5000:
        discount = total * 10 / 100
    else:
        discount = 0

    final_bill = total - discount
    balance = final_bill - paid

    print("Total Bill:", total)
    print("Discount:", discount)
    print("Final Bill:", final_bill)
    print("Balance:", balance)

    if paid >= final_bill:
        print("Fully Paid")
    elif paid > 0:
        print("Partially Paid")
    else:
        print("Unpaid")