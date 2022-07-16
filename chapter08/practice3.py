def average(*args):
    sum = 0

    for value in args:
        sum += value

    return sum / len(args)

print(average(1, 2, 3, 4, 5))
