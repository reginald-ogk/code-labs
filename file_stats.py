"""
This script reads a text file specified by the user and calculates:
1. The number of lines in the file.
2. The number of words in the file.
3. The number of characters in the file, excluding spaces and newlines.
"""

filename = input("Enter a file name: ")

try:    
    with open(filename, 'r') as f:
        content = f.read()
        print(content)

    line_count = content.count('\n') + (1 if content else 0)
    word_count = len(content.split())
    no_spaces = content.replace(" ", "").replace("\n", "")
    char_count = len(no_spaces)

    print(f"Number of lines: {line_count}")
    print(f"Number of words: {word_count}")
    print(f"Number of characters (excluding spaces and newlines): {char_count}")

except FileNotFoundError:
    print("File not found.")