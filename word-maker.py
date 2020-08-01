from itertools import combinations, permutations
import os.path
from argparse import ArgumentParser


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("the file %s does not exist." % arg)
    else:
        return open(arg, 'r')   # return an open file handle


parser = ArgumentParser(description='Wordlist manupluation tools')
parser.add_argument('-i', '--infile', dest='input_file', required=True,
                    help='input text file', metavar="FILE",
                    type=lambda x: is_valid_file(parser, x))
parser.add_argument('-o', '--outfile', dest='output_file', required=False,
                    help='output text file', metavar="FILE",
                    type=lambda x: is_valid_file(parser, x))
args = parser.parse_args()


def read_word_list(file_object):
    # Returns one list of words
    f = list(file_object)
    return [line.rstrip('\n') for line in f]


# def combine_list(word_list):
#     # returns a list of words consisting of
#     #  the combination of all items in a list.
#     forward = list(combinations(word_list, 2))
#     reverse = list()
#     for element in forward:
#         reverse.append([element[1], element[0]])
#     return forward + reverse


def permute_words(word_list):
    # returns a list of words consisting of
    #  the permutations of all items in a list.
    print("word list")
    print(word_list)
    return list(permutations(word_list, 2))


def permute_word_lists(list_of_word_lists):
    # returns a list of each two-word combination, including variants
    # of each word.
    # Each word's variants are not combined.
    for word in list_of_word_lists:
        print(word)


# def list_doubles_to_list(doubles_list):
#     combined_list = list()
#     for x in doubles_list:
#         if len(x) > 1:
#             combined_list.append(x[0]+x[1])
#             combined_list.append(x[1]+x[0])
#     return combined_list


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


def process_words(word_list):
    words = list()
    for word in word_list:
        words.append(run_sequential_uppercase(word, 12))
    return words


# permute_word_lists([['hello'], ['Hello'], ['goodbye'], ['Goodbye']])
# print(process_words(read_word_list(args.input_file)))
print(args.input_file)
# print(permute_words(read_word_list(args.input_file)))

# processed_words_list = process_words(read_word_list(args.input_file))
# print(processed_words_list)
# print(args.output_file)
