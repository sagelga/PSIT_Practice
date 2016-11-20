"""this is a docstring"""
def training():
    """this is a docstring"""
    new = []
    for _ in range(int(input())):
        new.append(int(input()))
    for _ in range(len(new)):
        for i in range(0, len(new)-1):
            if new[i] > new[i+1]:
                new[i], new[i+1] = new[i+1], new[i]
    for i in new:
        print(i)
training()
