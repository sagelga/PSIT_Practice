"""Not finish"""
def gas():
    """THis is a docstring"""
    distance, cap = int(input()), int(input())
    miles, prev_number, count = 0, 0, 0
    for _ in range(int(input())):
        number = int(input())
        if number != distance:
            if number >= cap + miles:
                count += 1
                if number == cap + miles:
                    miles = number
                else:
                    miles = prev_number
            else:
                prev_number = number
    print(count)
gas()
