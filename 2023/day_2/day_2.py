def part_one_calculation(data):

    possible_game_ids = []

    reds = 12
    greens = 13
    blues = 14

    for line in data:
        game_id, game_data = line.strip().split(":")
        game_sets = game_data.split(";")

        possible_game_void = True

        for game_set in game_sets:
            possible_set_void = True
            colors = game_set.split(",")
            for color in colors:
                amount, color = color.strip().split(" ")
                if color == "red" and int(amount) > reds:
                    possible_set_void = False
                elif color == "green" and int(amount) > greens:
                    possible_set_void = False
                elif color == "blue" and int(amount) > blues:
                    possible_set_void = False

            if possible_set_void == False:
                possible_game_void = False
                break

        if possible_game_void:
            possible_game_ids.append(game_id)

    result = 0
    for game in possible_game_ids:
        game_string, id = game.strip().split(" ")
        result += int(id)

    print("Part one result:", result)

def part_two_calculation(data):

    total_power = 0

    for line in data:
        game_id, game_data = line.strip().split(":")
        game_sets = game_data.split(";")

        game_lowest_green = 1
        game_lowest_blue = 1
        game_lowest_red = 1

        for game_set in game_sets:

            colors = game_set.split(",")
            
            for color in colors:
                amount, color = color.strip().split(" ")
                if color == "red" and game_lowest_red < int(amount):
                    game_lowest_red = int(amount)
                elif color == "blue" and game_lowest_blue < int(amount):
                    game_lowest_blue = int(amount)
                elif color == "green" and game_lowest_green < int(amount):
                    game_lowest_green = int(amount)

        total_power += game_lowest_red * game_lowest_blue * game_lowest_green     

    print("Part two result:", total_power)

def main():
    with open("input.txt", "r") as file:
        data = file.readlines()

    part_one_calculation(data)

    part_two_calculation(data)

if __name__ == "__main__":
    main()