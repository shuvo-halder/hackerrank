# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.


def neer_hundred(n):
    if abs(100 - n) <= 10:
        return True
    else:
        if abs(200 - n) <= 10:
            return True
        else:
            return False
        

# i can write this code another way

def near_hundred(n):
    return((abs(100 - n) <= 10 or abs(200 - n) <= 10))