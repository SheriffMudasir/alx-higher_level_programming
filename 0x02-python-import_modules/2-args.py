#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if ((n) == 0):
        print("{} arguments".format(0))
    elif (n) == 1:
        print("{} argument".format(1))
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
    else:
        print("{} arguments".format(len(sys.argv) - 1))
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
