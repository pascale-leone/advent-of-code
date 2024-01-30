import string

first = []
second = []
key = {}

groups = []

def alpha_key():
    alpha = list(string.ascii_lowercase)
    alpha.extend(list(string.ascii_uppercase))
    for i in range(52):
        key[alpha[i]] = i+1

def list_parse(lines):
    for line in lines:
        half_one = line[:(len(line)//2)]
        half_two = line[(len(line))//2:]
        first.append(half_one)
        second.append(half_two)

def priority_sum():
    sum = 0
    for x in range(len(first)):
        i = 0
        while i == 0:
            for j in first[x]:
                for k in second[x]:
                    if j == k:
                        i = key[j]
        sum += i
    print(sum)

def elf_groups(lines):
    new_lines = []
    for line in lines:
        new_line = line.strip()
        new_lines.append(new_line)
    i = 0
    while i < len(new_lines):
        g = []
        g.append(new_lines[i])
        g.append(new_lines[i+1])
        g.append(new_lines[i+2])
        groups.append(g)
        i += 3

def priority_sum3():
    sum = 0
    for x in groups:
        i = 0
        while i == 0:
            for j in x[0]:
                for k in x[1]:
                    if j == k:
                        for l in x[2]:
                            if j == l:
                                i = key[j]
        sum += i
    print(sum)

def main():
    file = open("input.txt")
#    file = open("small_input.txt")
    lines = file.readlines()
    file.close
    
    list_parse(lines)
    alpha_key()
    priority_sum()

    elf_groups(lines)
    priority_sum3()


if __name__ == main():
    main()
