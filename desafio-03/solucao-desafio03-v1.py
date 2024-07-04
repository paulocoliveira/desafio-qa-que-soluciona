def beautifulDays(i, j, k):
    beautiful_days_count = 0
    for day in range(i, j+1):
        inverted_day = int(str(day)[::-1])
        if ((day - inverted_day) % k == 0):
            beautiful_days_count += 1
    return beautiful_days_count

print(beautifulDays(20, 23, 6))
print(beautifulDays(13, 45, 3))
print(beautifulDays(1, 2000000, 1000000000))
print(beautifulDays(1, 2000000, 23047885))
