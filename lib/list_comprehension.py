#!/usr/bin/env python3

def return_evens(num_list):
    # filter out even numbers
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    #  add exclamation marks
    return [sentence + '!' for sentence in sentence_list]

# function tests
if __name__ == "__main__":
    print(return_evens([0, 1, 3, 5, 7, 8, 9]))
    print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))