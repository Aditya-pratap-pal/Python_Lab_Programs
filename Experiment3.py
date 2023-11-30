# String operations in Python

# Function to perform string operations
def perform_string_operations(input_string):
    # Length of the string
    length = len(input_string)
    print(f"Length of the string: {length}")

    # Convert the string to uppercase
    uppercase_string = input_string.upper()
    print(f"Uppercase: {uppercase_string}")

    # Convert the string to lowercase
    lowercase_string = input_string.lower()
    print(f"Lowercase: {lowercase_string}")

    # Count occurrences of a specific character in the string
    char_to_count = input("Enter a character to count: ")
    count = input_string.count(char_to_count)
    print(f"Occurrences of '{char_to_count}': {count}")

    # Check if the string starts with a specific prefix
    prefix = input("Enter a prefix to check: ")
    starts_with_prefix = input_string.startswith(prefix)
    print(f"Starts with '{prefix}': {starts_with_prefix}")

    # Check if the string ends with a specific suffix
    suffix = input("Enter a suffix to check: ")
    ends_with_suffix = input_string.endswith(suffix)
    print(f"Ends with '{suffix}': {ends_with_suffix}")

    # Find the index of a specific substring in the string
    substring = input("Enter a substring to find: ")
    index = input_string.find(substring)
    if index != -1:
        print(f"Index of '{substring}': {index}")
    else:
        print(f"'{substring}' not found in the string.")

# Example usage
user_input = input("Enter a string: ")
perform_string_operations(user_input)
