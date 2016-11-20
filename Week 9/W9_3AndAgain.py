"""This do something"""
import json
def caller():
    """This will do another thing"""
    line_a, line_b, trigger, text = json.loads(input()), json.loads(input()), True, []
    for i in range(max(len(line_a), len(line_b))):
        if (line_a[i] % 2 == 1) and (line_b[i] % 2 == 0):
            text.append(line_a[i] + line_b[i])
            trigger = False
    if trigger:
        print("Nope")
    else:
        print(text)

caller()
