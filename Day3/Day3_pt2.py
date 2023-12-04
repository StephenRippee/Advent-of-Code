"""
Load lines 1, 2, and 3
if you reach a number, save what spaces it occupies
search each space to the left and right
Then search the previous line around the same spots, +1 and -1 space
Same for next line
If, at any point in the process you encounter a non period non number, save the number and dip
"""

import re

# determines the gear ratio of a star
# returns 0 unless there are exactly 2 numbers touching.
# Then it returns the product of those numbers
# using the star position, determine Gear Ratio moves line by line searching for numbers that
# border the star
def determineGearRatio(star_position, top_line, middle_line, bottom_line):

    # loops through the top line searching for independent numbers that touch the star
    # If it finds one, it adds it to the 

    touching_numbers = []
    touching_numbers = touching_numbers + findStarNeighbors(star_position,top_line)
    touching_numbers = touching_numbers + findStarNeighbors(star_position,middle_line)
    touching_numbers = touching_numbers + findStarNeighbors(star_position,bottom_line)

    # top_neighbors = findStarNeighbors(star_position,top_line)
    # middle_neighbors = findStarNeighbors(star_position,middle_line)
    # bottom_neighbors = findStarNeighbors(star_position,bottom_line)

    # if len(top_neighbors) > 0:
    #     touching_numbers.append(top_neighbors)
    # if len(middle_neighbors) > 0:
    #     touching_numbers.append(middle_neighbors)
    # if len(bottom_neighbors) > 0:
    #     touching_numbers.append(bottom_neighbors)
    
    print(touching_numbers)

    if len(touching_numbers) == 2:
        gear_ratio = touching_numbers[0] * touching_numbers[1]
    else:
        gear_ratio = 0
    return gear_ratio

# loops through the top line searching for independent numbers that touch the star
# when it finds one, it adds it to the list and keeps looking
# Returns the list of numbers it found
def findStarNeighbors(star_position, line):
    print("star position: " + str(star_position))
    numbers_found = []
    start_view = 0

    match = re.search(r'\d+', line)
    while match != None:


        print("potential number: ", end=" ")
        print(match)

        if star_position >= start_view + match.start() - 1 \
            and star_position <= start_view + match.end():

            numbers_found.append(int(match.group()))
        start_view = start_view + match.end()
        match = re.search(r'\d+', line[start_view:])
    
    return numbers_found


# Moves across the line and looks for stars
# When it encounters a star, it calls for the gear ratio, then adds it to the sum
def analyzeLine(top_line, middle_line, bottom_line):

    gear_ratio = 0
    global gear_ratio_sum
    star_position = 0

    match_star = re.search(r'\*', middle_line)
    while match_star != None:
        print(match_star)
        star_position = star_position + match_star.start()
        gear_ratio = determineGearRatio(star_position, top_line, middle_line, bottom_line)
        gear_ratio_sum = gear_ratio_sum + gear_ratio
        print("tally: " + str(gear_ratio_sum) + "\n")

        # for some reason, the star_position variable must be moved up by one
        # doing middle_line[star_position+1:] does NOT work
        star_position += 1 
        match_star = re.search(r'\*', middle_line[star_position:])
        print(match_star)



with open("Day3\Day3_input.txt") as input_text:
    gear_ratio_sum = 0
    line_number = 1

    # Analyze first line
    top_line = "." * 150
    middle_line = input_text.readline().rstrip()
    bottom_line = input_text.readline().rstrip()
    analyzeLine(top_line, middle_line, bottom_line)
    print(line_number)
    line_number += 1

    # Analyze middle lines
    for newline in input_text.readlines():
        print(line_number)
        top_line = middle_line
        middle_line = bottom_line
        bottom_line = newline.rstrip()
        analyzeLine(top_line, middle_line, bottom_line)
        line_number += 1
    
    # Analyze last line
    top_line = middle_line
    middle_line = bottom_line
    bottom_line = "." * 150
    analyzeLine(top_line, middle_line, bottom_line)
        

