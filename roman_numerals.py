def to_roman(num):
    output = ""
    roman_numerals = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }

    keyss = list(roman_numerals.keys())

    for key in keyss:
        current_value = roman_numerals[key]

        # print(f"key = {key}")
        # print(f"value = {current_value}")

        while num >= current_value:
            output += key
            num -= current_value

    return output


print(to_roman(4))
print(to_roman(26))
