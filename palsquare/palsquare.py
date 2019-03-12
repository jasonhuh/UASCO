"""
ID: jasonhu5
LANG: PYTHON3
TASK: palsquare
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

def solve(B):
    N = 300
    res = []
    for i in range(1, N+1):
        square_base = convert(i*i, B)
        if is_palindrome(square_base):
            num_base = convert(i, B)
            res.append('{} {}\n'.format(num_base, square_base))
    return res

def test_convert():
    assert convert(8, 2) == '1000'
    assert convert(15, 16) == 'F'

def test_palindrom():
    assert is_palindrome('1000') == False
    assert is_palindrome('1001') == True
    assert is_palindrome('10101') == True

if __name__ == '__main__':
    fin = open('palsquare.in','r')
    fout = open('palsquare.out','w')
    B = int(fin.readline().strip()) # Base
    ans = solve(B)
    fout.write(''.join(ans))
    fout.close()
