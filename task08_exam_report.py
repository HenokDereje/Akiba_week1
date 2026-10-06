# EXAM RESULT REPORT

name = input("Enter your name: ")
python_score = float(input("Enter your Python score: "))
english_score = float(input("Enter your English score: "))
math_score = float(input("Enter your Math score: "))

average_score = (python_score + english_score + math_score) / 3

print("**************************")
print("    EXAM RESULT REPORT") 
print("**************************")
print(f"Student Name: {name}\n")  
print(f"Python Score: {python_score}")
print(f"English Score: {english_score}")
print(f"Math Score: {math_score}")
print("------------------------------")
print(f"Average Score: {average_score}")