"""This program will convert m/s into different unit of speed"""
def converter():
    """This should work"""
    speed = float(input())
    print("%.4f" %(speed * 3.2808) + " foot per second.")
    print("%.4f" %(speed * 2.2369) + " miles per hour.")
    print("%.4f" %(speed * 3.6000) + " kilometer per hour.")
converter()
