def roman_to_int(numeral):
    # Dictionary for Roman numerals
    roman_dict = {
        'M': 1000, 'D': 500, 'C': 100, 'L': 50, 
        'X': 10, 'V': 5, 'I': 1
    }

    final_answer = 0
    
    # Loop through the numeral
    for i in range(len(numeral)):
        # Check if the character is a valid Roman numeral
        if numeral[i] not in roman_dict:
            print(f"Invalid character '{numeral[i]}' in input. Please enter valid Roman numerals.")
            return  # Exit the function if an invalid character is found
        
        # If current numeral is less than the next one, subtract it
        if i + 1 < len(numeral) and roman_dict[numeral[i]] < roman_dict[numeral[i + 1]]:
            final_answer -= roman_dict[numeral[i]]
        else:
            final_answer += roman_dict[numeral[i]]
    
    print(f"The Roman numeral {numeral} translates to: {final_answer}")

# Taking user input
numeral_input = input("Enter the Roman numerals you want to convert: ")
roman_to_int(numeral_input)
