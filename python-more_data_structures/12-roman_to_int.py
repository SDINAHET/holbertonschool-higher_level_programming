#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Mapping of Roman numerals to their values
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    length = len(roman_string)

    for i in range(length):
        # If the current numeral is smaller than the next one, subtract it
        if i < length - 1 and
        roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]:
            total -= roman_dict[roman_string[i]]
        else:
            total += roman_dict[roman_string[i]]

    return total
