"""Print Output"""
def out():
    """print string output"""
    milisecs = 492137954293754252786
    seconds = milisecs // 1000
    milisecs = milisecs % 1000
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    minutes = minutes % 60
    days = hours // 24
    hours = hours % 24
    print(days, hours, minutes, seconds, milisecs)
out()
