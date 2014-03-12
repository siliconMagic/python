import pprint

matrix=[[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]]

def cw(m): return [[m[4-j][i] for j in range(0,5) ] for i in range(0,5)]
def ccw(m): return [[m[j][4-i] for j in range(0,5) ] for i in range(0,5)]

pprint.pprint(matrix)
pprint.pprint(cw(matrix))
pprint.pprint(ccw(matrix))