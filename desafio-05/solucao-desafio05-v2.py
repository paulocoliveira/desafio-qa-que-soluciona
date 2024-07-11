def timeInWords(h, m):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", 
            "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", 
            "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", 
            "twenty eight", "twenty nine", "half"]

    if m == 0:
        return f"{nums[h]} o' clock"
    if m == 15 or m == 30:
        return f"{nums[m]} past {nums[h]}"
    if m == 45:
        return f"quarter to {nums[(h % 12) + 1]}"

    hour_display = nums[h] if m <= 30 else nums[(h % 12) + 1]
    minute_word = "minute" if m in [1, 59] else "minutes"
    time_direction = "past" if m <= 30 else "to"

    if m in [1, 59]:
        minute_number = "one"
    else:
        minute_number = nums[m] if m <= 30 else nums[60 - m]

    return f"{minute_number} {minute_word} {time_direction} {hour_display}"

# Unit tests to verify correctness
assert timeInWords(5, 0) == "five o' clock"
assert timeInWords(5, 1) == "one minute past five"
assert timeInWords(5, 10) == "ten minutes past five"
assert timeInWords(5, 15) == "quarter past five"
assert timeInWords(5, 28) == "twenty eight minutes past five"
assert timeInWords(5, 30) == "half past five"
assert timeInWords(5, 40) == "twenty minutes to six"
assert timeInWords(5, 45) == "quarter to six"
assert timeInWords(5, 47) == "thirteen minutes to six"
assert timeInWords(12, 51) == "nine minutes to one"