def get_num_words(text):
    return len(text.split())

def get_characters_with_count(text):
    chars = {}
    for char in text:
        c = char.lower()
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def get_sorted_characters(characters):
    chars_list = []
    for char ,count in characters.items():
        chars_list.append({"char": char, "num": count})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list


def sort_on(items):
    return items["num"] 