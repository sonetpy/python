import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-H', '--host',default='localhost',dest='host',help='Provide destination host. Defaults to localhost',type=str)
args = parser.parse_args()
print(f'The host is "{args.host}"')