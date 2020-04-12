#! /usr/bin/env python

x = int(input("enter a value: "))
if x < 0:
    x = 0
    print('negative changed to %s' % (x))
elif x == 0:
    print('zero')
elif x == 1:
    print('one')
else:
    print('other value provided %s' % (x))
