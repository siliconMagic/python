import random
import itertools

deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']
joker_deck =  deck + ['?R', '?B']
double_deck = 2 * deck

def deal(numPlayers, cards=5, whole_cards=0, deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']):
    random.shuffle(deck)
    return [deck[cards*i:cards*(i+1)] for i in range(numPlayers)], deck[-1-whole_cards:-1]

def hand_rank(hand):
    "Return a value indicating how high the hand ranks."
    # counts is the count of each rank; ranks lists corresponding ranks
    # e.g. '7 T 7 9 7' => counts = (3, 1, 1); ranks = (7, 10, 9)
    groups = group(['--23456789TJQKA'.index(r) for r,s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks)-min(ranks) == 4
    flush = len(set([s for r,s in hand])) == 1
    return max(countRankings[counts], 4*straight + 5*flush), ranks

countRankings = {(5,):10, (4, 1):7, (3, 2):6, (3, 1, 1):3, (2, 2, 1):2, (2, 1, 1, 1):1, (1, 1, 1, 1, 1):0} 

def group(items):
    "Return a list of [(count, x)...], highest count first, then highest x first."
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse=True)

def unzip(pairs): return zip(*pairs)

def list_all_hands(hand):
    red_joker = [r+s for r in '23456789TJQKA' for s in 'HD']
    black_joker = [r+s for r in '23456789TJQKA' for s in 'SC']
    hand_list = []
    if '?R' in hand and '?B' in hand:
        card_spot_red, card_spot_black = hand.index('?R'), hand.index('?B')
        for wild_card_red in red_joker:
            for wild_card_black in black_joker:
                hand = hand[:]
                hand[card_spot_red], hand[card_spot_black] = wild_card_red, wild_card_black
                hand_list.append(hand)
        return hand_list
    elif '?R' in hand:
        card_spot_red = hand.index('?R')
        for wild_card_red in red_joker:
            hand = hand[:]
            hand[card_spot_red] = wild_card_red
            hand_list.append(hand)
        return hand_list
    elif '?B' in hand:
        card_spot_black = hand.index('?B')
        for wild_card_black in black_joker:
            hand = hand[:]
            hand[card_spot_black] = wild_card_black
            hand_list.append(hand)
        return hand_list
    else:
        hand_list.append(hand)
        return hand_list

def best_hand(player_hand, cards_dealt):
    winner = []
    for player_hand in cards_dealt:
        player_hand_ranks = []
        for hand in list_all_hands(player_hand):
            player_hand_ranks.append((hand_rank(hand), hand))
        best_hand = max(player_hand_ranks)
        winner.append(best_hand)
    return max(winner)[0][0]

hand_names = ['High Card', 'Pair', '2 Pair', '3 of a Kind', 'Straight', 'Flush', 'Full House', '4 of a Kind', '***', 'Straight Flush', '5 of a Kind']

def hand_percentages(n=100*1000):
    "Sample n random hands and print a table of percentages for each type of hand."
    counts = [0] * 11
    for i in range(n):
        cards_dealt, whole_cards = deal(1, deck = deck)
        for hand in cards_dealt:
            ranking = best_hand(hand, cards_dealt)
            counts[ranking] += 1
    for i in reversed(range(11)):
        print ("{0:15} {1:.3%}".format(hand_names[i], counts[i]/n))

hand_percentages()

# 7-card Stud using a deal(players, cards, whole cards)
# cards_dealt, whole_cards = deal(4, 5, 2)
# print whole_cards, cards_dealt
# winner = []
# for player in cards_dealt:
#   player_hand_ranks = []
#   for hand in itertools.combinations(player + whole_cards, 5):
#       player_hand_ranks.append((hand_rank(hand), hand))
#   best_hand = max(player_hand_ranks)
#   print(best_hand)
#   winner.append(best_hand)
# print ("winner: {0}".format(max(winner))
        
