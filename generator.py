import itertools

MAX = 200

single = """{0}{2}{1}"""

combs = itertools.product(range(MAX), range(MAX), list("+-*/")+["//"])


def handler(tup):
    first, second, operator = tup
    with open("question","a+") as question:
        with open("answer","a+") as answer:
            if (operator == "/" or operator == "//" ) and second == 0:
                print(single.format(first,second,operator),file=question)
                print("stop fudging with maths",file=answer)
            else:
                print(single.format(first,second,operator),file=question)
                print(eval(f"{first}{operator}{second}"),file=answer)


[*map(handler, combs)]
