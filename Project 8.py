#Declare variables
N= 0
y= 0
z= 0

#input
N=int(input("Enter a number: "))

#For loop
for y in range(1,N):
    if N%y ==0:
        z += y
if z==N:
    print(f"{N} is a perfect number.")
else:
    print(f'{N} is not a perfect number')
