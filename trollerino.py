#!/usr/bin/env python3

import os
import shutil


def main():
    root = os.path.expanduser('~') + "/Desktop/"
    source = "Copy/"
    target = "Source/"

    while True:
        if len(seek(root + target)) == 0:
            print("THOU SHALL NOT PASS")
            refill(root, source, target)

def seek(path):
    files = os.listdir(path)
    return files

def refill(root, source, target):
    for x in range(len(seek("%s%s" % (root, source)))):
        shutil.copy("%s%s%s" % (root, source, seek("%s%s" % (root, source))[x]),
                    "%s%s%s" % (root, target, seek("%s%s" % (root, source))[x]))



# Runs the main, after establishing that this is not a library.
if __name__ == "__main__":
    main()
