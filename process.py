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


# Function that dissects hand dictionary into 4 lists based on suite
def break_hand(hand: dict):
    heart_list = []
    spade_list = []
    club_list = []
    diamond_list = []
    for card, num in hand.items():
        card_number = int(card[:-1])
        if card[-1:] == "H":
            heart_list.append(card_number)
            if card_number == 1:
                heart_list.append(14)
        elif card[-1:] == "S":
            spade_list.append(card_number)
            if card_number == 1:
                heart_list.append(14)
        elif card[-1:] == "C":
            club_list.append(card_number)
            if card_number == 1:
                heart_list.append(14)
        elif card[-1:] == "D":
            diamond_list.append(card_number)
            if card_number == 1:
                heart_list.append(14)
    return [heart_list, spade_list, club_list, diamond_list]


# Function that reassembles wanted list of cards with suites
def create_wanted_list(wanted: list) -> list:
    wanted_list = []
    for entry in wanted:
        suite_name = entry[0]
        suite_wanted = entry[1]
        for num in suite_wanted:
            wanted_card = str(num) + suite_name
            wanted_list.append(wanted_card)
    return wanted_list


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


# Function checks for tunnels [4♠ 4♠ 4♠]
def check_tunnel(hand: dict) -> list:
    tunnels = []
    for card, num in hand.items():
        if num >= 3:
            tunnels.append(card)
    return tunnels


# Function to make my first move
def my_first_move(top_card: str, hand: dict, cards: dict):
    tunnels = check_tunnel(hand)
    if len(tunnels) > 0:
        tui.declare_tunnels(tunnels)
    my_move(top_card, hand, cards)


# Function that checks for the least valuable card
def least_valuable_card(hand: dict, good_cards: list) -> list:
    bad_cards = []
    for key in hand.keys():
        if key not in good_cards:
            bad_cards.append(key)
    return bad_cards


# Function to make my next moves
def my_move(top_card: str, hand: dict, cards: dict):

    # see chance of getting wanted card from top and from deck
    wanted_cards = create_wanted_list(check_possible_sequence(hand)[1])
    if top_card in wanted_cards:
        tui.chance("getting wanted card from top", 100)
    wanted_cards.append("007")
    wanted_cards.append("008")
    total_chance = decision(wanted_cards, cards)
    tui.chance("getting wanted card from deck", total_chance)

    # choose my action to draw card from top or from deck
    action = tui.my_action()
    if action == "A":  # from top
        draw(top_card, hand)
    elif action == "B":
        new_card = tui.add_card()
        draw(new_card, hand)  # from deck

    # find out all info out the 22 cards before discarding a card
    tui.sequences(True, check_pure_sequence(hand))
    tui.sequences(False, check_possible_sequence(hand)[0])
    good_cards = create_wanted_list(check_pure_sequence(hand))
    bad_cards = least_valuable_card(hand, good_cards)
    tui.bad_cards(bad_cards)
    discard(tui.discard(), cards)


# Function will calculate if picking top card is better than picking random card from deck
def decision(wanted_cards: list, cards: dict) -> int:
    num_desirable_outcomes = 0
    total_poss_outcomes = 0
    for key, value in cards.items():
        total_poss_outcomes += value
    for card in wanted_cards:
        if card in cards.keys():
            num_desirable_outcomes += cards[card]
    total_chance = (num_desirable_outcomes * 100)/total_poss_outcomes
    return int(total_chance)


# Function that checks for pure sequence [A♥ 2♥ 3♥]
def check_pure_sequence(hand: dict) -> list:
    suites = break_hand(hand)
    sequences = []
    for i in range(len(suites)):
        suite = suites[i]
        suite_sequences = []
        suite_name = ["H", "S", "C", "D"][i]
        for j in suite:
            if j + 1 in suite and j + 2 in suite:
                suite_sequences.append([j, j+1, j+2])
        sequences.append([suite_name, suite_sequences])
    return sequences


# Function checks for possible sequence [A♥ 2♥]
def check_possible_sequence(hand: dict) -> tuple:
    suites = break_hand(hand)
    sequences = []
    wanted = []  # cards needed to make sequence possible
    for i in range(len(suites)):
        suite = suites[i]
        suite_name = ["H", "S", "C", "D"][i]
        suite_sequences = []
        suite_wanted = []
        for j in suite:
            if j + 1 in suite:
                suite_sequences.append([j, j + 1])
                suite_wanted.append(j + 2)
                if j - 1 > 0:
                    suite_wanted.append([j - 1])
        sequences.append([suite_name, suite_sequences])
        wanted.append([suite_name, suite_wanted])
    return sequences, wanted


# Function to make other's move, returns new top card
def others_move(cards: dict) -> str:
    card = tui.other_discard()
    discard(card, cards)
    return card
