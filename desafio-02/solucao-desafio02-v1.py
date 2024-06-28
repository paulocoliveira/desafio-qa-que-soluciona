def countingValleys(path):
    level = 0
    valleys = 0
    in_valley = False
    for step in path:           
        if (step == "U"):
            level = level + 1
        elif (step == "D"):
            level = level - 1
        
        if (level == -1):
            in_valley = True
        elif (level == 0 and in_valley == True):
            valleys = valleys + 1
            in_valley = False

    return valleys

print(countingValleys("DDUUDDUDUUUD"))
print(countingValleys("UDUUUDUDDD"))
print(countingValleys("DUDUDUDUDUDUDU"))
print(countingValleys("DDUUUUDDDUUUDDDU"))