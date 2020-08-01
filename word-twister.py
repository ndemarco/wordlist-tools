# Manipulate a list of words

from itertools import permutations
import os.path
from argparse import ArgumentParser


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("the file %s does not exist." % arg)
    else:
        return open(arg, 'r')   # return an open file handle


parser = ArgumentParser(description="Wordlist manipulation tools")
parser.add_argument('-i', '--infile', dest='input_file', required=True,
                    help='input text file', metavar="FILE",
                    type=lambda x: is_valid_file(parser, x))
command_args = parser.parse_args()


def read_word_list(file_object):
    # returns one list of words
    f = list(file_object)
    return [line.rstrip('\n') for line in f]


def permute_words(word_list):
    phrase_list = list(permutations(word_list, 2))
    return list(map(list, phrase_list))


def make_number_list(digits):
    # inserts set of sequential integers of length 'digits'
    number_list = []
    for x in range(10):
        number_list.append('0' + str(x))
    for x in range(10**digits):
        number_list.append(int(x))
    return number_list


def run_sequential_uppercase(word, max_sequential_characters):
    # Creates a list of words where one or more sequential letters
    # is converted to uppercase, starting from the beginning of
    # the word.
    word_list = [word]
    for x in range(max_sequential_characters):
        for character in range(len(word)):
            if len(word) - x - character > 0:
                word_list.append(word[:character] +
                                 word[character:character + x + 1:].upper() +
                                 word[character + 1 + x:])
    return word_list


def twist_word_list(word_list):
    result = list()
    for word_pair in word_list:
        result.append(run_sequential_uppercase(word_pair[0], 2))
        result.append(run_sequential_uppercase(word_pair[1], 2))
    return result


print(twist_word_list(permute_words(read_word_list(command_args.input_file))))
# print(permute_words(read_word_list(args.input_file)))
# print(make_number_list("test", 2))
