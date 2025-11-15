def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def sort_on(items):
    return items["num"]

def word_count(filepath):
    count = 0
    with open(filepath) as f:
        file_contents = f.read()
        words = file_contents.split()
        count = len(words)
    return count

def char_count(filepath):
    chars = {}
    with open(filepath) as f:
        file_contents = f.read()
        for char in file_contents:
            lower_char = char.lower()
            if lower_char not in chars:
                chars[lower_char] = 1
            else:
                chars[lower_char] += 1 
    return chars

def sorted_list(dictionary):
    List = []
    minidict = {}
    for item in dictionary:
        minidict = {"char":item,"num":dictionary[item]}
        List.append(minidict)
    List.sort(reverse=True, key=sort_on)

    return List

