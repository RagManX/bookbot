from stats import get_num_words

def get_book_text(filename):
    with open(filename) as f:
        file_contents = f.read()
    return file_contents

def main():
    contents = (get_book_text("./books/frankenstein.txt"))
    counter = get_num_words(contents)
    print (f'{counter} words found in the document')
    return

main()
