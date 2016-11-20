"""This program will calculate the payments, goal achievements and stats."""
def seveneleven():
    """This thing will match the price with original sales. Sucess goals will be 2x the profit"""
    worker_name = input()
    rice_sold = int(input())
    sand_sold = int(input())
    sala_sold = int(input())
    water_sold = int(input())
    snack_sold = int(input())
    rice_prc = 30
    sand_prc = 25
    sala_prc = 20
    water_prc = 15
    snack_prc = 10
    message = ""
    if rice_sold >= 25:
        message = message + "R "
        rice_prc *= 2
    if sand_sold >= 40:
        message = message + "S "
        sand_prc *= 2
    if sala_sold >= 70:
        message = message + "P "
        sala_prc *= 2
    if water_sold >= 100:
        message = message + "W "
        water_prc *= 2
    if snack_sold >= 250:
        message = message + "K"
        snack_prc *= 2
    pay = (rice_sold * rice_prc) + (sand_sold * sand_prc) + (sala_prc * sala_sold)
    pay = pay + (water_prc * water_sold) + (snack_prc * snack_sold)
    print("Employee :", worker_name)
    print("Payday :", pay, "Baht.")
    print("Archivement :", message)
    print("You did great!,", worker_name + ".")
seveneleven()
