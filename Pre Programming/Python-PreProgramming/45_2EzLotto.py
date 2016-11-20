"""45_2EzLotto"""
import math
def codingin():
    """This thing will worked just fine"""
    var_a = int(input())
    var_b = int(input())
    var_c = int(input())
    var_d = int(input())
    var_e = int(input())
    average = max(var_a, var_b, var_c, var_d, var_e) + min(var_a, var_b, var_c, var_d, var_e)
    varp = average / 2
    varp += ("%2f" %average)
    print(math.floor(varp))

codingin()
