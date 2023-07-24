from os import system
from art import logo
import random

users_cards = []
dealers_cards = []


def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def start_game():
    users_cards = []
    dealers_cards = []
    userscore = 0
    dealerscore = 0

    print(logo)

    for i in range(0, 2):
        card0 = draw_card()
        card1 = draw_card()
        userscore += card0
        dealerscore += card1
        users_cards.append(card0)
        dealers_cards.append(card1)

    # printing
    print(f"user cards = {users_cards} , user score = {userscore}")
    print(f"dealer cards = {dealers_cards} , dealer score = {dealerscore}")

    user_draw = True

    if userscore == 21 or dealerscore > 21:
        print("USER WINS")
    if dealerscore == 21 or userscore > 21:
        print("DEALER WIN")

    choose = input("ENTER 'Y' TO DRAW 'N' TO PASS : ")

    if choose == "N" or choose == "n":
        user_draw = False

    while user_draw:

        if userscore == 21:
            print("USER WINS")
            return
        if dealerscore == 21:
            print("DEALER WIN")
            return
        if userscore > 21:
            print("Dealer WINS")
            return
        if dealerscore > 21:
            print("User WIN")
            return

        caard = draw_card()
        userscore += caard
        users_cards.append(caard)

        print(f"user cards = {users_cards} , user score = {userscore}")
        print(f"dealer cards = {dealers_cards} , dealer score = {dealerscore}")

        if userscore > 21:
            print("Dealer WINS")
            return
        if dealerscore > 21:
            print("User WIN")
            return
        if userscore == 21:
            print("USER WINS")
            return
        if dealerscore == 21:
            print("DEALER WIN")
            return

        choose = input("ENTER 'Y' TO DRAW 'N' TO PASS : ")

        if (choose == "N" or choose == "n"):
            user_draw = False

    if (dealerscore < 17):
        dealer_draw = True

    while dealer_draw:

        if userscore == 21:
            print("USER WINS")
            return
        if dealerscore == 21:
            print("DEALER WIN")
            return
        if userscore > 21:
            print("Dealer WINS")
            return
        if dealerscore > 21:
            print("User WIN")
            return

        caard = draw_card()
        dealerscore += caard
        dealers_cards.append(caard)

        print(f"user cards = {users_cards} , user score = {userscore}")
        print(f"dealer cards = {dealers_cards} , dealer score = {dealerscore}")

        if userscore > 21:
            print("Dealer WINS")
            return
        if dealerscore > 21:
            print("User WIN")
            return
        if userscore == 21:
            print("USER WINS")
            return
        if dealerscore == 21:
            print("DEALER WIN")
            return
        if dealerscore > 17:
            dealer_draw = False


play = True
while play:
    system("clear")
    start_game()
    choose = input("ENTER 'Y' TO Play Again 'N' TO Exit : ")
    if choose == "N" or choose == "n":
        play = False
