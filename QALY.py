def qaly():
    period = int(input())
    final_sum = 0
    while(period):
        quality = input()
        quality_list = quality.split()
        q = float(quality_list[0])
        y = float(quality_list[1])
        new_sum = q*y
        final_sum += new_sum
        period -= 1
    final_sum = "{:.3f}".format(final_sum)
    return final_sum

print(qaly())