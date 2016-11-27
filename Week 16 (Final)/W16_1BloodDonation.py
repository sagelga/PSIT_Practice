"""Blood Donation: PSIT 2016.Final Exam"""
def core():
    """
    Return True if registrant is passed conditions
    False otherwise
    """
    age = int(input())
    weight = int(input())
    ever_donate = int(input())
    if is_require_cert(age):
        cert = input()
    if is_age_pass(age):
        if is_require_cert(age):
            if age == 17 and is_cert_pass(cert) and is_weight_pass(weight)
