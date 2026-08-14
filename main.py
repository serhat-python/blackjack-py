import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

choice = input("Do you want to play a game of blackjack? Type 'y' or 'n'")

blackjack = True
user = []
comp = []

count_user = 0
count_computer= 0

game = True

while blackjack:
    if choice == "y":
        if count_user == 0:
            print (art.logo)
        user.append(random.choice(cards))
        user.append(random.choice(cards))
        comp.append(random.choice(cards))
        for add in user:
            count_user += add
        while game:
            print(f"Your cards: {user}, current score: {count_user}")
            print(f"Computers first cards: {comp}")
            choice = input("Type 'y' to get another card, type 'n' to pass: " )
            if choice == "y":
                user.append(random.choice(cards))
                count_user = 0
                for add in user:
                    count_user += add
                for add in comp:
                    count_computer += add
                if count_user > 21:
                    print(f"Your final hand: {user}, current score: {count_user}")
                    print(f"Computer's final hand: {comp}, final score: {count_computer}")
                    print("You went over. You lose :(")
                    choice = input("Do u want to play a game of Blackjack? Type 'y' or 'n'" )
                    if choice == "n":
                        game = False
                        blackjack = False
                    elif choice == "y":
                        count_computer = 0
                        count_user = 0
                        user = []
                        comp = []
                        print(art.logo)
                        user.append(random.choice(cards))
                        user.append(random.choice(cards))
                        comp.append(random.choice(cards))
                        for add in user:
                            count_user += add

                    else:
                        blackjack = False
            elif choice == "n":
                while count_computer < 17:
                    comp.append(random.choice(cards))
                    count_computer = 0
                    for add in comp:
                        count_computer += add
                print(f"Your final hand: {user}, current score: {count_user}")
                print(f"Computer's final hand: {comp}, final score: {count_computer}")
                game = False
                blackjack = False
                if count_computer > 21 and count_user <= 21:
                    print("U Win")
                elif count_computer > count_user:
                    print("U lose")
                elif count_computer == count_user:
                    print("Draw")
                elif count_computer < count_user:
                    print("U Win")



    elif choice == "n":
        blackjack = False
    else:
        choice = input("pls enter y or n ")

