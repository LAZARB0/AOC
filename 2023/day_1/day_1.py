import re

spelled_digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def first_and_last(input_string):
    first_digit = next((char for char in input_string if char.isdigit()), None)

    reversed_string = input_string[::-1]
    last_digit = next((char for char in reversed_string if char.isdigit()), None)

    return first_digit, last_digit

def part_two_conversion(line):
    
    for word, digit in spelled_digits.items():
        line = line.replace(word[:-1], digit)

    return line

def main():
    result = 0

    with open("input.txt", "r") as file:
        data = file.readlines()

    for line in data:
        converted_line = part_two_conversion(line)
        first, last = first_and_last(converted_line)
        
        if first is not None and last is not None:
            result += int(str(first) + str(last))

    print(result)


if __name__ == "__main__":
    main()