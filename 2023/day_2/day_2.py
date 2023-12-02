def main():
    with open("input.txt", "r") as file:
        data = file.readlines()

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

    print("result:", result)


if __name__ == "__main__":
    main()