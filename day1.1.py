f = open('puzzle1.1.txt')

diff = 0
leftList = []
rightList = []
for line in f:
    nums = line.split()
    leftList.append(int(nums[0]))
    rightList.append(int(nums[1]))

# There is definitely a faster way to do this, however, the list is small enough that it doesnt matter
correctedLeft = sorted(leftList)
correctedRight = sorted(rightList)

for i in range(len(correctedLeft)):
    diff += abs(correctedLeft[i] - correctedRight[i])

print(diff)
f.close()
