def whoami():
    def mprint(msg):
        print('method {0}'.format(msg))
    i = 'I am groot'
    def local_groot():
        i = 'I am local groot'
        print('local {0}'.format(i))
    def nonlocal_groot():
        nonlocal i
        i = 'I am nonlocal groot'
    def global_groot():
        global i
        i = 'I am global groot'
    mprint(i)
    local_groot()
    mprint(i)
    nonlocal_groot()
    mprint(i)
    global_groot()
    mprint(i)

whoami()
print('global {0}'.format(i))
