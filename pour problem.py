def pour_problem(X, Y, goal, start=(0, 0)):

    """
	:param X: size of container 1
	:param Y: size of container 2
	:param goal: final amount (goal)
	:param start: initial amounts in a tuple (example (2,3) means container 1 holds 2 and container 2 holds 3)
	:return: list of steps to reach goal, or Fail if no solution is found
	"""


    if goal in start:
        return [start]
    explored = set()
    frontier = [[start]]
    while frontier:
        path = frontier.pop(0)
        (x, y) = path[-1]
        for (state, action) in successors(x, y, X, Y).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if goal in state:
                    return path2
                else:
                    frontier.append(path2)
    return Fail
    
    Fail = []


def successors(x, y, X, Y):
    return {((0, y + x) if y + x <= Y else (x - (Y - y), y + (Y - y))): 'X->Y',
            ((x + y, 0) if x + y <= X else (x + (X - x), y - (X - x))): 'X<-Y',
            (X, y): 'fill X', (x, Y): 'fill Y',
            (0, y): 'empty X', (x, 0): 'empty Y'}


solution = pour_problem(5,7,4)
print(solution)
