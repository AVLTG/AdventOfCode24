import re


def calculateUncorruptedMults():
    f = open('puzzle3.txt')
    total = 0
    mixedList = []
    for line in f:
        nums = re.findall("mul\((\d{1,3}),(\d{1,3})\)", line)
        mixedList.extend(nums)

    for i in mixedList:
        total += int(i[0]) * int(i[1])

    print(total)


calculateUncorruptedMults()
