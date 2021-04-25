import collections

def function():
    line = input()

    frequencies = collections.Counter(line)
    repeated = {}

    for key, value in frequencies.items():
        repeated[key] = value

    res = 0
    # without the 7s
    for item in repeated:
        res += repeated[item] ** 2
    values = list(repeated.values())
    # result = all(elem == values[0] for elem in values)
    # if result:
    #     res += values[0] * 7
    # else:
    #     res += min(values) * 7
    if len(values) > 2:
        res += min(values) * 7
    return res
    
print(function())