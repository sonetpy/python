import argparse
parser = argparse.ArgumentParser("area of rectangle")
parser.add_argument('--length', required=True, type=int, dest='length', help="Enter length of side 1")
parser.add_argument('--width', type=int, required=True, dest='width', help="enter width of the side2")
args = parser.parse_args()

""" Below function is also another way to code
def cal(length, width):
    area = length * width
    return area
"""
def cal():
    return args.length * args.width


if __name__ == '__main__':
    print(f'width: {args.width}, length: {args.length} , area: {cal()}')
