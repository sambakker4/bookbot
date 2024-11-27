def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    text = text.lower()
    hashmap = {}

    for char in text:
        hashmap[char] = 1 + hashmap.get(char, 0)
    return hashmap
def sort_on(dict):
    return dict["num"]

with open("books/frankenstein.txt") as f:
    filecontents = f.read()
    chars = count_chars(filecontents)
    words = count_words(filecontents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} found in the document\n")

    chars_list = []
    for key, value in chars.items():
        chars_list.append({"char": key, "num": value})
    
    chars_list.sort(reverse=True, key=sort_on)

    for char_dict in chars_list:
        if not (char_dict["char"]).isalpha():
            continue
        print(f"The '{char_dict["char"]}' character was found {char_dict["num"]} times")

    print("--- End report ---")
print("hello world")