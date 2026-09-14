def birthday_wish(name):
    print("Happy Birthday,", name + "!")
    print("May you have a wonderful day!")


def new_year_wish(name):
    print("Happy New Year,", name + "!")
    print("Wishing you happiness and success!")


def festival_wish(name):
    print("Happy Festival,", name + "!")
    print("Have a joyful celebration!")


name = input("Enter your name: ")

print("\nChoose a wish:")
print("1. Birthday Wish")
print("2. New Year Wish")
print("3. Festival Wish")

choice = int(input("Enter your choice: "))

if choice == 1:
    birthday_wish(name)

elif choice == 2:
    new_year_wish(name)

elif choice == 3:
    festival_wish(name)

else:
    print("Invalid choice")