#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    userinput = argv[1:]
    number = len(userinput)
    print("{:d} {:s}{:s}".format(number, "arguments"
                                 if number is not 1 else "argument",
                                 "." if number is 0 else ":"))
    for index, arg in enumerate(userinput):
        print("{:d}: {:s}".format(index + 1, arg))
