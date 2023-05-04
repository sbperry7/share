def displayGreeting():
    print("\nThe Wizard will see you now.")
    print("\n\nOK, let's get started\n")

def askQuestion():
    
    while True:

    name = input("What's your name? ")

    if name == 'quit':

    else:

        question = input("\n\nWhat's your question? ")

        print("\n\nAttention " + name + "!  The Wizard declares:", wizard_message)

        choice = input("\n\nDo you have another question? Y/N ")

        if choice.lower() != 'y':
            break  #????


print("Assginment 2\n")
print("* * The Wizard * *")

name = ""

playGame = input("Do you want to talk to the Wizard? (Yes or No) ")

if playGame == 'Yes':
    displayGreetin()
    askQuestion()
else:
    print("The Wizard wants you to go away now!")





