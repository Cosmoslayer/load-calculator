# write your code here
import math


def plural(number):
    if number > 1:
        return 's'
    else:
        return ''


calculate = input("""
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal: 
""")
if calculate == "n":
    principal = int(input("Enter the loan principal: "))
    monthly_payment = int(input("Enter the monthly payment: "))
    interest_rate = float(input("Enter the loan interest: "))
    nominal_interest = (interest_rate / 100) / 12
    x = monthly_payment / (monthly_payment - nominal_interest * principal)
    months = math.ceil(math.log(x, 1 + nominal_interest))
    years = months // 12
    months_left = months % 12
    print(f"It will take {years} year{plural(years)} and {months_left} month{plural(months_left)} to repay this loan!")
elif calculate == "a":
    principal = int(input("Enter the loan principal: "))
    periods = int(input("Enter the number of periods: "))
    interest_rate = float(input("Enter the loan interest: "))
    nominal_interest = (interest_rate / 100) / 12
    annuity = principal * ((nominal_interest * math.pow((1 + nominal_interest), periods)) /
                           (math.pow((1 + nominal_interest), periods) - 1))
    print(f"Your monthly payment = {math.ceil(annuity)}!")
elif calculate == "p":
    annuity = float(input("Enter the annuity payment: "))
    periods = int(input("Enter the number of periods: "))
    interest_rate = float(input("Enter the loan interest: "))
    nominal_interest = (interest_rate / 100) / 12
    principal = annuity / ((nominal_interest * math.pow((1 + nominal_interest), periods)) /
                           (math.pow((1 + nominal_interest), periods) - 1))
    print(f"Your loan principal = {math.floor(principal)}!")
