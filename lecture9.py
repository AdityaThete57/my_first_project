total = 0
def add_to_total(value):
    global total #not to create a new local variable, but to use the global variable.
    total += value
    return total
add_to_total(10)
print(total) #unboundlocal error as it is modified in local scope, if global total not written
add_to_total(5)
print(total) #15

def update_local(error,dt):
    global integral #to use the global variable integral
    integral = 0.0 #defined as a local variable, so it will not affect the global variable integral
    integral += error*dt
    return integral
print(update_local(2,0.1)) #0.2
print(integral) #0,0 as it is not modified in global scope
print(update_local(3,0.1)) #0.3