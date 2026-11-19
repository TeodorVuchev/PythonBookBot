from stats import get_book_words, book_characters, chars_dict_to_sorted_list
import sys

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text().lower()
    book_words_count = get_book_words(book_text)
    characters_in_book: dict[str,int] = book_characters(book_text)
    sorted_characters: list[tuple[str,int]] = chars_dict_to_sorted_list(characters_in_book)
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {book_words_count} total words")
    print(f"--------- Character Count -------")
    for character in sorted_characters:
        if character[0].isalpha():
            print(f"{character[0]}: {character[1]}")
    print(f"============= END ===============")
    print(sys.argv)

def get_book_text() -> str:
    with open(sys.argv[1]) as f:
        file_contents:str = f.read()
    return file_contents


main()