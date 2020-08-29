import math_operators as math

print('welcome')
print("first number")
num1=int(input())
print("second number")
num2= int(input())


print("result " +str(num1)+ " + " +str(num2)+ " =",math.add(num1,num2))
print("result " +str(num1)+ " - " +str(num2)+ " =",math.sub(num1,num2))
print("result " +str(num1)+ " * " +str(num2)+ " =",math.mult(num1,num2))
print("result " +str(num1)+ " / " +str(num2)+ " =",math.div(num1,num2))
print("done")