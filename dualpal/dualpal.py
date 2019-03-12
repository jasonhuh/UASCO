"""
ID: jasonhu5
LANG: PYTHON3
TASK: dualpal
"""

def convert(num, B):
    digits = '0123456789ABCDEFGHIJK'
    res = []
    while num > 0:
        res.append(digits[num % B])
        num //= B
    return ''.join(reversed(res))

def is_palindrome(s):
    return all(s[i] == s[-i-1] for i in range(len(s)//2))

def solve(N, S):
    res = []
    num = S + 1
    while len(res) < N:
        found = False
        for base in range(2, 11):
            new_base = convert(num, base)
            if is_palindrome(new_base):
                if not found:
                    found = True
                else:  # Found for more than once
                    res.append(num)
                    break
        num += 1                
    return res

def test_convert():
    assert convert(8, 2) == '1000'
    assert convert(15, 16) == 'F'

def test_palindrome():
    assert is_palindrome('1000') == False
    assert is_palindrome('1001') == True
    assert is_palindrome('10101') == True

def test_solution():
    assert solve(3, 25) == [26, 27, 28]
    assert solve(9, 10) == [15, 16, 17, 18, 20, 21, 24, 26, 27]

if __name__ == '__main__':
    fin = open('dualpal.in','r')
    fout = open('dualpal.out','w')
    N, S = map(int, fin.readline().strip().split()) # Base
    ans = solve(N, S)
    fout.write(''.join(str(num) + '\n' for num in ans))
    fout.close()
