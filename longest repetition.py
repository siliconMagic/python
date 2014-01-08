def longest_repetition(l):
    if l == []:
        return None
    current_rep = 1
    longest_rep = 1
    winner = l[0]
    for i in range(0, len(l)-1):
        if l[i] == l[i+1]:
            current_rep = current_rep +1
        else:
            current_rep = 1
        if current_rep > longest_rep:
            winner = l[i]
            longest_rep = current_rep
    return winner
        
        
    
    
        
        
print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None
