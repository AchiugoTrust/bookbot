def txt_count(content):
    word_count = content.split()
    return len(word_count)

def char_count(words):
    char_dict = {}

    for word in words:
        for char in word.lower():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

    return char_dict

def sort_on(char_dict):
    return char_dict[1]