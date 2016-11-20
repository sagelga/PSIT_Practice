"""this is a string"""
def grading():
    """this is a string"""
    score_range = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+']
    num = int(input()) - 65
    for i in range(len(score_range)):
        num -= 5
        if num < 0:
            return score_range[i]
    return "A"
print(grading())
