from stats import *


# ============ BOOKBOT ============
# Analyzing book found at books/frankenstein.txt...
# ----------- Word Count ----------
# Found 75767 total words
# --------- Character Count -------
# e: 44538
# t: 29493
# a: 25894
# o: 24494
# i: 23927
# n: 23643
# s: 20360
# r: 20079
# h: 19176
# d: 16318
# l: 12306
# m: 10206
# u: 10111
# c: 9011
# f: 8451
# y: 7756
# w: 7450
# p: 5952
# g: 5795
# b: 4868
# v: 3737
# k: 1661
# x: 691
# j: 497
# q: 325
# z: 235
# æ: 28
# â: 8
# ê: 7
# ë: 2
# ô: 1
# ============= END ===============


def main():
    print("============ BOOKBOT ============")

    book_path = "books/frankenstein.txt"
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

