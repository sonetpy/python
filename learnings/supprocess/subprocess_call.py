import subprocess

# Example: Execute the 'ls -l' command
try:
    subprocess.call(['ls', '-l'])
except subprocess.CalledProcessError as e:
    print(f"Error executing command: {e}")
