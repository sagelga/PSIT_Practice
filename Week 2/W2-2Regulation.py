"""This program will print out various alignments by then given data."""
def sticking():
    """This funtion will receive numbers, and then print out by specs"""
    word_1 = int(input())
    word_2 = float(input())
    word_3 = str(input())
    print("%30d"%(word_1))
    print("%030d"%(word_1))
    print("%.2f"%(word_2))
    print("%.12f"%(word_2))
    print("%40s"%(word_3))
sticking()
