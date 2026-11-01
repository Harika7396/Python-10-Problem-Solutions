distance = float(input("Enter distance: "))
multiplier = float(input("Enter class multiplier: "))
reservation = float(input("Reservation fee: "))

n = int(input("Number of passengers: "))

for i in range(n):
    name = input("Passenger name: ")
    age = int(input("Passenger age: "))

    if distance <= 100:
        fare = distance * 1
    elif distance <= 500:
        fare = 100 + (distance - 100) * 0.8
    else:
        fare = 100 + 400 * 0.8 + (distance - 500) * 0.6

    fare = fare * multiplier

    if age >= 60:
        fare = fare - fare * 20 / 100

    fare += reservation

    print("Ticket Fare:", fare)

    cancel = input("Cancel ticket? (yes/no): ")

    if cancel == "yes":
        penalty = fare * 25 / 100
        print("Cancellation Penalty:", penalty)
        print("Refund:", fare - penalty)