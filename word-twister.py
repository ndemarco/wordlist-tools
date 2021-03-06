# Manipulate a list of words
from datetime import datetime
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
parser.add_argument('-o', '--outfile', dest='output_file', required=False,
                    help='output file', metavar="FILE")
command_args = parser.parse_args()


def read_word_list(file_object):
    # returns one list of words
    f = list(file_object)
    return [line.rstrip('\n') for line in f]


def permute_words(word_list):
    phrase_list = list(permutations(word_list, 2))
    return list(map(list, phrase_list))


'''
def make_number_list(digits, pad_with_zeros):
    # inserts set of sequential integers of length 'digits'
    number_list = []
    # for x in range(10**digits):
    #     number_list.append(str(x))
    #     for y in range(digits - len(str(x))):
    #         number_list.append(('z' * y) + str(x))
    for x in range(digits):
        for y in range(10):
            number_list.append(str(y))
    return number_list



Makes number lists.
for one digit: create set of natural numbers, including zero: list(range(10)).
For two digits: loop through 0-9, adding the range(10) to each digit looped.
'''


def make_number_list(digits):
    number_list = []
    if digits > 0:
        zero_to_nine = [str(i) for i in range(3)]
        number_list += zero_to_nine
        for z in range(1, digits):
            temp_numbers = []
            for y in number_list:
                temp_numbers += [y + s for s in zero_to_nine]
            number_list += temp_numbers
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
        result.append([run_sequential_uppercase(word_pair[0], 2),
                       run_sequential_uppercase(word_pair[1], 2)])
    return result

def write_file(output_file, final_list):
    f = open(output_file, "w")
    for word in final_list:
        f.write("%s\n" % word)

def combine_words_with_number(numberless_list, numbers):
    final_list = list()
    for word_pair in numberless_list:
        for first_word in word_pair[0]:
            for last_word in word_pair[1]:
                for number in numbers:
                    final_list.append(first_word+number+last_word)
                    # print(first_word+number+last_word)
    return final_list        

numbers = make_number_list(1)
numberless_list = (twist_word_list(permute_words(read_word_list(command_args.input_file))))

combined_list = combine_words_with_number(numberless_list, numbers)
write_file(command_args.output_file, combined_list)