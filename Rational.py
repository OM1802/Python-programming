#code to check if a number is rational or not 
from fractions import Fraction

def is_rational(number):
    try:
        Fraction(number)
        return True
    except ValueError:
        return False
num = 2.5
result = is_rational(num)

if result:
    print(f"{num} is a rational number.")
else:
    print(f"{num} is not a rational number.")

