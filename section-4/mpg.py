from random import randint

gallons = randint(10,25)
miles = randint(200,400)

print("The car's MPG is " + str(miles//gallons) + ".")
print("The number of gallons being held in the the car is " + str(gallons) + ".")
print("The number of miles the car traveled is " + str(miles) + ".")