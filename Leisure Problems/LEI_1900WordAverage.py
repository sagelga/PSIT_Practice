"""enter code here"""
def runner():
    """enter code here"""
    text = input()
    text = text.split(" ")
    text_count, total = 0, 0
    for i in text:
        trigger = False
        for j in i:
            if j.isalpha():
                total += 1
                trigger = True
        if trigger:
            text_count += 1
    if total == 0 or text_count == 0:
        print("0.00")
    else:
        print("%.2f" %(total / text_count))
runner()
