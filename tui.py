import process


# DISPLAYS TITLE OF PROGRAM
def title():
    msg = "|♥♣♠♦| Welcome to MARRIAGE CARD GAME! |♥♣♠♦|"
    print("~" * len(msg))
    print(msg)
    print("~" * len(msg))


# TAKES USER INPUT CARD AND RETURNS STANDARDISED INPUT
def add_card():
    print("Number + H♥ C♣ S♠ D♦")
    card = input("ADD card to hand: ")
    return process.standard(card)


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


# Displays Error Message
def error(msg: str):
    print(f"Error! {msg}")
