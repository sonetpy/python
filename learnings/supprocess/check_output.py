import subprocess

# Example: Run the 'ls' command and capture its output
try:
    output = subprocess.check_output(['ls', '-l'], shell=True)
    print(output.decode('utf-8'))  # Decode the bytes to a string
except subprocess.CalledProcessError as e:
    print(f"Error executing command: {e}")

