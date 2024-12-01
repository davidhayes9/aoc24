with open('day1.input', 'r') as f:
    file_input = f.readlines()

left_column = []
right_column = []
for line in file_input:
    left, right = line.split()
    left_column.append(left)
    right_column.append(right)

distance = 0
for l, r in zip(sorted(left_column), sorted(right_column)):
    distance += abs(int(l) - int(r))

print(f'{distance=}')

simlarity_score = 0
for num in left_column:
    times = right_column.count(num)
    simlarity_score += (int(num) * times)

print(f'{simlarity_score=}')