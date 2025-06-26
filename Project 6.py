#Declare Variables:
x= 0
y= 0
z= 0
j= 0
p= 0
g= 0

#Input
x= float(input("Enter the length of stick #1: "))
y= float(input("Enter the length of stick #2: "))
z= float(input("Enter the length of stick #3: "))

#Output
if x+z>y and x+y>z and y+z>x:
    print("Triangle Possible")
    if x==y==z:
        print("Equilateral triangle possible")
    elif x==y:
            print("Isosceles triangle possible")
    elif z==y:
            print("Isosceles triangle possible")
    elif x==z:
            print("Isosceles triangle possible")
    else:
            print("Scalene triangle possible")
else:
    print("No Triangle Possible")
