def char_frequency_counter(s):
    # Initialize hash list for 26 lowercase letters
    hash_list = [0] * 26
    # Count frequency of each character
    for char in s:
        index = ord(char) - 97
        hash_list[index] += 1
    # Get unique characters
    unique_chars = set(s)
    # Print frequency of each unique character
    for char in unique_chars:
        print(f"{char} = {hash_list[ord(char) - 97]}")
# Example usage
if __name__ == "__main__":
    input_string = "abaayzxxyzsgb"
    print(f"Character frequencies in: '{input_string}'\n")
    char_frequency_counter(input_string)
