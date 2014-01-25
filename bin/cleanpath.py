#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    paths = os.getenv('PATH').split(os.pathsep)
    cleaned_paths = []
    for path in paths:
        if path in cleaned_paths:
            sys.stderr.write('Duplicated: %s\n' % path)
            continue
        if not os.path.exists(path):
            sys.stderr.write('Doesn\'t exist: %s\n' % path)
            continue
        cleaned_paths.append(path)
    sys.stdout.write(os.pathsep.join(cleaned_paths))
