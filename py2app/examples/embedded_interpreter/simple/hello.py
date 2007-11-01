import sys, os
import pprint
try:
    set
except NameError:
    from sets import Set as set

def print_sys():
    for arg in 'prefix', 'exec_prefix', 'executable':
        print '%s: %s' % (arg, getattr(sys, arg))

def host_main():
    print 'Hello from main executable (pid: %s)' % (os.getpid(),)
    print_sys()
    print ''
    os.spawnv(os.P_WAIT, sys.executable, [sys.executable, __file__, 'subinterpreter', repr(sys.path)])

def spawned_main():
    print 'Hello from spawned executable (pid: %s)' % (os.getpid(),)
    print_sys()
    print ''
    otherpaths = set(filter(os.path.exists, eval(sys.argv[2])))
    mypaths = set(filter(os.path.exists, sys.path))
    mine_not_other = list(mypaths - otherpaths)
    other_not_mine = list(otherpaths - mypaths)
    mine_not_other.sort()
    other_not_mine.sort()
    if mine_not_other or other_not_mine:
        print 'Path mismatch :('
        if mine_not_other:
            print 'sub-interpreter extras: ', mine_not_other
        if other_not_mine:
            print 'sub-interpreter missing: ', other_not_mine
    else:
        print 'Sub-interpreter launched ok!'

if __name__ == '__main__':
    if sys.argv[1:2] == ['subinterpreter']:
        spawned_main()
    else:
        host_main()
