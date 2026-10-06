# ETHIOPIAN SHOPPING RECEIPT

c_name = input("Enter customer name:")  
p_name1 = input("Enter the first product name: ")
p_name2 = input("Enter the second product name: ")
price = float(input("Enter product price: "))
quantity1 = int(input("Enter the first product quantity: "))
quantity2 = int(input("Enter the second product quantity: "))

print("**************************")
print("    SHOPPING RECEIPT")
print("**************************")
print(f"Customer Name: {c_name}")
print(f"Product      price     Qty")
print("------------------------------")
print(f"{p_name1}      {price}     {quantity1}")
print(f"{p_name2}      {price}     {quantity2}")
print(f"Total: {(price * quantity1) + (price * quantity2)}")