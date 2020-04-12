def say(name):
    """
    Returns name passed as param
    """
    return name

foo = say('Some')
print(foo)

def add(n1=1, n2=2):
    return n1+n2

print(add())

def madlibs(name, noun="shoes", adjective="red"):
    return "{0} has {1} {2}".format(name, adjective, noun)

madlib = madlibs(name="Will", adjective="blue")
print(madlib)
