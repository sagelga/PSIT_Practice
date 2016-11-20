"""ATM ERROR"""
def test(bank):
    """print atm"""
    bankpan = bank//1000
    modpan = bank%1000
    bank5roy = modpan//500
    mod5roy = modpan%500
    bankroy = mod5roy//100
    modroy = mod5roy%100
    bank20 = modroy//20
    print(bank20)
    print(bankroy)
    print(bank5roy)
    print(bankpan)
test(int(input()))