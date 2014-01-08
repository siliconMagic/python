def csuccessors(state):
	M1, C1, B1, M2, C2, B2 = state
	if C1> M1 > 0 or C2 > M2 > 0:
		return{}
	val = (-2,-1,0) if B1 else (0,1,2); dir = '%s%s->' if B1 else '<-%s%s'
	return dict([((M1+i, C1+j, abs(B1-1), M2-i, C2-j, abs(B2-1)), dir % ('M'*abs(i), 'C'*abs(j)))
				for i in val for j in val
				if (M1+i >= 0 and C1+j >= 0 and M2-i >= 0 and C2-j >= 0 and 0 < abs(i+j) < 3)])

deltas = {(2,0,1,   -2,0,-1):'MM',
		  (0,2,1,    0,-2,-1):"CC",
		  (1,1,1,   -1,-1,-1):'MC',
		  (1,0,1,   -1,0,-1):'M',
		  (0,1,1,    0,-1,-1):'C'}

def add(X, Y):
	return tuple(x+y for x,y in zip(X, Y))

def sub(X, Y):
	return tuple(x-y for x,y in zip(X, Y))

def mc_problem(start = (3,3,1,0,0,0), goal=None):
	if goal is None:
		goal = (0,0,0)+ start[:3]
		if start == goal:
			return [start]
		explored = set()
		frontier = [[start]]
		while frontier:
			path = frontier.pop(0)
			s = path[-1]
			for (state, action) in csuccessors(s).items():
				if state not in explored:
					explored.add(state)
					path2 = path +[action, state]
					if state == goal:
						return path2
					else:
						frontier.append(path2)
		return Fail

answer = mc_problem(start = (7,6,1,0,0,0))
for step in answer:
	print step
