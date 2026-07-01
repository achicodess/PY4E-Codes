def computepay(hours, rate):
    if hours > 40:
        regular = 40 * rate
        overtime = (hours - 40) * (rate * 1.5)
        total_pay = regular + overtime
    else:
        total_pay = hours * rate
    return total_pay


# Main program
hrs = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))

finalpayout = computepay(hrs, rate)
print("The pay is:",finalpayout)