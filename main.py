import sys
from stats import get_num_words, get_characters_with_count, get_sorted_characters

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    file_contents = get_book_text(path_to_book)
    num_words = get_num_words(file_contents)
    chars_dict = get_characters_with_count(file_contents)
    sorted_chars_list = get_sorted_characters(chars_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_item in sorted_chars_list:
        character = char_item["char"]
        count = char_item["num"]
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")



if __name__ == "__main__":
    main()