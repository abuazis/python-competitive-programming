# Number Line Jumps Challenge
# https://www.hackerrank.com/challenges/kangaroo/problem

def kangaroo():
    # kangaroo has the following parameter(s):
    # int x1, int v1: starting position and jump distance for kangaroo 1
    # int x2, int v2: starting position and jump distance for kangaroo 2

    # Catch multiple number value
    x1, v1, x2, v2 = map(int, input().split())

    # Check if jump distance kangoroo 1 is further than kangoroo 2
    # and Check if they speed is not same (because if same speed, 
    # they will never meet). So return 'YES' if true else return 'NO'
    return 'YES' if (v1 > v2) and (x2 - x1) % (v2 - v1) == 0 else 'NO'

if __name__ == '__main__':
    # Run logic function
    print(kangaroo())