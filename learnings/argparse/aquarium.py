import argparse
tank_to_fish = {
    "tank_a": "shark, tuna, herring",
    "tank_b": "cod, flounder",
}
parser = argparse.ArgumentParser(description="List fish in aquarium.")
"""Calling add_argument on parser allows you to add arguments accepted by your command-line interface. In this case, you add a single argument named tank that is a string type."""
parser.add_argument("sonu", type=str)
"""Calling parser.parse_args() instructs parser to process and validate the command-line input passed to aquarium.py (for example, something like tank_a).
Accessing the args returned by parser.parse_args() allows you to retrieve the value of the passed in tank argument, and use it to print out the fish in that tank.
"""
args = parser.parse_args()
# Here args.sonu is the string that I inserted in sonu parameter. 
# What I inserted in sonu parameter is "tank_a OR tank_b".

fish = tank_to_fish.get(args.sonu, "")
print(fish)
