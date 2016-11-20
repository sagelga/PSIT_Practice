"""This program will run wheaver the input is in range of 0-120 and change back to grades"""
def grading():
    """It is doing some nested if-else relationship,
    to find the real grades that have been calculated."""
    raw_grade = int(input())
    if raw_grade >= 80 and raw_grade <= 100:
        grade = 4
    else:
        if raw_grade >= 75 and raw_grade <= 79:
            grade = 3.5
        else:
            if raw_grade >= 70 and raw_grade <= 74:
                grade = 3
            else:
                if raw_grade >= 65 and raw_grade <= 69:
                    grade = 2.5
                else:
                    if raw_grade >= 60 and raw_grade <= 64:
                        grade = 2
                    else:
                        if raw_grade >= 55 and raw_grade <= 59:
                            grade = 1.5
                        else:
                            if raw_grade >= 50 and raw_grade <= 54:
                                grade = 1
                            else:
                                grade = 0

    print("%.1f" %grade)
grading()
