from collections import Counter


def letter_frequency(_iterable):
    return Counter(_iterable)

if __name__ == '__main__':
    sentence = "i am fed up with myself"
    frequency_counter = letter_frequency(sentence)
    most_common = frequency_counter.most_common(2)
    print(most_common)
    responses = [
        "vanilla",
        "chocolate",
        "vanilla",
        "vanilla",
        "caramel",
        "strawberry",
        "vanilla"
    ]
    most_common = letter_frequency(responses).most_common(1)
    print(most_common)