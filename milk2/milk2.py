# Note: This code is work in progress




"""
ID: jasonhu5
LANG: PYTHON3
TASK: milk2
"""

"""
ID: jasonhu5
LANG: PYTHON3
TASK: milk2
"""

"""
ID: jasonhu5
LANG: PYTHON3
TASK: milk2
"""

def solve(ar):
    n = len(ar)
    ar = sorted(ar, key=lambda x: x[1]) # Sort by finishing time
    max_yes, max_no = ar[0][1] - ar[0][0], 0
    j = 0 # Index of starting activity
    start = ar[0][0]
    for i, cur in enumerate(ar[:-1]):
        nxt = ar[i+1]
        yes = nxt[1] - nxt[0]
        if cur[1] >= nxt[0]: # Overlap
            start = min(start, nxt[0])
            yes = max(yes, nxt[0] - start)
        else:
            yes = max(yes, cur[1] - start) # Duration for continuous activities
            no = nxt[0] - cur[1] # Duration for no activity
            max_no = max(max_no, no)
            print(max_no, no)
        max_yes = max(max_yes, yes)            
    return (max_yes, max_no)

def test_simple():
    assert solve([(100, 200)]) == (100, 0)
    assert solve([(300, 1000), (700, 1200), (1500, 2100)]) == (900, 300)
    assert solve([(2, 3), (4, 5), (6, 7), (8, 9), (10, 11), (12, 13), \
                    (14, 15), (16, 17), (18, 19), (1, 20)]) == (19, 0)
    

if __name__ == '__main__':
    test_simple()

    fin = open('milk2.in', 'r')
    fout = open('milk2.out', 'w')
    N = int(fin.readline().strip())
    ar = []
    for _ in range(N):
        start, finish = map(int, fin.readline().strip().split())
        ar.append((start, finish))
    ans = solve(ar)
    fout.write('{} {}\n'.format(ans[0], ans[1]))
    fout.close()
