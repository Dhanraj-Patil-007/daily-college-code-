# area of rectrangle without argument with return value 

def farea():
    l=10
    w = 10
    return l*w
print("area of rectrangle = ",farea())

# area of rectrangle with argument without return value 

def farea(l,b):
    area = l*b
    print("area of rectrangle = ",area)
farea(10,10)

    
# area of rectrangle without argument without return value 


def farea():
    l=10
    w=10
    area = l*w
    print("area of rectrangle = ",area)
farea()

    
# area of rectrangle with argument with return value 

def farea(l,w):
    area = l*w
    return area
print("area of rectrangle = ",farea(10,10))
    