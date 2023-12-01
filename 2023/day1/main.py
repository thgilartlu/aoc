import re

def spellDigits(line, digit_map):
    words = line.split()
    processed_words = []

    for word in words:
        processed_word = ''
        while word:
            match_found = False
            for digit_word, digit in digit_map.items():
                if word.startswith(digit_word):
                    processed_word += digit
                    word = word[len(digit_word):]
                    match_found = True
                    break
            if not match_found:
                processed_word += word[0]
                word = word[1:]
        processed_words.append(processed_word)

    return ''.join(processed_words)

def findCalibrationValue(line, digit_map):
    original_line = line
    line = spellDigits(line, digit_map)
    print(f"Original line: {original_line}, After replacement: {line}")

    digits = re.findall(r'\d', line)
    if digits:
        firstDigit = digits[0]
        lastDigit = digits[-1]
        print(f"First digit: {firstDigit}, Last digit: {lastDigit}")
        return int(firstDigit + lastDigit)
    return 0

def sumCalibrationValue(file_path, digit_map):
    total = 0
    with open(file_path, 'r') as file:
        for line in file:
            total += findCalibrationValue(line.strip(), digit_map)
    return total
digit_map = {
    'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'   
}

inputFile = '2023\day1\input.txt'

print(f"Total Calibration Value: {sumCalibrationValue(inputFile, digit_map)}")