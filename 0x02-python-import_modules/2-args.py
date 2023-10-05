if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if ((n) == 0):
        print("{} arguments".format(0))
    elif (n) == 1:
        print("{} argument".format(1))
        for i in range(1, n):
            if i <= n:
                print("{} : {}".format(i, sys.argv[i]))
    else:
        print("{} arguments".format(len(sys.argv) - 1))
        for i in range(0, n):
            if i <= n:
                print("{} : {}".format(i+1, sys.argv[i+1]))
