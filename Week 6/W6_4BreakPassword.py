"""This program will brute-force the hashing data"""
import hashlib
def bruteforce():
    """This function will encode the password"""
    text = input()
    for i in range(100000):
        password = "%05d" %i
        password = password.encode('utf8')
        password = (hashlib.sha512(password).hexdigest()).upper()
        if text == password:
            print("%05d" %i)

bruteforce()
