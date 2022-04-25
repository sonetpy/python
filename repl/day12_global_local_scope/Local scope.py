################### Local Scope ####################
"""
Local Scope : Exist within Function.
Global Scope : Exist within and outside of function.
"""
enemies = 1
def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


### This code will error out because the scope of Variable
### drinks = 2 is within the function and not outside the function.
### so it will give you an error "NameError: name 'drinks' is not defined"
"""
def player_health():
    drinks = 2
    print ("Players are energized")

print (player_health())
print (drinks)
"""

### Use of global ####
### This code is bit dangerous as it is changing my Global variable I declare
### Outside of function.
enemies = 2
def increase_enemies():
  global enemies
  enemies += 1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


# To avoid the above from happening and maintain the integrity of the global variable.
enemies = 1
def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")