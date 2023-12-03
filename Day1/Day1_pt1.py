# Day 1 Advent of code
#
# The code reads a file where each line has a "calibration number"
# hidden somewhere in the string. The calibration number is a 
# 2 digit number composed of the first number and last number of 
# the string. The goal is to find the sum of all calibration numbers
#
# Ex:
# 1abc2 -> 12
# pqr3stu8vwx -> 38
# a1b2c3d4e5f -> 15
# treb7uchet -> 77
# sum: 132


#Function for determining the calibration number
def getCalibrationValue(current_line) -> int:

    # If either digit remains -1, then there is an error
    first_digit = -1
    last_digit = -1

    for i in range(len(current_line)):
        if current_line[i].isdigit():
            first_digit = int(current_line[i])
            break
    
    for i in range(len(current_line)-1, -1, -1):
        if current_line[i].isdigit():
            last_digit = int(current_line[i])
            break
    
    if first_digit == -1 or last_digit == -1:
        raise ValueError("Line contains no numbers")
    else:
        return first_digit*10 + last_digit



# Loops line by line until the end of the document
# each line is fed to getCalibrationValue and each calibration number
# is summed
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
