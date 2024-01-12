cards = {"A1": 4, "A2": 4, "A3": 4, "A4": 4, "A5": 4, "A6": 4, "A7": 4, "A8": 4, "A9": 4, "A10": 4, "A11": 4, "A12": 4,
         "A13": 4, "B1": 4, "B2": 4, "B3": 4, "B4": 4, "B5": 4, "B6": 4, "B7": 4, "B8": 4, "B9": 4, "B10": 4, "B11": 4,
         "B12": 4, "B13": 4, "C1": 4, "C2": 4, "C3": 4, "C4": 4, "C5": 4, "C6": 4, "C7": 4, "C8": 4, "C9": 4, "C10": 4,
         "C11": 4, "C12": 4, "C13": 4, "D1": 4, "D2": 4, "D3": 4, "D4": 4, "D5": 4, "D6": 4, "D7": 4, "D8": 4, "D9": 4,
         "D10": 4, "D11": 4, "D12": 4, "D13": 4}


# Function that standardizes the card to suit "A,B,C,D"
def standard(card: str) -> str:
    card = card.upper().strip()
    card.replace("HEART", "A")
    card.replace("H", "A")
    card.replace("SPADE", "B")
    card.replace("S", "B")
    card.replace("CLUB", "C")
    # card.replace("C", "C")
    card.replace("DIAMOND", "D")
    # card.replace("D", "D")
    card.replace("JACK", "11")
    card.replace("J", "11")
    card.replace("QUEEN", "12")
    card.replace("Q", "D")
    card.replace("KING", "13")
    card.replace("K", "13")
    return card


# Function to return number of specific card. Returns int.
def card_num(card: str) -> int:
    return cards[card]


# Function that decrements number of specific card. Returns nothing.
def discard(card: str):
    cards[card] -= 1
