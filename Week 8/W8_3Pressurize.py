"""This program will calculate the difference of the pressure"""
def calculate(air_in, air_out):
    """This program will calculate is the pressure is good or not"""
    pressure = ((air_in - air_out) / air_in)
    return pressure

def caller():
    """This program will calculate is the pressure is good or not"""
    difference = calculate(float(input()), float(input())) * 100
    if difference > 30:
        print("Underpressure", end=" ")
    elif difference < -30:
        print("Overpressure", end=" ")
    else:
        print("Safe", end=" ")
    print("%.4f" %(abs(difference)) + "%")

caller()
