import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('nums', nargs='*')
args = parser.parse_args()

print(args)
