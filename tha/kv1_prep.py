from pprint import pprint
import os

sents = [
    '0 ÷ 8 3 6 + 4 x 9 = - 7 2 5 1',
    '7 8 x + 3 1 ÷ 5 - 2 6 0 9 = 4',
    '1 - 3 6 2 8 = 0 5 9 + ÷ 7 4 x',
    '7 3 + 4 8 0 = 5 ÷ 9 1 - 6 2 x',
    '÷ 2 0 x 3 = 8 7 1 + 5 6 4 9 -',
    '2 6 4 x - ÷ 1 8 9 3 0 + 7 5 =',
    '÷ 0 3 = 6 8 1 7 9 - + x 4 5 2',
    '9 1 + 6 5 4 2 3 8 x = 0 - ÷ 7',
    '5 1 0 + - 7 4 9 = 6 8 x 3 2 ÷',
    '9 + 6 - ÷ 4 0 3 5 7 1 8 x = 2',
    'x 2 3 4 8 9 ÷ + 1 - 6 7 = 5 0',
    '÷ 0 x 6 = 8 5 7 9 4 - + 2 1 3',
    '+ 0 6 ÷ 1 = 8 2 4 - 9 3 7 5 x',
    '4 + 6 9 7 x 0 8 = 5 1 - ÷ 2 3',
    '- 7 8 x 2 9 0 1 4 ÷ 3 5 6 = +',
    '3 4 ÷ 9 8 1 5 - 2 0 7 6 x = +',
    '5 x 7 1 = 0 - + 2 9 6 4 3 8 ÷',
    '÷ 0 + 2 5 6 9 = - 7 x 4 3 1 8',
    '7 ÷ 5 + 2 8 = 9 3 0 4 1 x 6 -',
    '÷ 5 4 = 9 0 x 2 3 1 - 7 + 6 8'
    ]

dict = {}

teljari = 0
for i in sents:
    teljari += 1
    i = 'kk2_' + i.replace(' ', '_') + '.wav'
    i = {str(teljari) + '.wav' : i}
    dict.update(i)


dir = os.path.join(os.getcwd(), 'wavs')
for filename in os.listdir(dir):
    src = os.path.join(dir, filename)
    dst = os.path.join(dir, dict[filename])
    for k,v in dict.items():
        if filename == k:
            os.rename(src, dst)
