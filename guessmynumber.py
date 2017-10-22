low = 0
high = 100
print("Please think of a number between 0 and 100!")

while True:
    print("Is your secret number ", int((low+high)/2), "?" )
    check = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guess correctly.")
    if check == 'l':
        low = int((low+high)/2)
    elif check == 'h':
        high = int((low+high)/2)
    elif check == 'c':
        print("Game over. Your secret number was:", int((low+high)/2))
        break
    else:
        print("Wrong input. Please indicate high, low or correct")
