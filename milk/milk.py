"""
ID: jasonhu5
LANG: PYTHON3
TASK: milk
"""

from collections import namedtuple

Milk = namedtuple('Transaction', 'price, amount')

def solve(N, milks):
    milks = sorted(milks, key=lambda milk : milk.price)
    total_price, sofar_amt, i = 0, 0, 0
    while sofar_amt < N:
        cur = milks[i]
        amt = min(N - sofar_amt, cur.amount)
        sofar_amt += amt
        total_price += (amt * cur.price)
        i += 1
    return total_price

def test_simple():
    N = 100
    milks =[Milk(5, 20), Milk(9, 40), Milk(3, 10), Milk(8, 80), Milk(6, 30)]
    assert solve(N, milks) == 630

if __name__ == '__main__':
    test_simple()
    fin = open('milk.in','r')
    fout = open('milk.out','w')
    N, M = map(int,fin.readline().strip().split())
    milks = []
    for _ in range(M):
        P, A = map(int, fin.readline().strip().split())
        milks.append(Milk(price=P, amount=A))
    ans = solve(N, milks)
    fout.write('{}\n'.format(ans))
    fout.close()
