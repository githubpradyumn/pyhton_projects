def roman_to_int(numeral):  
    # Define a function named 'roman_to_int' that takes one parameter 'numeral', representing a Roman numeral string.

    # Dictionary for Roman numerals
    roman_dict = {
        'M': 1000, 'D': 500, 'C': 100, 'L': 50, 
        'X': 10, 'V': 5, 'I': 1
    }
    # A dictionary that maps each Roman numeral symbol to its corresponding integer value.

    final_answer = 0
    # Initialize a variable 'final_answer' to store the final converted integer value.

    # Loop through the numeral string
    for i in range(len(numeral)):
        # Iterate over each character in the input 'numeral' string. 
        # 'i' is the index of the current character being processed.

        # Check if the character is a valid Roman numeral
        if numeral[i] not in roman_dict:
            print(f"Invalid character '{numeral[i]}' in input. Please enter valid Roman numerals.")
            return  # Exit the function if an invalid character is found.
        # This checks if the current character is not a valid Roman numeral by comparing it to the keys in 'roman_dict'.
        # If an invalid character is found, an error message is printed, and the function returns early.

        # If current numeral is less than the next one, subtract it
        if i + 1 < len(numeral) and roman_dict[numeral[i]] < roman_dict[numeral[i + 1]]:
            final_answer -= roman_dict[numeral[i]]
        # This checks if the current numeral is smaller than the next one (indicating a subtractive pair, like IV for 4).
        # If so, the value of the current numeral is subtracted from the 'final_answer'.

        else:
            final_answer += roman_dict[numeral[i]]
        # If the current numeral is not part of a subtractive pair, its value is simply added to 'final_answer'.

    # Print the final converted value
    print(f"The Roman numeral {numeral} translates to: {final_answer}")
    # Output the final integer value after all the Roman numerals have been processed.

# Taking user input
numeral_input = input("Enter the Roman numerals you want to convert: ")
# Ask the user to input a string of Roman numerals, which is stored in the variable 'numeral_input'.

roman_to_int(numeral_input)
# Call the 'roman_to_int' function with the user input to perform the conversion.
