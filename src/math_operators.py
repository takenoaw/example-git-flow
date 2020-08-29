def add(num1, num2):
    return num1+num2


def mult(num1, num2):
    return num1*num2


def sub(num1, num2):
    return num1-num2


def div(num1, num2):
    try:
        result = num1/m
    except:
        result = "Math error"
    return result


def abs(num):
    result = num
    if num < 0:
        result = num * -1
    return result
