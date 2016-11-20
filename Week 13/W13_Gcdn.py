"""This is a string"""
def gcd():
    """This is a string"""
    total = int(input())
    listing, total_list = [], []
    for _ in range(total):
        listing.append(int(input()))
    for i in range(2, max(listing)+1):
        counter = 0
        for j in range(len(listing)):
            if listing[j] % i == 0:
                counter += 1
            if counter == total:
                total_list.append(i)
    print(total_list[-1])
gcd()