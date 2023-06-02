with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()


def count_characters(words):
    characters = {}
    for word in words:
        for character in word:
            if character.islower():
                if character in characters:
                    characters[character] += 1
                else:
                    characters[character] = 1
    return characters


def print_report(characters):
    print(f"{len(words)} words found in the document")
    for character, count in sorted(characters.items(), key=lambda item: item[1], reverse=True):
        print(f"The '{character}' character was found {count} times")


print_report(count_characters(words))
