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
	return max(count_rankings[counts], 4*straight + 5*flush), ranks

count_rankings = {(5,):10, (4, 1):7, (3, 2):6, (3, 1, 1):3, (2, 2, 1):2, (2, 1, 1, 1):1, (1, 1, 1, 1, 1):0}

with open('poker.txt') as fp:
    for line in fp:
        print(line)