# This program takes an input of a roman numeral and returns the arabic numeral
# See LeetCode Problem: https://leetcode.com/problems/roman-to-integer/ 
# This code was written by Andrew Teubl on April 27, 2023

class RomanNumeralConverter:
    def __init__(self):
        self.roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def roman_to_decimal(self, roman_numeral):
        decimal_num = 0
        for i in range(len(roman_numeral)):
            if i > 0 and self.roman_map[roman_numeral[i]] > self.roman_map[roman_numeral[i - 1]]:
                decimal_num += self.roman_map[roman_numeral[i]] - 2 * self.roman_map[roman_numeral[i - 1]]
            else:
                decimal_num += self.roman_map[roman_numeral[i]]
        return decimal_num

if __name__ == '__main__':
    converter = RomanNumeralConverter()
    s = input("Enter a roman numeral ")
    r = converter.roman_to_decimal(s)
    print(r)