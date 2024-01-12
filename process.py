import tui


# Function that standardizes the card to suit "H,S,C,D"
def standard(card: str) -> str:
    card = card.upper().strip()
    card = card.replace("HEART", "H")
    card = card.replace("SPADE", "S")
    card = card.replace("CLUS", "C")
    card = card.replace("DIAMOND", "D")
    card = card.replace("JACK", "11")
    card = card.replace("J", "11")
    card = card.replace("QUEEN", "12")
    card = card.replace("Q", "12")
    card = card.replace("KING", "13")
    card = card.replace("K", "13")
    card = card.replace("A", "1")
    return card


# Function that checks if input card is valid
def valid(card: str) -> bool:
    num = card[:-1]
    suit = card[-1:]
    is_valid = False
    if num in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]:
        if suit in ["H", "S", "C", "D"]:
            is_valid = True
        else:
            tui.error("Invalid Suit.")
    else:
        tui.error("Invalid number.")
    return is_valid


# Function to return number of specific card. Returns int.
def card_num(card: str, cards: dict) -> int:
    num = cards[card]
    return num


# Function that decrements number of specific card. Returns nothing.
def discard(card: str, cards: dict):
    if card_num(card, cards) > 0:
        cards[card] -= 1


# Function that increments number of specific card. Returns nothing.
def draw(card: str, hand: dict):
    hand[card] += 1


#  Function to make initial hand during first draw
def make_hand(hand: dict, cards: dict):
    i = 1
    while i <= 21:
        card = tui.add_card()
        if valid(card):
            if card_num(card, cards) > 0:
                draw(card, hand)  # add card to hand
                discard(card, cards)  # remove from main deck
                tui.see_hand(hand)
                i += 1
            else:
                tui.error("Too many cards of same type.")


# Function to make my first move
def my_first_move():
    pass


# Function to make my next moves
def my_move():
    pass


# Function to make other's move
def others_move():
    pass
