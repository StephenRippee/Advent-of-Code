import re

# Returns a nested list with all numbers from each side
# Written by Chat GPT
def parseCard(line):
    matches = re.search(r'(.+?)\s*\|\s*(.+)', line)
    if matches:
        # Extract numbers on the left and right of the |
        # Remove the game number from the left
        winning_numbers = re.findall(r'\b\d+\b', matches.group(1))
        winning_numbers.pop(0)
        numbers_you_have = re.findall(r'\b\d+\b', matches.group(2))

        # Convert numbers to integers if needed
        winning_numbers = list(map(int, winning_numbers))
        numbers_you_have = list(map(int, numbers_you_have))

        return winning_numbers, numbers_you_have

# Checks to see how many scratched numbers are in winning numbers
# If 1 matches, the score is one. The score doubles for each additional match
def calculateMatches(winning_numbers, numbers_you_have):
    matches = 0
    for scratched_number in numbers_you_have:
        if scratched_number in winning_numbers:
            matches += 1
            print("Match! " + str(scratched_number))
    
    return matches

with open("Day4\Day4_input.txt") as input_text:

    # Dynamically sets array size to match file
    # Pointer then reset to top of page
    scratchcards_held = [1] * sum(1 for line in input_text)
    input_text.seek(0)

    winning_numbers = ()
    numbers_you_have = ()
    matches = 0
    current_card = 0

    for line in input_text.readlines():
        if scratchcards_held[current_card] > 0:
            # Determines the amount of matched numbers of the current game
            print("For card number: " + str(current_card + 1))
            winning_numbers, numbers_you_have = parseCard(line)
            print("Numbers on the left:", winning_numbers)
            print("Numbers on the right:", numbers_you_have)
            matches = calculateMatches(winning_numbers, numbers_you_have)
            print("Current score: " + str(matches))

            # If we have X cards of the current type, adds X to the next
            # set of cards. For example, if we have 3 Card 2s and match 4 times,
            # we get 3 cards of Card 3, 4, 5, and 6
            for num in range(matches):
                if current_card + num + 1 < len(scratchcards_held):
                    scratchcards_held[current_card + num + 1] += scratchcards_held[current_card]
            print(scratchcards_held)

            current_card += 1

    print("total scratchcards earned: " + str(sum(scratchcards_held)))


