import re

def findCalibrationValue(line):
    digits = re.findall(r'\d', line)
    
    if digits:
        firstDigit = digits[0]
        lastDigit = digits[-1]
        return int(firstDigit + lastDigit)
    return 0

def sumCalibrationValue(file_path):
    total = 0
    with open(file_path, 'r') as file:
        for line in file:
            total += findCalibrationValue(line.strip())
    return total

inputFile = '2023\day1\input.txt'

print(sumCalibrationValue(inputFile))