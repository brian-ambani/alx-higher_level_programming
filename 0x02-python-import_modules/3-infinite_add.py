#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    for value in range(len(sys.argv) - 1):
            add +=int(sys.argv[value + 1])

    print("{}".format(add))
