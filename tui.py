from process import standard


def title():
    msg = "|| Welcome to MARRIAGE CARD GAME! ||"
    print("~" * len(msg))
    print(msg)
    print("~" * len(msg))


def add_card():
    card = input("ADD card to hand: ")
    return standard(card)
