# Note: This code is work in progress




"""
ID: jasonhu5
LANG: PYTHON3
TASK: milk2
"""

def solve(ar):
    ar = sorted(ar, key=lambda x: x[1]) # Sort by finishing time
    max_yes, max_no = ar[0][1] - ar[0][0], 0
    j = 0 # Index of starting activity
    for i, cur in enumerate(ar[:-1]):
        nxt = ar[i+1]
        if cur[1] < nxt[0]: # No overlap
            yes = max(cur[1] - ar[j][0] # Duration for continuous activities
            max_yes = max(max_yes, yes)
            no = nxt[0] - cur[1] # Duration for no activity
            max_no = max(max_no, no)
            j = i + 1
        # TODO: Handle the enclosed scenario
    return (max_yes, max_no)

def test_simple():
    assert solve([(100, 200)]) == (100, 0)
    assert solve([(2, 3), (4, 5), (6, 7), (8, 9), (10, 11), (12, 13), \
                    (14, 15), (16, 17), (18, 19), (1, 20)]) == (19, 0)
    assert solve([(300, 1000), (700, 1200), (1500, 2100)]) == (900, 300)

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
