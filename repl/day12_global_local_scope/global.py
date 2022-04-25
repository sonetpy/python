################# global ############################
"""
Local Scope : Exist within Function.
Global Scope : Exist within and outside of function.
"""
drinks = 10
def player_health():
    drinks = 2
    print ("Players are energized by taking drinks ", drinks)

print (player_health())
print (drinks)

