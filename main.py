import art
import random

def neustart():
    global blackjack, game, count_comp, count_user, user, comp, choice
    choice = input("Do u want to play again? Type 'y' or 'n'")
    if choice == "n":
        blackjack = False
    elif choice == "y":
        game = True
        count_comp = 0
        count_user = 0
        user = []
        comp = []
    else:
        blackjack = False


def user_add():
    global  count_user, user
    user.append(random.choice(cards))
    count_user = 0
    for add in user:
        count_user += add
        if 11 in user and count_user > 21:
            user[user.index(11)] = 1
            count_user -= 10


def comp_add():
    global comp, count_comp
    comp.append(random.choice(cards))
    count_comp = 0
    for add in comp:
        count_comp += add
    if 11 in comp and count_comp > 21:
        comp[comp.index(11)] = 1
        count_comp -= 10


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

choice = input("Do you want to play a game of blackjack? Type 'y' or 'n'")

blackjack = True
user = []
comp = []

count_user = 0
count_comp= 0

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
            if count_user == 21:
                choice = "n"
            else:
                choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == "y":
                user_add()
                for add in comp:
                    count_comp += add
                if count_user > 21:
                    print(f"Your final hand: {user}, current score: {count_user}")
                    print(f"Computer's final hand: {comp}, final score: {count_comp}")
                    print("You went over. You lose :(")
                    game = False
                    neustart()
            elif choice == "n":
                while count_comp < 17:
                    comp_add()

                print(f"Your final hand: {user}, current score: {count_user}")
                print(f"Computer's final hand: {comp}, final score: {count_comp}")

                if count_comp > 21 or count_comp < count_user:
                    print("U Win")
                elif count_comp > count_user:
                    print("U lose")
                elif count_comp == count_user:
                    print("Draw")
                game = False

        game = False

        if blackjack:
            neustart()

    elif choice == "n":
        blackjack = False
    else:
        choice = input("pls enter y or n ")



