#Topic 7 Pratical
#task 6.1
#Declare all variables
food= 0
file= 0
k= 0
x= 0
#Open the file in write mode
file = open("food_festival_menu.txt", "w")

#Input
x= int(input("How many dishes would you like to present?: "))

#Loops and error traps 
for k in range(1, x + 1):
    food = input(f"Enter dish {k}: ")
    while food == "":
        print("Error. Please type a food")
        food = input(f"Enter dish {k}: ")
    file.write(food + "\n")
    
#Close file 
file.close()
print("Data Saved")
