#Declare variables
x= 0
y= 0
BMI= 0

#Input
x= float(input("Enter your weight in kilograms (kg): "))
y= int(input("Enter your height in centimeres (cm): "))

#Convert height from cm to m
m= y/100
#Calculate BMI
BMI= x/(m**2)

#Output
print("BMI: ", BMI)
