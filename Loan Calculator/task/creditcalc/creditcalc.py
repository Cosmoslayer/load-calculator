# write your code here
import math

interest = 0
principal = int(input("Enter the loan principal: "))
calculate = input("""
What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:
""")
if calculate == "m":
    monthly_payment = int(input("Enter the monthly payment: "))
    months = math.ceil(principal / monthly_payment)
    print(f"It will take {months} month{'s'if months > 1 else ' '} to repay the loan")
elif calculate == "p":
    months = int(input("Enter the number of months: "))
    payment = math.ceil(principal / months)
    last_payment = principal - ((months - 1) * payment)
    print(f"Your monthly payment = {payment} and the last payment = {last_payment}.")
