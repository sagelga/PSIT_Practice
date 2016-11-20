"""histogram"""
from string import ascii_letters as letters
def histogram(text):
    """find most used letter"""
    data = dict()
    for i in text:
        if i in letters:
            if i in data:
                data[i] += 1
            else:
                data[i] = 1
    for i in range(max(data.values()), 0, -1):
        print('%03d' % i, end=' ')
        for letter in letters:
            if letter in data:
                if data[letter] >= i:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
        print()
    print('    ', end='')
    for i in letters:
        if i in data:
            print(i, end=' ')
histogram(input())
