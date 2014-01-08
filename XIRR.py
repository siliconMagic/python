def xirr(transactions):
    years = [(ta[0] - transactions[0][0]).days / 365. for ta in transactions]
    residual = 1
    step = 0.05
    guess = 0.05
    epsilon = 0.0001
    limit = 10000
    while abs(residual) > epsilon and limit > 0:
        limit -= 1
        residual = 0.0
        for i, ta in enumerate(transactions):
            residual += ta[1] / pow(guess, years[i])
        if abs(residual) > epsilon:
            if residual > 0:
                guess += step
            else:
                guess -= step
                step /= 2.0
    return guess-1

from datetime import date
tas = [ (date(2006, 1, 24), -39967),
    (date(2008, 2, 6), -19866),
    (date(2010, 10, 18), 245706),
    (date(2012, 9, 14), 52142)]
print(xirr(tas))