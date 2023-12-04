import re

# Finds impossible games due to too many cubes of a given color
# Returns true if the maximum number of cubes seen is fewer than the Elf asks for, false otherwise
def determinePossibleForColor(game_string: str, color: str, max_allowed_of_color: int) -> bool:
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

    print(max_cubes_pulled)
    if max_cubes_pulled <= max_allowed_of_color:
        return True
    else:
        return False
    
# Iterates through all games and adds up the IDs of possible ones       
with open("Day2\Day2_test.txt") as input_text:

    sum_of_successful_game_IDs = 0
    line_number = 1
    
    for line in input_text.readlines():

        if determinePossibleForColor(line, "red", 12) \
        and determinePossibleForColor(line, "green", 13) \
        and determinePossibleForColor(line, "blue", 14):
            
            print("succeeded game: " + str(line_number))
            sum_of_successful_game_IDs = sum_of_successful_game_IDs + line_number

        else:

            print("failed game: " + str(line_number))

        line_number += 1


print(sum_of_successful_game_IDs)

