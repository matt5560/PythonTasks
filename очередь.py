line_count = int(input())
queue = []

for i in range(line_count):
    line = input()
    name = line.split(' ')
    if 'встал в очередь' in line or 'встала в очередь' in line:
        queue.append(name[0])
    elif 'будет за тобой' in line:
        line_split = line.split('! ')
        line_split_split = line_split[1].split('будет')
        queue.append(line_split_split[0])
    elif 'хватит' in line:
        line_l = line.split(',')
        queue.remove(line_l[0])
print(queue)

