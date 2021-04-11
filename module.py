def module():
    i = 0
    final_res = []
    while (i < 10):
        n = int(input())
        res = n%42
        if res not in final_res:
            final_res.append(res)
        i += 1

    return len(final_res)


print(module())
