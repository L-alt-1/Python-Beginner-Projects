# Declare Variables
count = 0  
artist = 0
file = 0

# Try opening the file
try:
    with open("artists.txt", "r") as file:
        # Loop 
        for line in file:
            count += 1 
    print(f"There will be {count} artist(s) performing.")
    
except FileNotFoundError:
    print("File missing.")
    
except IOError:
    print("File unreadable.")
