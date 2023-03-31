import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python script.py pass agr1 <MailboxSizeReports.csv> arg2 <Recoverable_Items.csv>")
    sys.exit(1)

# Get the values of the arguments
arg1 = sys.argv[1]
arg2 = sys.argv[2]

# Use the arguments as needed
print("Argument 1:", arg1)
print("Argument 2:", arg2)