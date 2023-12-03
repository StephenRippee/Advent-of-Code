
"""
Day 2 Advent of code

The code reads a file where each line has a "calibration number"
hidden somewhere in the string. The calibration number is a 
2 digit number composed of the first number and last number of 
the string. The goal is to find the sum of all calibration numbers
Day 2 is an extension of Day 1. Now spelled out numbers also apply

Ex:
two1nine -> 29
eightwothree -> 83
abcone2threexyz -> 13
xtwone3four -> 24
4nineeightseven2 -> 42
zoneight234 -> 14
7pqrstsixteen -> 76
Sum 281
"""

# Returns the number at the given position
# If no number is found, returns -1
def getNumberAtPosition(i, current_line) -> int:
    number_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    if current_line[i].isdigit():
        return int(current_line[i])
    else:
        for y in range(len(number_words)):
            if current_line.startswith(number_words[y], i, len(current_line)):
                return y+1      
    return -1

#Function for determining the calibration number
def getCalibrationValue(current_line) -> int:

    # -1 represents no number found
    first_digit = -1
    last_digit = -1

    for i in range(len(current_line)):
        position_number = getNumberAtPosition(i, current_line)
        if first_digit == -1:
            first_digit = position_number
            last_digit = first_digit
        elif position_number != -1:
            last_digit = position_number
    
    if first_digit == -1 or last_digit == -1:
        raise ValueError("Line contains no numbers")
    else:
        return first_digit*10 + last_digit


"""
Loops line by line until the end of the document
each line is fed to getCalibrationValue and each calibration number
is summed
"""
input_text = open("Advent of Code\Day1_input.txt", 'r') 
calibration_sum = 0
current_line = input_text.readline().rstrip()

while current_line != "":
    print(current_line)
    current_number = getCalibrationValue(current_line)
    print(current_number)
    calibration_sum += current_number
    print(calibration_sum)
    current_line = input_text.readline().rstrip()
    
# Closes file
input_text.close()