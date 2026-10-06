# EMPLOYEE PAYSLIP

name = input("Enter employee name: ")
salary = float(input("Enter employee salary:  "))
transport_allowance = float(input("Enter transport allowance: "))
food_allowance = float(input("Enter food allowance: "))

gross = salary + transport_allowance + food_allowance

print("**************************")
print("    EMPLOYEE PAYSLIP")
print("**************************")
print(f"Employee Name: {name}")
print(f"Basic Salary: {salary}")
print(f"Transport Allowance: {transport_allowance}")
print(f"Food Allowance: {food_allowance}")
print("------------------------------")
print(f"Gross Salary: {gross}")
