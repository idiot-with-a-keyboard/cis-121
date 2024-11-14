"""
Your name
Date

This program test your vector class.
"""

from VectorClass import *

def main():
	#implement the three vectors in the instructions.
    v1 = Vector(3,2)
    v2 = Vector(-2,6)
    v3 = Vector(4,0)


    run_tests(v1,v2,v3)




#This tests your code.  Don't edit the code below.
def run_tests(vec1, vec2, vec3):
    test_str_rep(vec1, vec2, vec3)
    test_magnitude(vec1, vec2, vec3)
    test_equals(vec1, vec2, vec3)
    test_less_than(vec1, vec2, vec3)
    test_add(vec1, vec2, vec3)


def test_str_rep(vec1, vec2, vec3):
    if (vec1.__str__() == "3x + 2y" and 
        vec2.__str__() == '-2x + 6y' and 
        vec3.__str__() == '4x + 0y'):
        print("Your __str__ method seems to be working correctly")
    else:
        print('this is what your vectors looks like compared to what they should be')
        print(f'{vec1.__str__()} == 3x + 2y and {vec2.__str__()} == -2x + 6y and {vec3.__str__()} == 4x + 0y')

def test_less_than(vec1, vec2, vec3):
    if (vec1<vec2 and vec1<vec3):
        print("Your __lt__ method seems to be working correctly")
    else:
        print("Your __lt__ method contains an error")

def test_add(vec1, vec2, vec3):
    if ((vec1 + vec2 + vec3).__str__() == "5x + 8y"):
        print("Your __add__ method seems to be working correctly")
    else:
        print("Your __add__ method contains an error")

def test_equals(vec1, vec2, vec3):
    if (vec2 == Vector(-2,6) and not (vec1 == vec2)):
        print("Your __eq__ method seems to be working correctly")
    else:
        print("Your __eq__ method contains an error")

def test_magnitude(vec1, vec2, vec3):
    if (((vec1.magnitude() - 3.605551275463989) < 0.0000000001) and 
            ((vec2.magnitude() - 6.324555320336759) < 0.0000000001) and 
            ((vec3.magnitude() - 4) < 0.0000000001)):
        print("Your magnitude method seems to be working correctly")
    else:
        print("Your magnitude method contains an error")

if __name__ == "__main__":
    main()
