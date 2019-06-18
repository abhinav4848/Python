import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--geo', nargs=2)
parser.add_argument('--pos', nargs=2)
parser.add_argument('type')

args = parser.parse_args()

print(args)
