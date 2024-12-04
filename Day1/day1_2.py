from day1_1 import makeLists


def similarity():
    simi = 0
    leftList, rightList = makeLists()
    for i in range(len(leftList)):
        total = 0
        for j in range(len(rightList)):
            if leftList[i] == rightList[j]:
                total += 1
        simi += total * leftList[i]

    print('Similarity of the two lists: ' + str(simi))


similarity()
