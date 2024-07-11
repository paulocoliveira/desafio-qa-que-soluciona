def timeInWords(h, m):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", 
            "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", 
            "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", 
            "twenty eight", "twenty nine", "half"]

    if m == 0:
        return f"{nums[h]} o' clock"
    elif m <= 30:
        if m == 15 or m == 30:
            return f"{nums[m]} past {nums[h]}"
        elif m == 1:
            return f"one minute past {nums[h]}"
        else:
            return f"{nums[m]} minutes past {nums[h]}"
    else:
        if m == 45:
            return f"quarter to {nums[(h % 12) + 1]}"
        elif m == 59:
            return f"one minute to {nums[(h % 12) + 1]}"
        else:
            return f"{nums[60 - m]} minutes to {nums[(h % 12) + 1]}"

# Exemplos de uso:
assert timeInWords(5, 0) == "five o' clock", "Test failed for 5:00"
assert timeInWords(5, 1) == "one minute past five", "Test failed for 5:01"
assert timeInWords(5, 10) == "ten minutes past five", "Test failed for 5:10"
assert timeInWords(5, 15) == "quarter past five", "Test failed for 5:15"
assert timeInWords(5, 28) == "twenty eight minutes past five", "Test failed for 5:28"
assert timeInWords(5, 30) == "half past five", "Test failed for 5:30"
assert timeInWords(5, 40) == "twenty minutes to six", "Test failed for 5:40"
assert timeInWords(5, 45) == "quarter to six", "Test failed for 5:45"
assert timeInWords(5, 47) == "thirteen minutes to six", "Test failed for 5:47"
assert timeInWords(12, 51) == "nine minutes to one", "Test failed for 12:51"