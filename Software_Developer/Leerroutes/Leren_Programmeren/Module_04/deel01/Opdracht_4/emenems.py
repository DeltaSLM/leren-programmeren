import random

MnMcolors = ['red', 'green', 'geel', 'pink', 'blue']
randomized = random.sample(MnMcolors, random.randint(1, 5))


def decomposition(i, x):
    # need help here
    ran = [random.randint(1, i) for _ in range(x)]
    res = [ran[y] * i / sum(ran) for y in range(x)]
    return map(round, res)


rand_numbers = list(decomposition(200, len(randomized)))
print(rand_numbers)
thedict = {}
for num, color in enumerate(randomized):
    thedict[color] = rand_numbers[num]

print(thedict)