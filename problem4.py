from fractions import Fraction # this function make 2 3 into 2/3 simplest form
from functools import reduce

def product(fracs):
    t = Fraction(reduce(lambda x,y: x*y,fracs))
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)  # fracs is a list of fractional tuple objects
    print(*result)