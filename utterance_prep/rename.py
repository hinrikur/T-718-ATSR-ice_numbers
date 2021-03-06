import sys
import os

'''
Hinrik Hafsteinsson - Spring 2019

Script for renaming .wav files.
Input: Participant ID (e.g. kk1)

Looks for a directory of .wav files with filenames of integers from 1-20
(the default naming format for each participant). Then loads number strings
from participant's text file and renames each file with corresponding string.
'''

wd = os.getcwd()

participant = sys.argv[1]
name_file = os.path.join(wd, 'num_utterance_lists/' + participant + '.txt')
wav_dir = os.path.join(os.path.dirname(wd), 'waves/' + participant)
# participant = wav_dir[-3:]

def name_dict(name_list):
    runner = 1
    name_dict = {}
    for name in name_list:
        name_dict[str(runner)] = name
        runner += 1
    return name_dict

def name_list(filename):
    name_list = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            line = line.strip().replace(' ', '_')
            name_list.append(line)
    return name_list

def rename_files_fromdict(dir, dict):
    for file in os.listdir(dir):
        for k,v in dict.items():
            if file == k + '.wav':
                oldname = os.path.join(wav_dir, file)
                newname = os.path.join(wav_dir, participant + '_' + v + '.wav')
                os.rename(oldname, newname)

name_dict = name_dict(name_list(name_file))

rename_files_fromdict(wav_dir, name_dict)

print('All done')
