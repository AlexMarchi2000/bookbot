def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


def get_num_words(text: str) -> int:
    return len(text.split())

def count_chars(text: str) -> dict[str, int]:
    occurrency: dict[str, int] = {}
    words = text.split()
    for word in words:
        for char in word:
            lower_char = char.lower()
            if lower_char in occurrency:
                occurrency[lower_char] += 1
            else:
                occurrency[lower_char] = 1
    return occurrency

