\# Longest Substring Without Repeating Characters

This is a Python script that reads a string from the command line and
finds the longest substring in it that doesn\'t contain any duplicate
characters. If there are multiple substrings of equal length that
satisfy the condition, returning any of these substrings would be a
valid answer.

\## Usage

1\. Make sure you have Python installed on your system. 2. Open a
terminal or command prompt in the directory where the \`solution.py\`
script is located. 3. Run the script using the command: \$ python3
solution.py

4\. Enter your desired input string when prompted.

\## Input Format

The first line contains a single string of input.

\## Output Format

The output will be displayed after \'output:\', including the length of
the longest substring without repeating characters.

\## Examples

\### Example 1: \$ python3 solution.py input: ABBCDDEFGHII output:
DEFGHI length: 6

\### Example 2: \$ python3 solution.py input: AABBCCD output: AB length:
2 output: BC length: 2 output: CD length: 2 \<any of the above 3 would
be accepted\>

\### Example 3: \$ python3 solution.py input: ABCD output: ABCD length:
4

The longestUniqueSubstr function uses a single loop to traverse the
input string. Use a char_index dictionary to keep track of the last
index at which each character was seen. The start pointer keeps track of
the starting index of the current window, and whenever a repeating
character is encountered, move the window\'s left boundary (start) one
step to the right. Update the max_length and max_start variables
whenever we find a longer substring without any duplicate characters.

To minimize processing time and memory usage, use a sliding window
approach with two pointers to traverse the input string only once. This
will ensure a linear time complexity and constant space complexity.

Time Complexity: The time complexity of the longestUniqueSubstr function
is O(n), where n is the length of the input string. This is because we
traverse the input string only once with the single loop.

Space Complexity: The space complexity of the longestUniqueSubstr
function is O(k), where k is the size of the character set (256 for
ASCII characters). This is because the function uses a dictionary
(char_index) to keep track of characters in the current window, and the
dictionary can have a maximum size of k. The additional variables used
in the function (max_length, max_start, start) are all scalar variables
that take constant space. The main function uses a few more scalar
variables (input_str and output_str), which also take constant space.
Therefore, the space used by the algorithm remains constant, resulting
in an overall space complexity of O(1).

This code, in conclusion, satisfies the required criteria of reducing
both processing time and memory use. It employs a single loop to
efficiently discover the largest substring without repeating any
characters, and regardless of the input size, it only consumes a fixed
amount of extra RAM.
