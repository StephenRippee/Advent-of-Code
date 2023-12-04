import re

# Finds impossible games due to too many cubes of a given color
# Returns true if the maximum number of cubes seen is fewer than the Elf asks for, false otherwise
def determineMaxCubeCount(game_string: str, color: str) -> int:
    max_cubes_pulled = 0
    cubes_pulled = 0
    position = 0

    # Exits when there are no more instances of the color to find
    while position != -1:

        """
            Hacky regex, I know. If I knew regex better I would have built this code around it
            and it would be much cleaner. If the color is found, the game_string is cut off where
            it found the color and the regex pulls the last number from the string. Then it moves
            on to the next time it encounters the color.
            Ex: "1 red, 82 blue" -> "1 red, 82" -> 82
        """
        position = game_string.find(color, position+1)
        if position != -1:
            matches = re.findall(r'\b\d+\b', game_string[:position])
            cubes_pulled = int(matches[-1])
            
            max_cubes_pulled = max(cubes_pulled, max_cubes_pulled)

    return max_cubes_pulled
    
# Iterates through all games and adds up the IDs of possible ones       
with open("Day2\Day2_input.txt") as input_text:

    line_number = 1
    min_red = 0
    min_green = 0
    min_blue = 0
    power = 0
    sum_of_all_powers = 0
    
    for line in input_text.readlines():

        min_red = determineMaxCubeCount(line, 'red')
        min_green = determineMaxCubeCount(line, 'green')
        min_blue = determineMaxCubeCount(line, 'blue')
        power =  min_red * min_green * min_blue
        sum_of_all_powers = sum_of_all_powers + power

        print(line.rstrip())
        print(min_red)
        print(min_green)
        print(min_blue)
        print("Power: " + str(power))
        print("Sum: " + str(sum_of_all_powers))

        line_number += 1

