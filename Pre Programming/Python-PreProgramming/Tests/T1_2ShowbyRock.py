"""This program will check either P' Nok will win the battle"""
def nok_pear():
    """This thing will check the variables. Comparing to each other"""
    var_a = input()
    var_b = input()
    if var_a == "Rock" and var_b == "Scissors":
        print("God of Banana")
        print("Rock!!!")
    if var_a == "Rock" and var_b == "Paper":
        print("Banabird")
        print("Rock!!!")
    if var_a == "Rock" and var_b == "Rock":
        print("Banabana")
        print("Rock!!!")
    if var_a == "Scissors" and var_b == "Paper":
        print("God of Banana")
    if var_a == "Scissors" and var_b == "Rock":
        print("Banabird")
    if var_a == "Scissors" and var_b == "Scissors":
        print("Banabana")
    if var_a == "Paper" and var_b == "Paper":
        print("Banabana")
    if var_a == "Paper" and var_b == "Rock":
        print("God of Banana")
    if var_a == "Paper" and var_b == "Scissors":
        print("Banabird")
nok_pear()
