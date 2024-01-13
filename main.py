import process
import tui

cards = {"1H": 4, "2H": 4, "3H": 4, "4H": 4, "5H": 4, "6H": 4, "7H": 4, "8H": 4, "9H": 4, "10H": 4, "11H": 4, "12H": 4,
         "13H": 4, "1S": 4, "2S": 4, "3S": 4, "4S": 4, "5S": 4, "6S": 4, "7S": 4, "8S": 4, "9S": 4, "10S": 4, "11S": 4,
         "12S": 4, "13S": 4, "1C": 4, "2C": 4, "3C": 4, "4C": 4, "5C": 4, "6C": 4, "7C": 4, "8C": 4, "9C": 4, "10C": 4,
         "11C": 4, "12C": 4, "13C": 4, "1D": 4, "2D": 4, "3D": 4, "4D": 4, "5D": 4, "6D": 4, "7D": 4, "8D": 4, "9D": 4,
         "10D": 4, "11D": 4, "12D": 4, "13D": 4, "007": 4, "008": 1}

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
    game_over = False
    turn_number = 1
    players, my_turn = tui.player_num()
    top_card = tui.top_card()
    while game_over is False:
        if turn_number == my_turn:  # My first turn
            process.my_first_move(top_card, hand, cards)
        if turn_number % players == my_turn and turn_number > my_turn:  # My turns after this
            process.my_move(top_card, hand, cards)
        else:  # Other's turn to discard cards
            top_card = process.others_move(cards)


if __name__ == "__main__":
    run()
