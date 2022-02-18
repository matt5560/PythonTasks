symbol_index = 0
list_result = []
strings = []
mark = False
slash = False

lines = int(input("строки: "))
for i in range(lines):
    program = input()
    while program[symbol_index] == " ":
        list_result.append(" ")
        symbol_index += 1
    for j in range(symbol_index, len(program)):
        if not slash:
            if program[j] == "'":
                list_result.append(program[j])
                mark = not mark
            elif program[j] == "\\":
                list_result.append(program[j])
                slash = True
            elif program[j] == "#":
                if mark:
                    list_result.append(program[j])
                else:
                    break
            elif program[j] == " ":
                if mark == True:
                    list_result.append(program[j])
                else:
                    if j + 1 != len(program):
                        if program[j + 1] == " ":
                            list_result.append("")
                        else:
                            list_result.append(program[j])
            else:
                list_result.append(program[j])
        else:
            slash = False
            list_result.append(program[j])
    strings.append("".join(list_result))
    list_result = []
    mark = False
    slash = False
    symbol_index = 0

for i in strings:
    print(i)