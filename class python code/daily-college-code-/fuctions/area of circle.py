# area of circle with argument with return value
def area(r):
    PI = 3.14
    return PI*(r*r)

print("area of circle is ",area(5))

# area of circle without argument with return value

def area():
    r = 5
    PI = 3.14
    return PI*(r*r)
print("area of circle is ",area())


# area of circle with argument without return value

def findarea(r):
    PI = 3.14
    area = PI*(r*r)
    print("area of circle is ",area)
findarea(5)


# area of circle without argument without return value

def findarea():
    r=5
    PI =3.14
    area=PI*(r*r)
    
    print("area of circle is ",area)
findarea()



    