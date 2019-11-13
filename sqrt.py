import math

sum_sqrt = 0
dictionary = {}
with open('100.txt') as f:
    for line in f:
        complete_number = ''
        for character in line:
            no_spaces_line = line.strip()
            if character != ',':
                complete_number += character
            else:
                if no_spaces_line not in dictionary:
                    dictionary[no_spaces_line] = int(complete_number)
                else:
                    dictionary[no_spaces_line] += int(complete_number)
                complete_number = ''
        if no_spaces_line not in dictionary:
            dictionary[no_spaces_line] = int(complete_number)
        else:
            dictionary[no_spaces_line] += int(complete_number)

for i in dictionary:
    sum_sqrt += math.sqrt(dictionary[i])


print(sum_sqrt)
