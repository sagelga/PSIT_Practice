"""Program To Calculate And Answer Functions"""
def cal():
    """Calculate and answer functions"""
    va_a = float(input())
    va_b = float(input())
    va_c = float(input())
    va_d = float(input())
    print(4*va_a)
    print(3*(((2*va_a)-(2*va_b))**4)-(((2*va_a)-(2*va_b))**3)+(2*(((2*va_a)-(2*va_b))**2)+10))
    var_x = (2*(va_a+va_b))
    var_y = (2*(va_a+va_c))
    var_z = ((3*((2*(va_d**2))**4))-((2*(va_d**2))**3)+(2*((2*(va_d**2))**2))+10)
    print(((var_z+var_x)**2)-(var_x*var_y)+(var_y**2))
    variabletx = 2*(va_a+va_b)
    variablety = 2*(va_a-va_c)
    variabletz = 3*((2*(va_d**2))**4)-((2*(va_d**2))**3)+(2*((2*(va_d**2))**2))+10
    var_t = ((variabletz+variabletx)**2)-(variabletx*variablety)+(variablety**2)
    iam = 2*(va_a-va_b)
    var_i = 3*((iam)**4)-(iam**3)+(2*((iam)**2))+10
    var_g = 32*va_c
    var_e = va_d**8
    print(((var_t**2)+(var_i**2)-(var_g**2))/((var_e**2)-(2*(var_t*var_e))+2*(var_t)))
cal()
