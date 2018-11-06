import random

print('''
Nocwing Password Generator v0.1
-------------------------------
''')

alpha_numeric = "abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789"
with_special_chars = alpha_numeric + "!@#$%^&*"

num_of_passwords = input("How many passwords do you need?\n: ")
num_of_passwords = int(num_of_passwords)
num_of_chars = input("How long do you want the passwords to be?\n: ")
num_of_chars = int(num_of_chars)
use_special = input("Do you want to use special characters?\n(yes/no): ")

print("Here are your passwords!\n")

for pwd in range(num_of_passwords):
    password = ""
    if use_special.lower() == "yes":
        for chars in range(num_of_chars):
            password += random.choice(with_special_chars)
    else:
        for chars in range(num_of_chars):
            password += random.choice(alpha_numeric)
    print(password)
# print('''
# All done!
# ---------
# ''')
# input("Press [Enter] to exit...")
