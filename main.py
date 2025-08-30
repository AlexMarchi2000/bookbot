from stats import *


import sys


def main():

    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")

    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_occurrency = count_chars(text)
    char_occurrency = dict(sorted(char_occurrency.items(), key= lambda x: x[1], reverse=True))
    for key, value in char_occurrency.items():
        print(f"{key}: {value}")

    print("============= END ===============")


main()

