#!/usr/bin/python3
for al in range(97, 123):
    if al == 113 or al == 101:
        continue
    else:
        print("{:c}".format(al), end='')
