import sys

from stats import get_num_words
from stats import char_counts
from stats import sort_chars

def get_book_text(filename):
    with open(filename) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_to_sort = "./books/frankenstein.txt"
    arguments = sys.argv
    arguments.pop(0)
    if not (arguments):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    while(arguments):
        book_to_sort = arguments.pop(0)
        contents = (get_book_text(book_to_sort))
        counter = get_num_words(contents)
        #print (f'{counter} words found in the document')
        letters = char_counts(contents)
        results = sort_chars(letters)
        #print(results)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_to_sort}...")
        print("----------- Word Count ----------")
        print(f"Found {counter} total words")
        print("--------- Character Count -------")
        #print(type(results))
        while (results):
            #print(results.pop(0))
            item=results.pop(0)
            if item["char"].isalpha():
                print (f"{item["char"]}:", item["num"])
        print("============= END ===============")
    return

main()
#print(sys.argv)
#print(type(sys.argv))
#print(len(sys.argv))
