import random
# Loop
# Ask: rall the dice?
while True:
    choice =  input("Roll the dice? (y/n): ").lower()
    if choice == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"You rolled a {die1} and a {die2}.")
    elif choice == "n":
        print("Thank you for playing!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

# Generate two random  numbers
#prnt then
# If both numbers enters n
# print thank you message l
#else
# print the numbers and ask again