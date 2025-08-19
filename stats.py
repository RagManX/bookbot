def get_num_words(text_to_split):
    split_text = text_to_split.split()
    size = len(split_text)
    return size

def char_counts(full_text):
    text = full_text.lower()
    chars = {}
    for letter in text:
        if letter in chars:
            chars[letter] += 1
        else:
            chars[letter] = 1
    return chars

def sort_on(items):
    return items["num"]

def sort_chars(input_dict):
    sorter = []
    for letter in input_dict:
        sorter.append({"char": letter, "num": input_dict[letter]})
    sorter.sort(reverse=True, key=sort_on)
    return sorter
