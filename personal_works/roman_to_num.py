def roman_to_int(s: str) -> int:
    # Define a dictionary for Roman numeral values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Initialize the total and the previous value
    total = 0
    prev_value = 0

    # Iterate through the Roman numeral string from right to left
    for char in reversed(s):
        current_value = roman_values[char]
        # If the current value is less than the previous value, subtract it
        if current_value < prev_value:
            total -= current_value
        else:
            # Otherwise, add the current value
            total += current_value
        # Update the previous value
        prev_value = current_value

    return total

# Examples
print(roman_to_int("III"))       # Output: 3
print(roman_to_int(""))     # Output: 58
print(roman_to_int("MCMXCIV"))   # Output: 1994
