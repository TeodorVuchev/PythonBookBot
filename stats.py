# Finds the count of words inside the  book string
def get_book_words(book_text:str) -> int:
    book_words = book_text.split()
    return len(book_words)

# Isolates each character in the book string into number of times it appears as a dict with int
def book_characters(book_text:str) -> dict[str,int]:
    characters_by_count: dict[str,int] = {}
    for character in book_text:
        if characters_by_count.get(character) is None:
            characters_by_count[character] = 1
            continue
        characters_by_count[character] += 1    
    return characters_by_count

# helper function for character sorting to be used as key to ensure the characters count is the sorting value
def sort_on(character: tuple[str, int]) -> int:
    return character[1]

# order the character occurrences by most to least via a list and tuples
def chars_dict_to_sorted_list(characters_by_count: dict[str, int]) -> list[tuple[str, int]]:
    chars_sorted: list[tuple[str, int]] = []
    for character in characters_by_count:
        char_tuple = (character, characters_by_count[character])
        chars_sorted.append(char_tuple)
    chars_sorted = sorted(chars_sorted, key = sort_on ,reverse = True)
    return chars_sorted