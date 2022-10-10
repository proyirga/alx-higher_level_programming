#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for elm in range(x):
        try:
            print(f"{my_list[elm]}", end = "")
            i += 1
        except IndexError:
            break
    print()
    return (i)
