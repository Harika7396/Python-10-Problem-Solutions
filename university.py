n = int(input("Enter number of applicants: "))

eligible = []

for i in range(n):
    print("\nApplicant", i + 1)

    name = input("Enter name: ")
    aggregate = float(input("Enter aggregate marks: "))
    subject = float(input("Enter minimum subject marks: "))
    attendance = float(input("Enter attendance: "))
    income = float(input("Enter family income: "))

    if aggregate >= 80 and subject >= 70 and attendance >= 75 and income <= 300000:
        eligible.append([name, aggregate, attendance, income])

eligible.sort(key=lambda x: (-x[1], -x[2], x[3]))

print("\nEligible Students Ranking")

for i, student in enumerate(eligible, 1):
    print(i, student)