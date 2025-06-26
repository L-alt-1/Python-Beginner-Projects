#Declare variables
x= 0
y= 0
z= 0

#input


#While loop
while True:
    x=input("Enter your student number or 0 to exit: ")
    if x == "0":
          print(f"Thank you")
          break
    z=0
    for y in str(x):
        z += int(y)
            
    if z%8 ==0:
        print(f"Valid")
        break
    else:
        print(f"Invalid")
    j= int(input("Do you want to enter another student number (1 for yes 2 for no): "))
    if j==2:
        break
