#!/usr/bin/env python

import os
import sys
import multiprocessing


if __name__ == '__main__':
    count = multiprocessing.cpu_count()
    if sys.argv[1:]:
        if sys.argv[1] == '--help':
            print "usage: %s [number-of-parallel-processes]" % sys.argv[0]
            sys.exit(1)
        else:
            count = int(sys.argv[1])

    print "Pool size:", count
    commands = [s.strip() for s in sys.stdin.readlines()]
    print multiprocessing.Pool(count).map(os.system, commands)
