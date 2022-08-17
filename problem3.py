"""Problem 3:		
		
In this example, you'll find 4 substrings (or subsets of characters) without any repeating characters. These are “abc”, “abcd”, “b”, “b”. The longest is “abcd”, so the answer is 4.		
// Example Input: s = "abcabcdbb"		
Another example:		
// Example Input: s = "pwwkew"		
The longest substring is “wke”, so the answer is 3.
You need to find the longest substring with out repeating character
"""

import argparse
from collections import OrderedDict

def longest_substring(string):
    """ Since I don't know if the program has to be case sensitive, I'm adding an argument to
    apply lower case to the string if it needs (without -c argument, "A" and "a" are considered
    different charecters and will be on the final substring).
    """

    """I'm using an OrderedDict because Sets are not an ordered python data structure, so
    the final substring would probably end up in the wrong order."""
    final_substring = OrderedDict()

    for character in string:
        final_substring[character] = None

    processed_final_substring = "".join(
        final_substring.keys()
    )
    return f"Original string: {string}, processed substring: {processed_final_substring}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Prints the longest substring without repeating characters"
    )
    parser.add_argument("-s", "--String", help="The string to be processed")
    parser.add_argument("-c", "--caseinsensitive", action=argparse.BooleanOptionalAction)
    arguments = parser.parse_args()

    if arguments.String:
        string = arguments.String
        if arguments.caseinsensitive:
            string = string.lower()
        print(longest_substring(string))
    else:
        print("No string given, so printing some examples:")
        print(longest_substring("aasswwdd"))
        print(longest_substring("jjwerr"))
