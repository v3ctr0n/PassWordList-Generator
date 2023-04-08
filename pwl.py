import random
import string

print( '''

╔═══╗             ╔╗╔╗╔╗         ╔╗╔╗          ╔╗     
║╔═╗║             ║║║║║║         ║║║║         ╔╝╚╗    
║╚═╝║╔══╗ ╔══╗╔══╗║║║║║║╔══╗╔═╗╔═╝║║║   ╔╗╔══╗╚╗╔╝    
║╔══╝╚ ╗║ ║══╣║══╣║╚╝╚╝║║╔╗║║╔╝║╔╗║║║ ╔╗╠╣║══╣ ║║     
║║   ║╚╝╚╗╠══║╠══║╚╗╔╗╔╝║╚╝║║║ ║╚╝║║╚═╝║║║╠══║ ║╚╗    
╚╝   ╚═══╝╚══╝╚══╝ ╚╝╚╝ ╚══╝╚╝ ╚══╝╚═══╝╚╝╚══╝ ╚═╝    
        GENERATOR by v3ctr0n
        
''')

special_char = ['@', '#', '&', '$', '*', '%', '!', '~', '?', '123']

def generate_passwords(num_passwords, info_list, include_special_chars=False, capitalize_words=False):
    passwords = []
    for i in range(num_passwords):
        password = ""
        random.shuffle(info_list)  # Shuffle the list before generating each password
        for word in info_list:
            if capitalize_words and random.random() < 0.5:
                word = word.capitalize()
            password += word
        if include_special_chars:
            password += ''.join(random.choices(special_char, k=random.randint(1, 3)))
        passwords.append(password)
    return passwords

# Get user input
info_list = []
while True:
    info = input("Enter a piece of information to use for password generation (press enter to finish): ")
    if not info:
        break
    info_list.append(info)
num_passwords = int(input("Enter the number of passwords to generate: "))
include_special_chars = input("Include special characters? (Y/N)").lower() == "y"
capitalize_words = input("Randomly capitalize words? (Y/N)").lower() == "y"

passwords = generate_passwords(num_passwords, info_list, include_special_chars, capitalize_words)

# Write passwords to file
with open('passwords.txt', 'w') as f:
    for password in passwords:
        f.write(password + '\n')
        
# Print success message
print(f"{len(passwords)} passwords generated and saved to passwords.txt")
