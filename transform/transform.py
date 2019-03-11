"""
ID: jasonhu5
LANG: PYTHON3
TASK: transform
"""

def reflect(ar):
    n = len(ar)
    res = ar.copy()
    for row in range(n):
        res[row] = res[row][::-1]
    return res

def solve(ar1, ar2):
    def rot_cw_90(A, B):
        for row in range(n):
            for col in range(n):
                if A[row][col] != B[col][n-1-row]:
                    return False
        return True

    def rot_cw_180(A, B):
        for row in range(n):
            for col in range(n):
                if A[row][col] != B[n-1-row][n-1-col]:
                    return False
        return True

    def rot_cw_270(A, B):
        for row in range(n):
            for col in range(n):
                if A[row][col] != B[n-1-col][row]:
                    return False
        return True

    def flipped(A, B):
        return reflect(A) == B

    def combination(A, B):
        flipped = reflect(A)
        return rot_cw_90(flipped, B) or rot_cw_180(flipped, B) or rot_cw_270(flipped, B)
        
    n = len(ar1)
    if rot_cw_90(ar1, ar2):
        return 1
    if rot_cw_180(ar1, ar2):
        return 2        
    if rot_cw_270(ar1, ar2):
        return 3
    if flipped(ar1, ar2):
        return 4
    if combination(ar1, ar2):
        return 5
    if ar1 == ar2:
        return 6        
    return 7

# ---- Unit Tests ----
def test_flip():
    # Flip
    assert reflect(['@-@','---','@@-']) == ['@-@','---','-@@']
    assert reflect(['*-@-','@---','-@@-','**0-']) == ['-@-*','---@','-@@-', '-0**']

def test_90():
    ar1 = ['@-@','---','@@-']
    ar2 = ['@-@','@--','--@']
    assert solve(ar1, ar2) == 1

def test_180():
    ar1 = ['@-@','---','@@-']
    ar2 = ['-@@','---','@-@']
    assert solve(ar1, ar2) == 2

def test_270():
    ar1 = ['@-@','---','@@-']
    ar2 = ['@--','--@','@-@']
    assert solve(ar1, ar2) == 3

def test_flipped():
    ar1 = ['@-@','---','@@-']
    ar2 = ['@-@','---','-@@']
    assert solve(ar1, ar2) == 4 

def test_combination():
    ar1 = ['@-@','---','@@-']
    ar2 = ['--@','@--','@-@']
    assert solve(ar1, ar2) == 5    

def test_no_change():    
    ar1 = ['@-@','---','@@-']
    ar2 = ['@-@','---','@@-']
    assert solve(ar1, ar2) == 6

def test_invalid():
    ar1 = ['@-@','---','@@-']
    ar2 = ['-@-','-@-','-@-']
    assert solve(ar1, ar2) == 7

if __name__ == '__main__':
    # test_flip()
    # test_90()
    # test_180()
    # test_270()
    # test_flipped()
    # test_combination()
    # test_no_change()
    # test_invalid()
    fin = open('transform.in','r')
    fout = open('transform.out','w')
    N = int(fin.readline())
    ar1, ar2 = [], []
    for _ in range(N):
        s = fin.readline().strip()
        ar1.append(s)
    for _ in range(N):
        s = fin.readline().strip()
        ar2.append(s)
    ans = solve(ar1, ar2)
    fout.write('{}\n'.format(ans))
