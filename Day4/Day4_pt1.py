import re

# Returns a nested list with all numbers from each side
# Written by Chat GPT
def parseCard(line):
    matches = re.search(r'(.+?)\s*\|\s*(.+)', line)
    if matches:
        # Extract numbers on the left and right of the |
        winning_numbers = re.findall(r'\b\d+\b', matches.group(1))
        winning_numbers.pop(0)
        numbers_you_have = re.findall(r'\b\d+\b', matches.group(2))

        # Convert numbers to integers if needed
        winning_numbers = list(map(int, winning_numbers))
        numbers_you_have = list(map(int, numbers_you_have))

        return winning_numbers, numbers_you_have
    else:
        print("No match found.")

# Checks to see how many scratched numbers are in winning numbers
# If 1 matches, the score is one. The score doubles for each additional match
def calculateScore(winning_numbers, numbers_you_have):
    matches = 0
    for scratched_number in numbers_you_have:
        if scratched_number in winning_numbers:
            matches += 1
            print("Match! " + str(scratched_number))
    
    if matches > 0:
        return 2 ** matches / 2
    else:
        return 0

with open("Day4\Day4_input.txt") as input_text:

    winning_numbers = ()
    numbers_you_have = ()
    score_sum = 0

    for line in input_text.readlines():
        winning_numbers, numbers_you_have = parseCard(line)
        # Print the results
        print("Numbers on the left:", winning_numbers)
        print("Numbers on the right:", numbers_you_have)
        score_sum += calculateScore(winning_numbers, numbers_you_have)
        print("Current score: " + str(score_sum))
    
