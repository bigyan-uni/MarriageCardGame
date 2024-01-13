import process
import tui

cards = {"1H": 3, "2H": 3, "3H": 3, "4H": 3, "5H": 3, "6H": 3, "7H": 3, "8H": 3, "9H": 3, "10H": 3, "11H": 3, "12H": 3,
         "13H": 3, "1S": 3, "2S": 3, "3S": 3, "4S": 3, "5S": 3, "6S": 3, "7S": 3, "8S": 3, "9S": 3, "10S": 3, "11S": 3,
         "12S": 3, "13S": 3, "1C": 3, "2C": 3, "3C": 3, "4C": 3, "5C": 3, "6C": 3, "7C": 3, "8C": 3, "9C": 3, "10C": 3,
         "11C": 3, "12C": 3, "13C": 3, "1D": 3, "2D": 3, "3D": 3, "4D": 3, "5D": 3, "6D": 3, "7D": 3, "8D": 3, "9D": 3,
         "10D": 3, "11D": 3, "12D": 3, "13D": 3, "007": 3, "008": 1}

hand = {"1H": 0, "2H": 0, "3H": 0, "4H": 0, "5H": 0, "6H": 0, "7H": 0, "8H": 0, "9H": 0, "10H": 0, "11H": 0, "12H": 0,
        "13H": 0, "1S": 0, "2S": 0, "3S": 0, "4S": 0, "5S": 0, "6S": 0, "7S": 0, "8S": 0, "9S": 0, "10S": 0, "11S": 0,
        "12S": 0, "13S": 0, "1C": 0, "2C": 0, "3C": 0, "4C": 0, "5C": 0, "6C": 0, "7C": 0, "8C": 0, "9C": 0, "10C": 0,
        "11C": 0, "12C": 0, "13C": 0, "1D": 0, "2D": 0, "3D": 0, "4D": 0, "5D": 0, "6D": 0, "7D": 0, "8D": 0, "9D": 0,
        "10D": 0, "11D": 0, "12D": 0, "13D": 0, "007": 0, "008": 0}


# Main function that displays Menus and calls other modules.
def run():
    tui.title()
    process.make_hand(hand, cards)

    # Players now have a hand of 21
    turn_number = 1
    players, my_turn = tui.player_num()
    top_card = tui.top_card()
    while True:
        if turn_number == my_turn:  # My first turn
            process.my_first_move(top_card, hand, cards)
        elif turn_number % players == my_turn and turn_number > my_turn:  # My turns after this
            process.my_move(top_card, hand, cards)
        else:  # Other's turn to discard cards
            top_card = process.others_move(cards)
        turn_number += 1


if __name__ == "__main__":
    run()
