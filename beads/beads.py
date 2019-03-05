"""
ID: jasonhu5
LANG: PYTHON3
TASK: beads
"""
def solve(txt):
    def traverse(idx, color, dir):
        res, cur = 0, idx
        while cur >= 0 and cur < n:
            if s[cur] == color or s[cur] == 'w':
                cur += dir
                res += 1
            else:
                break
        return res

    s, n = txt*2, len(txt)*2
    res, i = 0, 0
    while i < n:
        l, r = s[i-1], s[i]
        left_leng, right_leng = 0, 0
        if l == 'w': # Try both 'r' and 'b' and see which is bigger
            left_leng = max(traverse(i-1, 'r', -1), traverse(i-1, 'b', -1))
        else:
            left_leng = traverse(i-1, l, -1)

        if r == 'w': # Try both 'r' and 'b' and see which is bigger
            right_leng = max(traverse(i, 'r', 1), traverse(i, 'b', 1))
        else:
            right_leng = traverse(i, r, 1)

        res = min(n//2, max(res, (left_leng + right_leng)))
        i += 1
    return res

def test_simple():
    txt = 'ww'
    assert solve(txt) == 2

def test_simple2():
    txt = 'wwwbbrwrbrbrrbrbrwrwwrbwrwrrb'
    assert solve(txt) == 11

def test_simple3():
    txt = 'rwrwrwrwrwrwrwrwrwrwrwrwbwrwbwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwr'
    assert solve(txt) == 74

if __name__ == '__main__':
    # test_simple()
    # test_simple2()
    # test_simple3()

    fin = open('beads.in', 'r')
    fout = open('beads.out', 'w')
    N = int(fin.readline().strip())
    txt = fin.readline().strip()
    ans = solve(txt)
        
    fout.write(str(ans) + '\n')
    fout.close()
