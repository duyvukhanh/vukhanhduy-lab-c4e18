from random import *
def calc(x,y,op):
    res = 0

    if op == "+":
        res = x + y
    elif op == "-":
        res = x - y
    elif op == "*":
        res = x * y 
    elif op == "/":
        res = x / y
    return res
    
# print("Hello World")
# result = calc(1,2,"+")

# print(result)