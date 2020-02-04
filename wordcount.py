# put your code here.
import sys
from collections import Counter


def get_word_dict(file_name):
    file = open(file_name)
    word_dict = {}
    for line in file:
        line = line.strip()
        words = line.split(" ")
        for word in words:
            word_dict[word] = word_dict.get(word, 0) + 1

    file.close()

    return word_dict


def count_words(file_name):
    word_dict = get_word_dict(file_name)

    for word in word_dict:
        print(f"{word} {word_dict[word]}")


def count_words_counter(file_name):
    file = open(file_name)
    word_counter = Counter()
    for line in file:
        line = line.strip()
        words = line.split(" ")
        for word in words:
            word_counter[word] = word_counter[word] + 1

    file.close()
    for word in word_counter:
        print(f"{word} {word_counter[word]}")


def count_words_sorted(file_name):
    word_dict = get_word_dict(file_name)
    word_keys = list(word_dict.keys())
    word_keys.sort(key=str.lower)
    for word_key in word_keys:
        print(f"{word_key} {word_dict[word_key]}")

# def count_word_sorted_count(file_name):
#     word_dict = get_word_dict(file_name)

file_name = sys.argv[1]
count_words(file_name)
