"""This program will check the raw grade and convert to another grade type"""
def grade_converter():
    """This function will suit the corresponding grade"""
    raw_score = float(input())
    if 0 <= raw_score <= 100:
        if 95 <= raw_score <= 100:
            print("A")
        if 90 <= raw_score < 95:
            print("B+")
        if 85 <= raw_score < 90:
            print("B")
        if 80 <= raw_score < 85:
            print("C+")
        if 75 <= raw_score < 80:
            print("C")
        if 70 <= raw_score < 75:
            print("D+")
        if 65 <= raw_score < 70:
            print("D")
        if 60 <= raw_score < 65:
            print("F+")
        if raw_score < 60:
            print("F")
    else:
        print("ERR")
grade_converter()
