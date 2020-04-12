import sys
def div(a, b):
    return int(a) / int(b)

try:
    print(div(sys.argv[1], sys.argv[2]))
except ValueError as e:
    print('Arguments are not all numbers')
except ZeroDivisionError as e:
    print("You can't divide by zero")
