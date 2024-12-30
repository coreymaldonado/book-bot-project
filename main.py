def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)

    file_contents = file_contents.lower()

    # Find and return the word count of the book
    word_count = len(file_contents.split())
    print(f'Frankenstein contains {word_count} words. \n')

    # Find and return the count of each character contained within the book
    file_characters = list(file_contents)
    char_dict = {}
    for char in file_characters:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    # Use the created char dictionary to display how many times each letter was found

    sorted_char_dict = {k: char_dict[k] for k in sorted(char_dict)}
    # new_dictionary.sort(reverse=True, key=)

    for char in sorted_char_dict:
        if char.isalpha():
            print(f'The character {char} was found {char_dict[char]} times.')


main()
