The key to this problem is to sort each milk by price, and then *greedily* add amount of each milk with lowest price 
until the total amount of added milk is the same as N.

Here is a solution:

```py
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
```
