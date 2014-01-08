import random

times = [0] * 11
loc = 5
times[5] = 1
track_steps = 0

while 0 <= loc <= 10:
    step = random.randint(0,1)
    track_steps += 1
    if step == 0:
        loc -= 1
        print 'Moving left to location', loc
        if loc < 0:
            break
    else:
        loc += 1
        print 'Moving right to location', loc
        if loc > 10:
            break
    times[loc] = times[loc] + 1
    print times
print 'That took ', track_steps, ' steps. Congratulations!'