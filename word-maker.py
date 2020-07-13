from itertools import combinations
import os.path
from argparse import ArgumentParser


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("the file %s does not exist." % arg)
    else:
        return open(arg, 'r')   # return an open file handle


parser = ArgumentParser(description='FileCombiner description')
parser.add_argument('-i', '--infile', dest='filename', required=True,
                    help='input text file', metavar="FILE",
                    type=lambda x: is_valid_file(parser, x))
args = parser.parse_args()


def get_word_list(file_object):
    f = list(file_object)
    return [line.rstrip('\n') for line in f]


def combine_list(word_list):
    # returns the combination of all items in a list.
    forward = list(combinations(word_list, 2))
    reverse = list()
    for element in forward:
        reverse.append([element[1], element[0]])
    return forward + reverse


def list_doubles_to_list(doubles_list):
    combined_list = list()
    for x in doubles_list:
        if len(x) > 1:
            combined_list.append(x[0]+x[1])
            combined_list.append(x[1]+x[0])
    return combined_list


def add_sequential_capitals(word, max_num_of_capitals):
    words = list()
    for x in range(max_num_of_capitals):
        for letter in range(len(word)):
            if len(word) - x - letter > 0:
                words.append(word[:letter] +
                             word[letter:letter + x + 1:].upper() +
                             word[letter + 1 + x:])
    return words
    # + word[letter:letter + x].upper()  \


def process_words(word_list):
    print("process_words\n", word_list)
    words = list()
    for word in word_list:
        print(word)
        words.append(add_sequential_capitals(word, 12))
    return words


processed_words_list = process_words(get_word_list(args.filename))
print(processed_words_list)
