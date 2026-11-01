basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowances: "))
hours = float(input("Enter overtime hours: "))
rate = float(input("Enter overtime rate: "))
incentive = float(input("Enter incentives: "))

overtime = hours * rate

gross = basic + allowance + overtime + incentive

if gross <= 30000:
    tax = gross * 5 / 100
else:
    tax = 30000 * 5 / 100 + (gross - 30000) * 10 / 100

other = float(input("Other deductions: "))

net = gross - tax - other

print("\n----- SALARY SLIP -----")
print("Basic Salary:", basic)
print("Allowances:", allowance)
print("Overtime:", overtime)
print("Incentives:", incentive)
print("Gross Salary:", gross)
print("Tax:", tax)
print("Other Deductions:", other)
print("Net Salary:", net)