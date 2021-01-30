import argparse


def parse_b(args):
    print(args.baz)


parser = argparse.ArgumentParser("A helper with various examples for argparse")
parser.add_argument('positional-simple', help="A positional argument")
parser.add_argument('choice', choices=['a', 'b', 'c'], help="mulitple choices")

parser.add_argument('--simple-option', '-s', action='store_const', const=42, help="A simple option value, default to false")
parser.add_argument('--one-value', metavar='val', nargs='?', const='c', default='hello', help="parameter with optional value, default to hello")
parser.add_argument('--two-values', nargs=2, dest="new_arg", metavar=('v1', 'v2'), help="two values are required stored in new_args")
parser.add_argument('--one-int', default='10', type=int, help="int optional value (default: %(default)s)")
parser.add_argument('--multi', nargs='*', metavar='v', help="parameter with optional values")
parser.add_argument('--required', required=True, help="a parameter that is required")

subparsers = parser.add_subparsers(help='sub-commands')
# create the parser for the "a" command
parser_a = subparsers.add_parser('sub-a', help='sub command a')
parser_a.add_argument('bar', type=int, help='bar help')
# create the parser for the "b" command
parser_b = subparsers.add_parser('sub-b', help='sub command b')
parser_b.add_argument('--baz', choices='XYZ', help='baz help')
parser_b.set_defaults(func=parse_b)

parser.parse_args()