'''
The following iterative sequence is defined for the set of positive integers
n -> n/2 (n is even)
n -> 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
'''
from matplotlib.pyplot import plot, show

cache = { 1: 1 }
def chain(cache, n):
    if not cache.get(n,0):
        if n % 2: cache[n] = 1 + chain(cache, 3*n + 1)
        else: cache[n] = 1 + chain(cache, n/2)
    return cache[n]

m,n = 0,0
for i in range(1, 10000000):
    c = chain(cache, i)
    if c > m: m,n = c,i
print (n, " is the high number")


def print_chain(n):
    link = n
    the_chain = []
    while link != 1:
        if link % 2:
            link = 3*link + 1
        else:
            link = link/2
        the_chain.append(link)
    return the_chain    
        
print(len(print_chain(n)), " steps")
plot(print_chain(n))
show()