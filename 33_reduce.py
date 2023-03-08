from functools import reduce

l = [1, 2, 3, 4]


def greater(prev, curr):
    if (prev > curr):
        return prev
    else:
        return curr


greatest = reduce(greater, l)

print(greatest)
  