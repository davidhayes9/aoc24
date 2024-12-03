with open('day2.input', 'r') as f:
    file_input = f.readlines()


def check_level(report):
    # check that all levels in report differ by 1 - 3

    count = 0
    for i in range(len(report) - 1):
        if abs(int(report[i]) - int(report[i + 1])) in [1, 2, 3]:
            count += 1
    return count == (len(report) - 1)


def check_inc_dec(report):
    # check if all levels are either increasing or decreasing

    i, j = 0, 0
    count_inc, count_dec = 0, 0
    for ii in range(len(report) - 1):
      
        first = report[ii]
        second = report[ii + 1]
        
        if first < second: 
            i += 1
            count_inc += 1
        
        if first > second:
            j += 1
            count_dec += 1

    if count_dec == (len(report) - 1) or count_inc == (len(report) - 1):
            return check_level(report)


safe_reports_part1, safe_reports_part2 = 0, 0
for report in file_input:

    int_report = [int(x) for x in report.split()]
    if check_inc_dec(int_report):
        safe_reports_part1 += 1

    else:
        # test with the last element popped
        last_list = list(int_report)
        last_list.pop()
        if check_inc_dec(last_list):
            safe_reports_part2 += 1
        else:
            # brute-force by testing it each time with one element removed, break the look if safe report is found 
            for el in range(len(int_report) - 1):
                new_list = list(int_report)
                new_list.pop(el)
                if check_inc_dec(new_list):
                    safe_reports_part2 += 1
                    break


print(f'{safe_reports_part1=}')

safe_reports_part2 += safe_reports_part1
print(f'{safe_reports_part2=}')