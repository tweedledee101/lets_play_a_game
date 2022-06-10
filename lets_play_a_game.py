print("Welcome to Fantasma's: Game of Horror\n brought to you by tweedledee\n")
user_name = input("What's your name dear friend\n")

print(f"Ah yes {user_name}, I thought I smelled fear.\n Would you like to go on a journey with me? \n")

journey_answer = input("y: yes\nn: no\n")

if journey_answer == "y":
    print("wonderful, glad to have you aboard!")

else:
    print("fine, come back when you wanna talk")
    exit()
