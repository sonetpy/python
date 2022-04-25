"""
Adding an Optional Argument
Sometimes, it’s helpful to include optional arguments in your command-line interface. These options are typically prefixed with two dash characters, for example --some-option. Let’s rewrite aquarium.py with the following adjusted content that adds an --upper-case option to your CLI:
"""

import argparse

tank_to_fish = {
    "tank_a": "shark, tuna, herring",
    "tank_b": "cod, flounder",
}

parser = argparse.ArgumentParser(description="List fish in aquarium.")
parser.add_argument("tank", type=str)
parser.add_argument("--upper-case", default=False, action="store_true")
args = parser.parse_args()

fish = tank_to_fish.get(args.tank, "")


"""
Note that, although the argument is two words separated by a dash (upper-case), argparse makes it available to your code as args.upper_case (with an underscore separator) after you call parser.parse_args(). 
In general, argparse converts any dashes in the provided arguments into underscores so that you have valid Python identifiers to reference after you call parse_args().
"""
if args.upper_case:
    fish = fish.upper()


print(fish)