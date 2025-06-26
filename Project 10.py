 #Declare Variables
test_scores = 0
total= 0
count= 0
Average = 0
grade= 0

#Function 1
def calcAverage(total,count):
    Average= total/5
    return Average

#Function 2
def determineGrade(Average):
    if 90<= Average <=100:
        grade= "A"
    elif 80<= Average <=89:
        grade= "B"
    elif 70<= Average <=79:
        grade= "C"
    elif 60<= Average <=69:
        grade= "D"
    else:
        grade= "F"
    return grade
        
#Output
def main():
    count= 1
    total= 0
    while count <= 5:
        test_scores= float(input(f"Enter test score {count}: "))
        total+= test_scores
        count+= 1
    Average= calcAverage(total, 5)
    grade= determineGrade(Average)
    print(f"Your average test score is {Average:.2f}% and thus your grade is {grade}")


# Demonstration
if __name__ == "__main__":
    main()
