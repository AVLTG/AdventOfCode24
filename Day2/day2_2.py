def getTolerantSafeReports():
    f = open('puzzle2.txt')
    safe_reports = 0
    for report in f:
        curr_rep = report.split()
        direction = getDirection(curr_rep)

        if not check(curr_rep, direction):
            for i in range(len(curr_rep)):
                modified_rep = curr_rep.copy()
                modified_rep.pop(i)
                direction = getDirection(modified_rep)
                if check(modified_rep, direction):
                    safe_reports += 1
                    break
                else:
                    pass
        else:
            safe_reports += 1
    f.close()
    print('The number of safe reports are: ' + str(safe_reports))


def getDirection(rep):
    if int(rep[0]) > int(rep[1]):
        return False
    return True


def check(rep, dire):
    for j in range(len(rep)-1):
        if dire:
            if int(rep[j]) >= int(rep[j + 1]) or abs(int(rep[j]) - int(rep[j + 1])) > 3:
                return False
        else:
            if int(rep[j]) <= int(rep[j + 1]) or abs(int(rep[j]) - int(rep[j + 1])) > 3:
                return False
    return True


getTolerantSafeReports()
