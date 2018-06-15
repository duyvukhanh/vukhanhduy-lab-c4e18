from random import *
import eval
x = choice(range(1,10))
y = choice(range(1,10))
ops = ["+","-","*","/"]
error = [-1,0,1]
op = choice(ops)

result = eval.calc(x,y,op)

er = choice(error)
screen_result = result + er
 
print("{0} {1} {2} = {3}".format(x,op,y,screen_result))
ans = input("Y/N? :").upper()
if (er == 0 and ans == "Y") or (er !=0 and ans =="N"):
    print("Yay")
elif (er == 0 and ans == "N") or (er !=0 and ans =="Y"):
    print("You Are Wrong")

