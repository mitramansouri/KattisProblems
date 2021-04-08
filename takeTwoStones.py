def take_two_stones():
    n = int(input())
    if n % 2 == 0:
        return "Bob"
    else:
        return "Alice"

print(take_two_stones())