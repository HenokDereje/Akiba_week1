# ETHIOPIAN SHOPPING RECEIPT

c_name = input("Enter customer name:")  
p_name = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity1 = int(input("Enter product quantity: "))

print("**************************")
print("    SHOPPING RECEIPT")
print("**************************")
print(f"Customer Name: {c_name}")
print(f"Product      price     Qty")
print("------------------------------")
print(f"{p_name}      {price}     {quantity1}")
print(f"Total: {price * quantity1}")