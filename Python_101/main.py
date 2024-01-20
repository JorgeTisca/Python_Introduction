user_option = input("rock, paper or sisor-----")
computer_option = "paper"

if user_option == computer_option:
    print("Draw!")
elif user_option == "rock":
    if computer_option == "sisor":
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
        print("sisor Winner!")
        print("Computer Win!")

elif user_option == "sisor":
    if computer_option == "paper":
        print("sisor Win!")
        print("User Win!")
    else:
        print("rock Winner!")
        print("Computer Win!")
