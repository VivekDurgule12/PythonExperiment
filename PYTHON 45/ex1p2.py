def calculate_electricity_bill():
    units = float(input("Enter the number of units consumed: "))

    if units <= 50:
        bill = units * 3.50
    elif units <= 150:
        bill = 50 * 3.50 + (units - 50) * 4.00
    elif units <= 250:
        bill = 50 * 3.50 + 100 * 4.00 + (units - 150) * 5.20
    else:
        bill = 50 * 3.50 + 100 * 4.00 + 100 * 5.20 + (units - 250) * 6.50

    print(f"Electricity Bill: Rs. {bill:.2f}")

calculate_electricity_bill()
