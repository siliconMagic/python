import matplotlib.pyplot as plt

def collatz (n):
	step = 1
	while n > 1:
		step = step + 1
		if n % 2 == 0:
			n = n / 2
		else:
			n = 3 * n + 1
	return step

big_list = []

for n in range(100):
	big_list.append(collatz(n))

print(big_list)

plt.plot(big_list)
plt.show()

