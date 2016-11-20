"""Using different functions to make the thing work"""
def recalling():
    """Announcing the output number to the functions_a"""
    output = "1"
    functions_a(output)
    output = "2"
    functions_a(output)
    output = "3"
    functions_a(output)
    output = "4"
    functions_a(output)
def functions_a(parameter):
    """Printing out the output, given by recalling"""
    print("Output" + parameter)
    print("Output" + parameter)
    print("Output" + parameter)
recalling()
