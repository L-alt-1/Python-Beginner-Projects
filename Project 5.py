#Declare Variables:
x= 0

#Input
x= float(input("Enter a temperature (in Celcius): "))

#Output
if x<0:
    print("The temperature is Freezing Cold")
elif x<=10:
    print("The temperature is Cold")
elif x<=20:
    print("The temperature is Cool")
elif x<=30:
    print("The temperature is Warm")
else:
    print("The temperature is Scorching")
