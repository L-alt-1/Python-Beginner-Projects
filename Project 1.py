
#Declare variables
x= 0
y= 0
kWh= 0

#Input
x= float(input("Enter the appliance ower in watts (W): "))
y= int(input("Enter the duration the appliance is used in hours: "))

#Calculation
kWh= (x*y)/1000

#Output
print("Energy consumption: ", kWh, "kWh")
