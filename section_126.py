#section_126.py

import math

class QuadError(Exception):
    pass

def quad(a,b,c):
    if a == 0:
        qe = QuadError("이차 방정식이 아니에요.")
        qe.member= (a, b, c)
        raise qe
    if b*b-4*a*c < 0:
        qe = QuadError("방정식의 근이 없어요.")
        qe.member= (a, b, c)
        raise qe
    x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    return (x1, x2)

def getQuad( a, b, c ):
    try:
        x1, x2 = quad( a, b, c )
        print("방정식의 근은", x1, x2)
    except QuadError as err:
        print(err, err.member)

getQuad(0, 100, 10)
