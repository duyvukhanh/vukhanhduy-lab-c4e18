from random import *
from eval import calc
def generate_quiz():
    x = randint(1,10)
    y = randint(1,10)
    op = choice(["+","-","*","/"])
    errors = [-1,0,1]
    er = choice(errors)
    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y 
    elif op == "/":
        result = x / y
    display_result = result + er
    # Hint: Return [x, y, op, result]
    return [x, y, op, display_result]

def check_answer(x, y, op, display_result, user_choice):
    result = calc(x, y, op)
    if user_choice:
        if result == display_result:
            return True
        else:
            return False
    elif not user_choice:
        if result != display_result:
            return True
        else:
            return False