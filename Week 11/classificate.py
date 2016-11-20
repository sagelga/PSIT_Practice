"""This is docstring yo!"""
def classify():
    """It's a something"""
    year = []
    student = []
    text = input()
    while text != "END":
        if text[0:4] not in year:
            year.append(text[0:4])
        student.append(text)
        text = input()

    year = [int(i) for i in year]
    year = sorted(year)
    for i in student:
        print(student.count(str(i)))

classify()