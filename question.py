# Function to find the length of the longest substring without repeating characters.
def longestUniqueSubstr(str):
    n = len(str)
    max_length = 0
    max_start = 0
    start = 0
    char_index = {}

    for i in range(n):
        if str[i] in char_index and char_index[str[i]] >= start:
            start = char_index[str[i]] + 1

        char_index[str[i]] = i

        if i - start + 1 > max_length:
            max_length = i - start + 1
            max_start = start

    return str[max_start:max_start+max_length]

# Main function to read input from the command line
if __name__ == '__main__':
    input_str = input("input: ")
    output_str = longestUniqueSubstr(input_str)
    print("output:", output_str, "length:", len(output_str))
