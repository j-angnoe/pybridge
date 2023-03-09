# Ik kan een andere module gewoon importen as regular.
import another_module

# Scope werkt goed
myvar = 1

def hoi(*args):
    data = [[1,2,3],[1,2,3],[1,2,3],[1,2,3]]
    return data
    
def doei():
    # return tuple werkt.
    return myvar, another_module.bla()

