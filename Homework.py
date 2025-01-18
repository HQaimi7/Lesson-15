class RomanConverter:
    def __init__(self, number):
        # Initialize with the integer number
        if not (0 < number < 4000):
            raise ValueError("Number must be between 1 and 3999")
        self.number = number

    def to_roman(self):
        # Roman numerals list of tuples: symbols and their corresponding values
        roman_numerals = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        # Resultant Roman numeral
        result = ""
        num = self.number

        # Process the number and build the Roman numeral string
        for value, numeral in roman_numerals:
            while num >= value:
                result += numeral
                num -= value

        return result


# Example usage
if __name__ == "__main__":
    # Create an instance of RomanConverter with an integer
    converter = RomanConverter(1987)

    # Convert to Roman numeral
    print("Roman numeral of 1987 is:", converter.to_roman())

    # Create another instance with another integer
    converter2 = RomanConverter(3000)
    print("Roman numeral of 3000 is:", converter2.to_roman())
