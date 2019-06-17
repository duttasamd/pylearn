import argparse

def fib(n) :
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b

    return a

def argparser1() :
    parser = argparse.ArgumentParser()

    parser.add_argument("num", help="Position on the fibonacci series.", type=int)
    parser.add_argument("-o", "--output", help="Output file to write the result.", action="store_true")

    args = parser.parse_args()

    print("The argument was", args.num)

    print("The number at position {} of the fibonacci sequence is {}".format(args.num, fib(args.num)))

    if args.output :
        f = open("fibonacci.txt", "a")
        f.write("The number at position {} of the fibonacci sequence is {}.\n".format(args.num, fib(args.num)))


# Advanced. Mutually Exclusive groups.
def argparser2() :
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()

    group.add_argument("-v", "--verbose", action="store_true", help="User friendly mode.")
    group.add_argument("-q", "--quiet", action="store_true", help="Raw output.")

    parser.add_argument("num", help="Position on the fibonacci series.", type=int)
    parser.add_argument("-o", "--output", help="Output file to write the result.", action="store_true")

    args = parser.parse_args()

    if args.verbose :
        print("The argument was", args.num)
        print("The number at position {} of the fibonacci sequence is {}".format(args.num, fib(args.num)))
    elif args.quiet :
        print(fib(args.num))
    else :
        print("fib({}) = {}".format(args.num, fib(args.num)))

    if args.output :
        f = open("fibonacci.txt", "a")
        f.write("The number at position {} of the fibonacci sequence is {}.\n".format(args.num, fib(args.num)))

# run the program with parameter num and option -o
# $ python 06_argparse.py 8 -o

if __name__ == '__main__':
    # argparser1()
    argparser2()