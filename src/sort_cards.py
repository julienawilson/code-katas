"""Sort a deck of cards code-kata using a Priority Queue."""

from priority import PriorityQueue

card_dict = {
    'A': 1,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    1: 'A',
    10: 'T',
    11: 'J',
    12: 'Q',
    13: 'K',
}


def sort_cards(cards):
    """Sort shuffled list of cards, sorted by rank."""
    card_list = []
    for card in cards:
        try:
            card_list.append(int(card))
        except ValueError:
            card_list.append(card_dict[card])
    card_list.sort()
    result = []
    for card in card_list:
        if card > 1 and card < 10:
            result.append(str(card))
        else:
            result.append(card_dict[card])
    return result


def sort_cards_w_pq(cards):
    """Sort shuffled list of cards, sorted by rank, using a priority queue."""
    card_list = []
    for card in cards:
        try:
            card_list.append((int(card), card))
        except ValueError:
            card_list.append(card_dict[card])
    card_q = PriorityQueue(card_list)
    result = []
    for i in range(len(card_list)):
        result.append(card_q.pop())
    return result
