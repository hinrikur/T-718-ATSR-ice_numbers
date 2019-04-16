from pprint import pprint
import os

sents = [
    '+ 6 2 x = - 3 9 7 ÷ 4 1 8 0 5',
    '7 + 9 5 0 2 6 3 ÷ = - 4 8 x 1',
    '9 2 6 ÷ x 7 8 5 0 = 4 - + 3 1',
    '÷ + 7 2 0 9 5 x 3 6 4 1 - 8 =',
    '0 = 4 8 7 5 2 6 + 9 x 3 - 1 ÷',
    '= 3 7 ÷ 2 1 5 8 - x + 6 4 9 0',
    '÷ 3 8 9 7 2 5 - + x = 1 0 6 4',
    '3 + - 1 4 ÷ x 6 5 7 = 0 8 9 2',
    'x 2 1 9 ÷ 7 8 6 3 - = + 4 5 0',
    '3 = ÷ 4 + 1 0 7 2 9 8 6 5 - x',
    '÷ 4 2 x 0 6 5 = 3 + 9 8 - 1 7',
    '2 7 3 x 0 1 5 + 8 ÷ = 9 - 6 4',
    '+ ÷ = 5 2 0 6 x - 9 1 3 4 7 8',
    '1 0 4 7 2 6 - 5 9 = + ÷ 8 3 x',
    '7 = + 9 ÷ 6 - 2 5 3 4 0 1 x 8',
    '9 4 x 7 0 1 + 2 6 8 3 ÷ = - 5',
    '1 - 5 x 8 3 0 4 ÷ 9 6 = 2 7 +',
    '- + x 0 8 4 6 1 = 3 2 5 ÷ 9 7',
    '5 7 + 8 x 3 - 9 4 1 6 ÷ = 2 0',
    '9 1 0 = 6 - ÷ 5 + 8 3 7 2 4 x'
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
