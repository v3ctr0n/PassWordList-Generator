import random

print("")
print("############################")
print("#--------------------------#")
print("#---PassWordlist Creator---#")
print("#--------------------------#")
print("############################")
print("")
print("Created by: v3ctr0n")
print("")
print("Company (1) or a single person (2) ?")
answer = input("Choose 1 or 2: ")

if answer == "1":
        name = input("Name of the company: ")
        othr_name = input("Other name for the company:")
        othr_name2 = input("Other other name: ")
        street = input("Street name: ")
        other1 = input("Other1 : ")
        other2 = input("Other2 : ")
        other3 = input("Other3 : ")

        info_list = [name, othr_name, street, other1, other2, other3,'@', '#', '&', '$', '*', '%', '/', '-', '_', '!', '~', '?', '.', '123', '1234']

        #combines 5 words at most submitted by the user
        for i in range(200):
            print (''.join(random.sample(info_list, random.randint(1,5))))

    

elif answer == "2":
        first_name = input("First name of the person: ")
        surname = input("Surname of the person: ")
        year = input("Year of birth: ")
        id_number = input("National identification number: ")
        family1 = input("Name of a first family member: ")
        family2 = input("Name of a second family member: ")
        family3 = input("Name of a third family member: ")
        pet_name = input("Pet name: ")
        other1 = input("Other1 : ")
        other2 = input("Other2 : ")
        other3 = input("Other3 : ")
        other4 = input("Other4 : ")
    
        info_list = [first_name, surname, year, id_number, family1, family2, family3, pet_name, other1, other2, other3, other4, 
        '@', '#', '&', '$', '*', '%', '/', '-', '_', '!', '~', '?', '.', '123', '1234']

        #combines 5 words at most submitted by the user 
        for i in range(200):
            print (''.join(random.sample(info_list, random.randint(1,5))))

else:
    print("Is typing 1 or 2 so hard?")
