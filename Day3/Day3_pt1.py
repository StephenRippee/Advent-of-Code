"""
Load lines 1, 2, and 3
if you reach a number, save what spaces it occupies
search each space to the left and right
Then search the previous line around the same spots, +1 and -1 space
Same for next line
If, at any point in the process you encounter a non period non number, save the number and move on
"""

import re

def hasNeighbor(match, start_view, top_line, middle_line, bottom_line):
    
    left = start_view + match.start() - 1
    right = start_view + match.end() + 1

    if left < 0:
        left = 0
    if right >= len(middle_line):
        right = len(middle_line) - 1

    neighbors = top_line[left:right] \
    + middle_line[left:right] \
    + bottom_line[left:right]
    print(top_line[left:right])
    print(middle_line[left:right])
    print(bottom_line[left:right])

    symbols = re.findall(r'[^.0-9]', neighbors)

    if len(symbols) > 0:
        return True
    else:
        print("skipped: " + str(match.group()))
        return False


def analyzeLine(top_line, middle_line, bottom_line):

    part_number = 0
    global part_number_sum
    start_view = 0

    match = re.search(r'\d+', middle_line)
    while match != None:
        print(match)
        if hasNeighbor(match, start_view, top_line, middle_line, bottom_line):
            part_number = int(match.group())
            part_number_sum = part_number_sum + part_number
            print("tally: " + str(part_number_sum) + "\n")
        
        start_view = start_view + match.end()
        match = re.search(r'\d+', middle_line[start_view:])


with open("Day3\Day3_input.txt") as input_text:
    part_number_sum = 0

    # Analyze first line
    top_line = "." * 150
    middle_line = input_text.readline().rstrip()
    bottom_line = input_text.readline().rstrip()
    analyzeLine(top_line, middle_line, bottom_line)

    # Analyze middle lines
    for newline in input_text.readlines():
        top_line = middle_line
        middle_line = bottom_line
        bottom_line = newline.rstrip()
        analyzeLine(top_line, middle_line, bottom_line)
    
    # Analyze last line
    top_line = middle_line
    middle_line = bottom_line
    bottom_line = "." * 150
    analyzeLine(top_line, middle_line, bottom_line)
        

