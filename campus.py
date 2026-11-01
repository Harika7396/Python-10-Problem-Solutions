venue = float(input("Venue cost: "))
equipment = float(input("Equipment cost: "))
transport = float(input("Transport cost: "))

catering = float(input("Catering per person: "))
certificate = float(input("Certificate per person: "))

participants = int(input("Expected participants: "))

sponsorship = float(input("Sponsorship amount: "))
contribution = float(input("Registration fee per person: "))

fixed = venue + equipment + transport

variable = catering + certificate

total_cost = fixed + variable * participants

income = sponsorship + contribution * participants

shortfall = max(0, total_cost - income)

remaining_per_person = contribution - variable

if remaining_per_person > 0:
    import math
    minimum = max(0, math.ceil((fixed - sponsorship) / remaining_per_person))
else:
    minimum = "Not possible"

print("\n----- EVENT REPORT -----")
print("Fixed Cost:", fixed)
print("Variable Cost:", variable)
print("Total Cost:", total_cost)
print("Total Income:", income)
print("Shortfall:", shortfall)
print("Minimum Registrations:", minimum)