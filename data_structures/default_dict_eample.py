from collections import defaultdict


def letter_frequency(sentence):
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies


if __name__ == '__main__':
    sentence = "i am fed up with myself"
    frequency_counter = letter_frequency(sentence)
    print(frequency_counter)