def count_words(text):
    num_words = 0
    word_list = text.split()
    num_words = len(word_list)
    return num_words

def count_characters(text):
    chars = text.lower()
    char_count = {}
    for char in chars:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def sort_on(items):
    return items["num"]

def sort_list(char_dict):
    char_list = []
    for char in char_dict:
        if char.isalpha():
            char_list.append({"char" : char, "num" : char_dict[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list