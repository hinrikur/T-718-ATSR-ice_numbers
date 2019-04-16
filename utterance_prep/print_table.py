
'''
Hinrik Hafsteinsson - Spring 2019

Small script for printing items for a LaTeX table with number info.
'''

filepath = 'num_utterance_lists/all_nums.txt'

with open(filepath, 'r') as file:
    teljari = 0
    table_runner = 1
    for line in file.readlines():
        if teljari > 19:
            table_runner += 1
            teljari = 0
            print('New table: {0}'.format(table_runner))
        teljari += 1
        line = line.replace(' ', ' & ').strip('\n')
        line = line.replace('÷', '$\\div$')
        line = '{0}. & & '.format(teljari) + line + '\\\\'
        print(line)
