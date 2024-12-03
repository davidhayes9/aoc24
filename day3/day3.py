import re

with open('day3.input', 'r') as f:
    file_input = f.read()


def sum_instruct(mul_instructs):

    total = 0
    for num in re.findall(r'mul\(([0-9]{0,3},[0-9]{0,3})\)', mul_instructs):
        first, second = num.split(',')
        total += (int(first) * int(second))
    
    return total


print(f'Part1 = {sum_instruct(file_input)}')

# regex to capture everything(including new line) from don't() untill do()
regex_remove_donts = r'(don\'t\(\)(.|\n)*?)do\(\)'

new_out = re.sub(regex_remove_donts, "", file_input)
print(f'Part2 =  {sum_instruct(new_out)}')
