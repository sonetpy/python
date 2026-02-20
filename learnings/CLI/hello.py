# mycli.py

import argparse

parser = argparse.ArgumentParser(description="Simple Greeting CLI")

parser.add_argument("--fname", required=True, help="First Name")
parser.add_argument("--lname", required=True, help="Last Name")

args = parser.parse_args()

# Capitalize first letter
first = args.fname.capitalize()
last = args.lname.capitalize()

print(f"hello {first} {last}!")
# cli command: python mycli.py --fname john --lname doe