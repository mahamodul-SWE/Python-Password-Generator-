#Password Generator in Python:

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the python Password Generator...")

user_letters = int(input("How many letters would you like in your password?\n"))
user_symbols = int(input(f"How many symbols would you like?\n"))
user_numbers = int(input(f"How many numbers would you like?\n"))


new_password = []

for char in range(1, user_letters + 1):
  new_password.append(random.choice(letters))

for char in range(1, user_symbols + 1):
  new_password += random.choice(symbols)

for char in range(1, user_numbers + 1):
  new_password += random.choice(numbers)


print(new_password)
random.shuffle(new_password)
print(new_password)

password = ""
for char in new_password:
  password += char

print(f"Your new password is: {password}")