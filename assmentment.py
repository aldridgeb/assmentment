import random

def get_name():
    name_local = input("what is your name: ")
    return name_local


def get_age():
    age_local = int(input("how old are you: "))
    return age_local


name = get_name()
age = get_age()
print(f"\nHi {name} at {age} years old you might find this a bit easy \n"
      "\nanyway this is a test about numbers in maroi \n"
      "you will need to enter the number witch applies"
      " e.g for the numbers write 1, 2 , 3 , 4 and so on \n")

days = [["tahi", "1"], ["rua", "2"], ["toru", "3"], ["wha", "4"], ["rima", "5"], ["ono", "6"], ["whitu", "7"], ["waru", "8"], ["tekau", "10"]]


random.shuffle(days)

for i in days:
    answer = input(f"enter the abbreviation witch applies to {i[0]}: ")
    if answer == i[1]:
        print("Correct! \n")
        continue
    else:
        print("Incorect! \n")
        question = input ("do you want to play again? answer with y/n")
        if question != 'y':
            quit()
