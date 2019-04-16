import random
import os

'''
Hinrik Hafsteinsson - Spring 2019

Randomization script used for generating number strings for training/testing material.
Outputs a directory with 8 .txt files each with 20 lines of 10 randomized digits
and mathemiatics symbols.
'''

directions = ['upp', 'niður', 'hægri', 'vinstri']
numbers = [str(v) for v in random.sample(range(0, 10), 10)]
functions = ['plús', 'mínus', 'deilt með', 'sinnum']
func_signs = ['+', '-', 'x', '÷', '=']

participants = ['kk1', 'kk2', 'kk3', 'kk4', 'kv1', 'kv2', 'kv3', 'kv4']

cwd = os.getcwd()
target_dir = os.path.join(cwd, 'num_utterance_lists')

def make_dir(target):
    if os.path.isdir(target):
        pass
    else:
        os.mkdir(target)

def random_list(lst):
    randomized = random.sample(lst, len(lst))
    return randomized

def write_files(participant):
    runner = 1
    list_to_randomize = numbers + func_signs
    filename = os.path.join(target_dir, participant) + '.txt'
    with open(filename, 'w') as file:
        while runner != 21:
            file.write(' '.join(random_list(list_to_randomize)))
            file.write('\n')
            runner += 1

make_dir(target_dir)
for participant in participants:
    write_files(participant)
