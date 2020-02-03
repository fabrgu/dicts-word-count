# put your code here.
def count_words(file_name):
    file = open(file_name)
    word_dict = {}
    for line in file:
        line = line.strip()
        words = line.split(" ")
        for word in words:
            word_dict[word] = word_dict.get(word, 0) + 1

    file.close()
    for word in word_dict:
        print(f"{word} {word_dict[word]}")


count_words("twain.txt")
