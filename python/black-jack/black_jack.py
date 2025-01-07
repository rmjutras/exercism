"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
# Design considerations: creating 'Hand' class would eliminate
# the duplication the str to int conversion in every function
# (could put in the constructor)
FACE_CARD = ['J', 'K', 'Q']
ACE_CARD = 'A'

def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    try:
        int(card)
    except ValueError as exc:
        if card in FACE_CARD:
            return 10
        if card == ACE_CARD:
            return 1
        raise ValueError('Value is not a recognized card') from exc
    return int(card)

def higher_card(card_one: str, card_two: str):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    card_one_int = value_of_card(card_one)
    card_two_int = value_of_card(card_two)

    if card_one_int > card_two_int:
        return card_one
    if card_one_int < card_two_int:
        return card_two
    if card_one_int == card_two_int:
        return card_one, card_two
    raise ValueError('Cards could not be compared')

def value_of_ace(card_one: str, card_two: str):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if ACE_CARD in (card_one, card_two):
        return 1
    
    card_one_int = value_of_card(card_one)
    card_two_int = value_of_card(card_two)
    if card_one_int + card_two_int <= 10:
        return 11
    return 1

def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    hand = (card_one, card_two)
    if ACE_CARD in hand and \
        (value_of_card(card_one) == 10 or value_of_card(card_two) == 10):
        return True
    return False

def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    card_one_int = value_of_card(card_one)
    card_two_int = value_of_card(card_two)
    return card_one_int == card_two_int

def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    card_one_int = value_of_card(card_one)
    card_two_int = value_of_card(card_two)
    return 9 <= (card_one_int + card_two_int) <= 11
