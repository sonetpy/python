# mycli.py

import argparse

def main():
    parser = argparse.ArgumentParser(description="Greeting CLI")

    parser.add_argument("--fname", required=True, help="First Name")
    parser.add_argument("--mname", help="Middle Name")
    parser.add_argument("--lname", required=True, help="Last Name")

    args = parser.parse_args()

    first = args.fname.capitalize()
    last = args.lname.capitalize()

    if args.mname:
        middle = args.mname.capitalize()
        print(f"hello {first} {middle} {last}!")
    else:
        print(f"hello {first} {last}!")
if __name__ == "__main__":
    main()