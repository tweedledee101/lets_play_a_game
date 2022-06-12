import random
from pprint import pprint

# Setting the scene
print("Welcome to Fantasma's: Game of Horror\n brought to you by tweedledee\n")

user_name = input("What's your name dear friend\n")

print(f"Ah yes {user_name}, I thought I smelled fear.\n")


# To make this more game-like, we should be able to offer various options which we can program for
feelings = ["insulted", "scared", "doesn't care" ]


# You know what a string is, pay attention to how one quote works vs, three quotes (demonstrated below)
print("""
      ********************
      *      MENU        *
      ********************
      *** 1: insulted ****
      *** 2: scared ******
      *** 3: doesn't care*
      ********************\n\n
""")

user_feels = input(f"{user_name} feels (choose a numbered option from above):")

# This looks long and complicated, its not... we're taking the user input (their feelings) and just checking the number. If the number matches, we do everything within each block:
if user_feels == "1":
    #creating a bunch of different responses the user can choose from, using a dictionary.
    options = {
               1: "I think that's your own stinky farts you are smelling." ,
               2: "Coming from a creature like you I'll take that as a compliment",
               3: "Yeah, well your breath doesn't do the air any favors either"  
    }

    print("*********** Insult Options Are: *******************")
    pprint(options)

    insult_Fantasma = input("What would you like to say to Fantasma? (input number here:)\n")
    int_insult_Fantasma = int(insult_Fantasma)
    print(f"\n{user_name} unflinchingly says to Fantasma: ", options[int_insult_Fantasma])

elif user_feels == "2":

    options = {
               1: "Sweet Baby Jesus, uh uh.... wha... come back later" ,
               2: "I choose life",
               3: "Death isn't a good look for me man how'd the hell did I get in here anyway?!"
    }

    pprint(options)
    scared_Fantasma_input = input("What would you like to say to Fantasma? (input number here:)\n")
    int_scared_Fantasma_input = int(scared_Fantasma_input)
    print(f"\n {user_name}, frighetened by Fantasma's presence says: ", options[int_scared_Fantasma_input])

else:
# @Fatime !!!! I intentionally left an error in here, can you tell me what the error is, and why its an error?
    options = {
               1: "meh" ,
               2: "Dude can we just get this useless dialogue over with already?",
               3: "Hey, you're kinda scary, think you can scare my boss into giving me the day off?"
    }

    pprint(options)
    indifferent_Fantasma_input = input("What would you like to say to Fantasma? (input number here:\n")
