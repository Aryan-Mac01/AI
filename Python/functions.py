#simple function in Python
def simple():
    print("This is a simple function.")
simple()

#function with parameters
def plus_ten(a):
    return a+10
plus_ten(10)

#function within a function
def wage(w_hours):
    return w_hours * 25

def w_bonus(w_hours):
    return wage(w_hours) + 100

wage(8),  w_bonus(8)

#function with conditional statements
def add_10(m):
    if m>=100:
        m=m+10
        return m
    else:
        return "Save More"
add_10(110)

#function with multiple parameters
def subtract(a, b):
    return a - b
subtract(10, 5)