import random

options = ("rock", "paper", "scissor")
playgame = "yes"
while playgame == "yes":
    print("You ready to Play, Select..")
    user_option = input("rock, paper or scissor-----").lower()
    computer_option = random.choice(options)  # select random option
    if not user_option in options:
        print("ERROR ERROR---Incorrect Options---ERROR ERROR")
        exit()
    print(f"You select {user_option}")
    print(f"Computer select {computer_option}")
    if user_option == computer_option:
        print("Draw!")
    elif user_option == "rock":
        if computer_option == "scissor":
            print("rock Winner!")
            print("User Win!")
        else:
            print("paper Winner!")
            print("computer Win!")
    elif user_option == "paper":
        if computer_option == "rock":
            print("paper Winner!")
            print("User Win!")
        else:
            print("scissor Winner!")
            print("Computer Win!")

    elif user_option == "scissor":
        if computer_option == "paper":
            print("scissor Win!")
            print("User Win!")
        else:
            print("rock Winner!")
            print("Computer Win!")
    try:
        playgame = input('Are You Play Again "Yes" or "No"? =>').lower()
    except Exception:
        print("ERROR ERROR---Incorrect Options---ERROR ERROR")
        exit()
print("Finish Game...")
