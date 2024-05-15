def count_frequency(numbers):
    freq= {}
    for nums in numbers:
        if nums in freq:
            freq[nums] += 1
        else:
            freq [nums] = 1
    return  freq

numberss = [11,55,66,44,44,3,4,4,4,4]

coun_freq =count_frequency(numberss)
print(coun_freq)