def getSafeReports():
    f = open('puzzle2.txt')
    safe_reports = 0
    for report in f:
        curr_rep = report.split()
        direction = True
        safe_reports += 1

        if int(curr_rep[0]) > int(curr_rep[1]):
            direction = False

        for i in range(len(curr_rep) - 1):
            if direction:
                if int(curr_rep[i]) >= int(curr_rep[i + 1]) or abs(int(curr_rep[i]) - int(curr_rep[i + 1])) > 3:
                    safe_reports -= 1
                    break
            else:
                if int(curr_rep[i]) <= int(curr_rep[i + 1]) or abs(int(curr_rep[i]) - int(curr_rep[i + 1])) > 3:
                    safe_reports -= 1
                    break
    f.close()
    print('The number of safe reports are: ' + str(safe_reports))


getSafeReports()
