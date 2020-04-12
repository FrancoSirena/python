""" w for overwriting it and a for appending to it """
f = open('some_w.txt', 'w')

mlist = ['a', 'b', 'c']
for m in mlist:
    f.write(m + '\n')
f.close()

with open('some_w.json', 'w') as j:
    import json
    dum = {'a': 'foo', 'b': 'bar'}
    json.dump(dum, j)
