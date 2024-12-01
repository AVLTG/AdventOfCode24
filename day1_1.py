def makeLists():
    f = open('puzzle1.txt')

    leftList = []
    rightList = []
    for line in f:
        nums = line.split()
        leftList.append(int(nums[0]))
        rightList.append(int(nums[1]))
    f.close()
    return leftList, rightList


def difference():
    diff = 0
    leftList, rightList = makeLists()
    # There is definitely a faster way to do this, however, the list is small enough that it does not matter
    correctedLeft = sorted(leftList)
    correctedRight = sorted(rightList)

    for i in range(len(correctedLeft)):
        diff += abs(correctedLeft[i] - correctedRight[i])

    print('Difference of the two lists: ' + str(diff))


difference()
