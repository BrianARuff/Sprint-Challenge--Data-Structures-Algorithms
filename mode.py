def findMode(numbers):
    dict = {}

    for n in numbers:
        if n not in dict:
            dict[n] = 1
        else:
            dict[n] = dict[n] + 1
    return max(dict, key=lambda k: dict[k])


print(findMode([1, 2, 2, 3, 4, 5, 6, 6, 6]))
