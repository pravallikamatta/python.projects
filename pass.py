import random
print("WELCOME TO THE PASSWORD GENERATOR APP")
letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = list('!@#$%^&*()-_=+[]{}|;:,.<>?/')
all = letters + numbers + symbols

n_letters= int(input("Enter the length of the password: \n"))
n_symbols = int(input("Enter the number of symbols: \n"))
n_numbers = int(input("Enter the number of numbers: \n"))
password_list = [] 
for char in range(n_letters):
    password_list.append(random.choice(letters)) 
for char in range(n_symbols):
    password_list += random.choice(symbols)
for char in range(n_numbers):
    password_list += random.choice(numbers)
random.shuffle(password_list)
password = ''.join(password_list)
print(f"Your password is: {password}")
