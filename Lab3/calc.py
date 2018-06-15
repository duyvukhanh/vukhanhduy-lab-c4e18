x = int(input("x = "))
op = input("Operation(+,-,*,/):")
y = int(input("y = "))


print("* "*10)
result = 0

if op == ("+"):
    result = x + y
elif op == ("-"):
    result = x - y
elif op == ("*"):
    result = x * y
elif op == ("/"):
    result = x / y


print("{0} {1} {2} = {3}".format(x, op, y, result))
