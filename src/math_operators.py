def add(num1,num2):
    return num1+num2
def mult(num1,num2):
    return num1*num2
def sub(num1,num2):
    return num1-num2
def div(num1,num2):
    try:
        resul = num1/m
    except:
        resul = "Math error"
    return resul
def abs(num):
    result = num
    if num<0:
        result = num * -1
    return result