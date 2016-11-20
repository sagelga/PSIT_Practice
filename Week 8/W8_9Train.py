"""This is a DOCSTRING"""
def seperate(name):
    """This is a DOCSTRING"""
    column = ''
    row = ''
    for i in name:
        if i.isalpha():
            column += i
        else:
            row += i
    differs = 0
    column = column[::-1]
    for i in range(len(column)):
        differs += (ord(column[i]) - 64) * (26**i)
    return(differs, row)

def main():
    """This is a DOCSTRING"""
    column_a, row_a = seperate(input())
    column_b, row_b = seperate(input())
    print(abs(int(column_a)-int(column_b)) + abs(int(row_a)-int(row_b)))

main()
