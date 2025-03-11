from stats import txt_count
from stats import char_count
from stats import sort_on
import sys

def get_book_text(filepath):

    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



def main():
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}") 


    content = get_book_text(book_path)
    print(f"Found {txt_count(content)} total words")
    print("--------- Character Count -------")
    character_count = char_count(content)
    sorted_char = dict(sorted(character_count.items(), key=sort_on, reverse=True))
    sorted_alpha_chars = {char: count for char, count in sorted_char.items() if char.isalpha()}

    for char, count in sorted_alpha_chars.items():
        print(f"{char}: {count}")
    print("============= END ===============")


main()