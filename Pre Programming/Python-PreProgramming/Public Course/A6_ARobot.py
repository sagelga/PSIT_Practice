"""This program will run wheaver the input is in range of 0-120 and change back to grades"""
def grade():
    """It is doing some nested if-else relationship,
    to find the real grades that have been calculated."""
    raw_grade = int(input())
    if raw_grade >= 100 and raw_grade <= 120:
        print("A")
    else:
        if raw_grade >= 95 and raw_grade <= 99:
            print("B+")
        else:
            if raw_grade >= 90 and raw_grade <= 94:
                print("B")
            else:
                if raw_grade >= 85 and raw_grade <= 89:
                    print("C+")
                else:
                    if raw_grade >= 80 and raw_grade <= 84:
                        print("C")
                    else:
                        if raw_grade >= 75 and raw_grade <= 79:
                            print("D+")
                        else:
                            if raw_grade >= 70 and raw_grade <= 74:
                                print("D")
                            else:
                                print("F")
grade()
