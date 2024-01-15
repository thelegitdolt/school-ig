from Projects.project1.complex import Complex
from Projects.project1.vector2d import Vector2D

# cse30
# lab1
# test modules vector.py and complex.py

if __name__ == '__main__':

    v1 = Vector2D(2, 3)
    v2 = Vector2D(0.5, -1.5)
    v3 = Vector2D(0, 0)
    print(v1.magnitude())
    print(v2.magnitude())
    print(v1 <= v2)

    ################################################################################
    # test vector.py

    score2 = 0
    total2 = 10
    module2 = 'vector.py'
    class2 = 'Vector2D'
    # 1
    try:
        v1 = Vector2D(2, 3)
        v2 = Vector2D(0.5, -1.5)
        v3 = Vector2D(0, 0)
        score2 += 1
        print(f'module {module2} and class {class2} are implemented +1/1')
    except Exception:
        print(f'module {module2} or class {class2} is not implemented +0/{total2}')
    else:
        # 2
        try:
            assert str(v1) == '<2, 3>'
            assert str(v2) == '<0.5, -1.5>'
            assert str(v3) == '<0, 0>'
            score2 += 1
            print('str is implemented correctly +1/1')
        except Exception:
            print('str is not implemented correctly +0/1')
        # 3
        try:
            assert (v1 + v2) == Vector2D(2.5, 1.5)
            assert (v1 + v3) == Vector2D(2, 3)
            score2 += 1
            print('addition is implemented correctly +1/1')
        except Exception:
            print('addition is not implemented correctly +0/1')
        # 4
        try:
            assert (v1 - v2) == Vector2D(1.5, 4.5)
            assert (v1 - v3) == Vector2D(2, 3)
            score2 += 1
            print('subtraction is implemented correctly +1/1')
        except Exception:
            print('subtraction is not implemented correctly +0/1')
        # 5
        try:
            assert (v1 * 3) == Vector2D(6, 9)
            assert (v1 * 0) == Vector2D(0, 0)
            score2 += 1
            print('multiplication is implemented correctly +1/1')
        except Exception:
            print('multiplication is not implemented correctly +0/1')
        # 6
        try:
            assert (v1 / 2) == Vector2D(1.0, 1.5)
            assert (v1 / 0) == None
            score2 += 1
            print('division is implemented correctly +1/1')
        except Exception:
            print('division is not implemented correctly +0/1')
        # 7
        try:
            assert not (v1 == v2)
            assert (v1 * 0 == v3)
            score2 += 1
            print('equivalence is implemented correctly +1/1')
        except Exception:
            print('equivalence is not implemented correctly +0/1')
        # 8
        try:
            assert (v1 > v2)
            print(2)
            assert not (v1 <= v2)
            score2 += 1
            print('comparison is implemented correctly +1/1')
        except Exception:
            print('comparison is not implemented correctly +0/1')
        # 9
        try:
            assert (v1.dot(v2)) == -3.5
            assert (v1.dot(v3)) == 0
            score2 += 1
            print('dot product is implemented correctly +1/1')
        except Exception:
            print('dot product is not implemented correctly +0/1')
        # 10
        try:
            assert str(v1.normalize()) == '<0.5547001962252291, 0.8320502943378437>'
            score2 += 1
            print('normalize is implemented correctly +1/1')
        except Exception:
            print('normalize is not implemented correctly +0/1')

    # output score

    print(f'{module2} score: {score2}/{total2}\n')
    score =  10 + score2
    print(f'your total score is {score}')
    with open('tmp', 'w') as f:
        f.write(str(score))
