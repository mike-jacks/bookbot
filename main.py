from stats import get_num_words, count_characters, sorted_word_counts
import sys

def get_book_text(filepath: str) -> str:
    try:
        with open(filepath) as f:
            file_contents = f.read()
    except Exception as e:
        print(f"Unable to open '{filepath}'. This is not a valid text file.")
    return file_contents

def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_filepath = args[1]
    frankenstein_text = get_book_text(book_filepath)
    num_words = get_num_words(frankenstein_text)
    char_count = count_characters(frankenstein_text)
    char_list_dict = sorted_word_counts(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in char_list_dict:
        char: str = char_dict["char"]
        if char.isalpha():
            print(f"{char_dict["char"]}: {char_dict["num"]}")
    print("============= END ===============")

if __name__ == "__main__":
    main()