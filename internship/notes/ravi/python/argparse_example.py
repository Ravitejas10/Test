import argparse
#https://docs.python.org/3/library/argparse.html
#https://www.geeksforgeeks.org/command-line-option-and-argument-parsing-using-argparse-in-python/
# # Initialize the Parser
# parser = argparse.ArgumentParser(description='Process some integers.')
#
# # Adding Arguments
# parser.add_argument('integers', metavar='N',
#                     type=int, nargs='+',     #nargs : + means one or more argument needs to be passed in the terminal, * means zero or more argument needs to be passed
#                     help='an integer for the accumulator')
#
# parser.add_argument(dest='accumulate',
#                     action='store_const',
#                     const=sum,
#                     help='sum the integers')
#
# args = parser.parse_args()
# print(args.accumulate(args.integers))
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))

