"""
ID: jasonhu5
LANG: PYTHON3
TASK: milk2
"""

def solve(ar):
    # Combine overlapping events
    def merge_events(ar):
        ar = sorted(ar, key=lambda x: x[0]) # Sort by start time    
        stack = [ar[0]]
        for _, event in enumerate(ar[1:]):
            top = stack[-1]
            if top[1] >= event[0]: # Events overlap
                if top[1] < event[1]:
                    stack.pop()
                    stack.append((top[0], event[1]))
            else:
                stack.append(event)
        return stack
    finals = merge_events(ar)
    max_range, max_space = finals[0][1] - finals[0][0], 0
    for i, event in enumerate(finals[1:], 1):
        max_range = max(max_range, event[1] - event[0])
        max_space = max(max_space, event[0] - finals[i-1][1])
    return (max_range, max_space)
        
def test_simple():
    assert solve([(100, 200)]) == (100, 0)
    assert solve([(300, 1000), (700, 1200), (1500, 2100)]) == (900, 300)
    assert solve([(2, 3), (4, 5), (6, 7), (8, 9), (10, 11), (12, 13), \
                    (14, 15), (16, 17), (18, 19), (1, 20)]) == (19, 0)
    assert solve([(100, 200), (200, 400), (400, 800), (800, 1600), (50, 100), \
                    (1700, 3200)]) == (1550, 100)

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
