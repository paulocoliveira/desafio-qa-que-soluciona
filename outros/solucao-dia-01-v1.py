def pickingNumbers(a):
    # Write your code here
    size = len(a)
    start = 0
    big = 0
    for i in range(start, size):
        for j in range(i+1, size):
            if (abs(a[i]-a[j]) <= 1):
                if (((j-i) + 1) > big):
                    big = (j-i) + 1
    return big

l = [4, 6, 5, 3, 3, 1]
print(pickingNumbers(l))