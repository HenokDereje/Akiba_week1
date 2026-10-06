# TRAVEL PLANNER

destination = input("Enter your travel destination: ")
distance = float(input("Enter the distance to your destination (in km): "))
speed = float(input("Enter your average speed (in km/h): "))

time = distance / speed

print("Destination: ", destination)
print("Distance: ", distance)
print("Speed: ", speed)
print(f"Estimated Travel Time: {time} hours")


