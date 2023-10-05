#!/usr/bin/python
if __name__ == "__main__" :
    if  len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

        operators = {"+": add; "-":sub, "*":mul, "/":div}
        if sys.argv[2] not in list(operators.keys()):
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)

            a = int(sys.arg[1])
            b = int(sys.arg[3])

            print("{} {} = {}".format(a, sys.argv[2], b, opearators[sys.argv[2]](a,b)))
