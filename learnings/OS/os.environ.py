'''
In this example, we first set the value of the variable my_var. We then use the subprocess.run method to execute the export command with the variable name and value as arguments. The shell=True argument tells subprocess.run to run the command in a shell environment.

We then check if the variable is exported by running the env command and filtering the output for the variable name using grep. The capture_output=True argument tells subprocess.run to capture the output of the command, and the text=True argument tells it to return the output as a string.

Finally, we print the output to the console to confirm that the variable has been exported. Note that the export command only exports the variable for the current shell session. To make the variable available to other processes or future shell sessions, you may need to add the export command to your shell startup file (e.g., ~/.bashrc).
'''
import os
import subprocess

# set the variable
my_var = 'my_value'

# export the variable
os.environ['MY_VAR'] = my_var

# check if the variable is exported
result = subprocess.run('env | grep MY_VAR', shell=True, capture_output=True, text=True, check=True)

print(result.stdout.strip())  # output: MY_VAR=my_value