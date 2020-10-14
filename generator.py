import itertools

MAX = 200

single = """
if x == {0} and y == {1} and operator == '{2}':
    print("{0}{2}{1} = {3}")
"""

combs = itertools.product(range(MAX), range(MAX), "+-x/")


def handler(tup):
    first, second, operator = tup
    if operator == "/" and second == 0:
        print(
            """
if x == {0} and y == {1} and operator == '{2}':
    print("{0}{2}{1} = undefined")""".format(
                first, second, operator.replace("x", "*")
            )
        )
    else:
        print(
            single.format(
                first,
                second,
                operator,
                eval(f"{first}{operator.replace('x','*')}{second}"),
            )
        )


print(
    "print('what operator do you want to do?');\nops=['+','-','x','/']\noperator=None\nwhile not operator in ops:\n\toperator = input('+ - x /\\t')\nx=-1\nwhile not 0<=x<=199:\n\tx=int(input('what\\'s the first num you want to input?(0-200)'))\ny=-1\nwhile not 0<=y<=199:\n\ty=int(input('what\\'s the second num you want to input?(0-200)'))"
)
[*map(handler, combs)]
