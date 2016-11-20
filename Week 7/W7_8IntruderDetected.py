"""Pair Programming Week 7 by K. Srisuntiroj ID0022
The program will find the number inside many O's. Then sort and convert to binary number"""
def calculate(raw_line):
    """This thing is a docstring"""
    for _ in range(16):
        raw_line += input()
    for i in range(10):
        if raw_line.count(str(i)) > 0:
            line = (raw_line.find(str(i))) // 16
            column = (raw_line.find(str(i))) % 16
            print(binaryline[line * 5:(line * 5) + 4] + binaryline[column * 5:(column * 5) + 4])

binaryline = "0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111"
calculate("")
