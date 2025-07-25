# Emi Calculator 

car_price = 1753690.00
car_down_payment = 160000
bank_interest_rate = 9.0
loan_period_years = 5

# Loan Calculator 

loan_amount = car_price - car_down_payment
loan_months = loan_period_years * 12
monthly_interest_rate = bank_interest_rate / (12*100)

# Emi formula 
emi = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** loan_months) / \
((1 + monthly_interest_rate) ** loan_months - 1)

# calculations 

total_payment = emi*loan_months
total_interest = total_payment - loan_amount


print(f"on-road price : {car_price }")
print(f"down payment : {car_down_payment }")
print(f"loan amount {loan_amount }")
print(f"bank interest : {bank_interest_rate }")
print(f"loan period : {loan_period_years }")
print(f"monthly interest : {monthly_interest_rate }")
print(f"monthly emi : {emi }")
print(f"total payment : {total_payment }")
print(f"total interest : {total_interest }")