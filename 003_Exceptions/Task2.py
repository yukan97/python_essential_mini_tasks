def add(a, b):
    out = None
    try:
        out =  a + b
    except TypeError:
        
        print("A and B should be numbers")
    return out

def minus(a, b):
    out = None
    try:
        out =  a - b
    except TypeError:
        
        print("A and B should be numbers")
    return out

def multiply(a, b):
    out = None
    try:
        out =  a * b
    except TypeError:
        
        print("A and B should be numbers")
    return out

def divide(a, b):
    out = None
    try:
        out =  a / b
    except TypeError:
        
        print("A and B should be numbers")
    except ZeroDivisionError:
        print('Division by zero is prohibited')
    return out

def power(a, b):
    out = None
    try:
        out =  a**b
    except TypeError:
        
        print("A and B should be numbers")
    except ZeroDivisionError:
        print('Division by zero is prohibited')
    return out

print(add(3, 0))
print(minus(3, 0))
print(multiply(3, 0))
print(divide(3, 0))
print(power(0, -2))
print(add('3', 0))
print(minus('3', 0))
print(multiply('3', 0))
print(divide(3, 2))
print(power(2, 2))