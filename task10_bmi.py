# BMI HEALTH INFORMATION

name = input("Enter your name: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print("============== BMI REPORT =======")
print("Name: ", name)
print("Weight: ", weight, "kg") 
print("Height: ", height, "m")
print("BMI: ", bmi)