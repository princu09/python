import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'mul':
        return args.x * args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'div':
        return args.x / args.y

    else:
        return "Someting went to wrong"



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--x' , type=float , default=1.0 , help="Enter first number. Please Contact on Twitter @princu09")

    parser.add_argument('--y' , type=float , default=3.0 , help="Enter second number. Please Contact on Twitter @princu09")

    parser.add_argument('--o' , type=str , default="add" , help="Please Contact on Twitter @princu09")

    args = parser.parse_args()

    sys.stdout.write(str(calc(args)))

# ---------------------------Note-----------------------------------------
print("\nFor learn how to run and access python_utility , open this file in your editor and learn about this file")
print("\nThank You\n")