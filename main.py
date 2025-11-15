import sys
from stats import *

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)      

def main():
    file_path = sys.argv[1]
    words = word_count(file_path)
    char_dict = char_count(file_path)
    sorted_dict = sorted_list(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for dict in sorted_dict:
        if dict["char"].isalpha():    
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main()

