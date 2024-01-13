from typing import Tuple

import process


# DISPLAYS TITLE OF PROGRAM
def title():
    msg = "|♥♣♠♦| Welcome to MARRIAGE CARD GAME! |♥♣♠♦|"
    print("~" * len(msg))
    print(msg)
    print("~" * len(msg))


# Asks what action user will take
def my_action() -> str:
    print("""
    What action will you take?
    \t[A] Take top card
    \t[B] Draw from card deck
    """)
    return input().upper().strip()


# Asks what user will throw from hand
def discard() -> str:
    print("Number + H♥ C♣ S♠ D♦")
    card = input("What card will you discard?")
    return card


# TAKES USER INPUT CARD AND RETURNS STANDARDISED INPUT
def add_card() -> str:
    print("Number + H♥ C♣ S♠ D♦")
    card = input("ADD card to hand: ")
    return process.standard(card)


# FIRST FLIPPED TOP CARD
def top_card() -> str:
    print("Number + H♥ C♣ S♠ D♦")
    card = input("What is the top card? ")
    return process.standard(card)


# Returns Number of Players
def player_num() -> Tuple[int, int]:
    players = int(input("How many players are there?"))
    turn = int(input("Which turn do you play?"))
    return players, turn


# DISPLAYS CARDS IN HAND
def see_hand(hand: dict):
    for card, num in hand.items():
        if num != 0:
            number = card[:-1]
            suit = card[-1:]
            display = ""
            if number == "11":
                number = "J"
            elif number == "12":
                number = "Q"
            elif number == "13":
                number = "K"
            elif number == "1":
                number = "A"
            if suit == "H":
                display = number + "♥"
            elif suit == "C":
                display = number + "♣"
            elif suit == "S":
                display = number + "♠"
            elif suit == "D":
                display = number + "♦"
            print(f"[{display}], " * num, end="")
    print("\n")


# Displays tunnels in own hand:
def declare_tunnels(tunnels):
    print("!!!You have the following tunnels: !!!")
    for tunnel in tunnels:
        print(tunnel)


# Returns card discarded by others
def other_discard() -> str:
    card_num = input("Card discarded by others: ")
    return card_num


# Displays sequences (pure or possible)
def sequences(pure: bool, sequence: list):
    if pure is True:
        print("You have the following pure sequences: ")
    elif pure is False:
        print("You have the following possible sequences: ")
    for entry in sequence:
        print(f"For the suite {entry[0]}, ")
        print(entry[1])


# Displays chance of an event
def chance(event: str, probability: int):
    print(f"The chance of {event} is {probability}%.")


# Displays bad cards
def bad_cards(cards: list):
    print("Cards you should consider discarding are: ")
    print(cards)


# Displays Error Message
def error(msg: str):
    print(f"Error! {msg}")
