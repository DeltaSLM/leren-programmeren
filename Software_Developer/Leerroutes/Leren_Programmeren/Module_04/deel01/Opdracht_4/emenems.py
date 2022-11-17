import random

MnMcolors = ['red', 'green', 'yellow', 'pink', 'blue']
randomized = random.sample(MnMcolors, random.randint(1, 5))

def decomposition(i):
      # need help here
      while i > 0:
        n = random.randint(1, i)
        yield n
        i -= n

rand_numbers = list(decomposition(200))
thedict = {}
for num, color in enumerate(randomized):
    thedict[color] = rand_numbers[num]

print(thedict)