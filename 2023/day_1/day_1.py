def first_and_last(input_string):
    first_digit = next((char for char in input_string if char.isdigit()), None)

    reversed_string = input_string[::-1]
    last_digit = next((char for char in reversed_string if char.isdigit()), None)

    return first_digit, last_digit


def main():
    result = 0

    with open("input.txt", "r") as file:
        data = file.readlines()

    for line in data:
        first, last = first_and_last(line)
        
        if first is not None and last is not None:
            result += int(str(first) + str(last))

    print(result)

if __name__ == "__main__":
    main()