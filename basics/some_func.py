def total(n):
    return n * .07 + n

def tax_amount(n):
    return n * .07

""" __name__ resolves  to the name of the scope, __main__ is the shell command and import NAME will resolve to NAME"""

if __name__ == '__main__':
    import sys
    print(total(int(sys.argv[1])))
