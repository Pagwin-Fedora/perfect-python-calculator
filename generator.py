print("print('what operator do you want to do?');\nops=['+','-','x','/']\noperator=None\nwhile not operator in ops:\n\toperator = input('+ - x /\\t')\nx=-1\nwhile not 0<=x<=199:\n\tx=int(input('what\\'s the first num you want to input?(0-200)'))\ny=-1\nwhile not 0<=y<=199:\n\ty=int(input('what\\'s the second num you want to input?(0-200)'))")
for o in ["+","-","x","/"]:
    print("if operator == '"+o+"':")
    for i in range(200):
        for n in range(200):
            s = """
    if x == {0} and y == {1}:
        print('{0}{3}{1}={2}')
        """
            if o == "/" and n == 0:
                continue
            s = s.format(i,n,eval("i{0}n".format(o.replace("x","*"))),o)
            print(s)
