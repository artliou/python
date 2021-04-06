# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
import re

file = open("regex_sum_256930.txt", "r")
# file = open("regex_sum_42.txt", "r")

integers = re.findall('[0-9]+', file.read())
#print(file.read())
total = 0
count = 0
for integer in integers:
    count += 1
    # newInt = float(integer)
    # total += int(newInt)
    total += int(integer)


print("Count", count)
print(total)
