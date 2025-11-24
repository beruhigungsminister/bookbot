import sys
from stats import count_words
from stats import count_characters
from stats import sort_list

word_count = 0
char_count = {}
sorted_ls_of_dict = []
file_location = ""


def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)
    sorted_ls_of_dict = sort_list(char_count)
    #return print(word_count), print(char_count)
    #print(sort_list(char_count))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_location}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in sorted_ls_of_dict:
        character = i["char"]
        count = i["num"]
        print(f"{character}: {count}")

def get_file_path():
    global file_location
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_location = sys.argv[1]

def main():
    get_file_path()
    get_book_text(file_location)

main()