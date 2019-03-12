This question is a slight variation of the previous problem, palsquare. The _gotcha_ of this problem is this problem statement:

'... palindromic when written in two or more number bases'

So, the solution needed to tract if a palindrome is found. If it's already found, then a number with different base is found again, 
then the number can be included in the list of result. Here is a gist of the technique.

```python
found = False
for base in range(2, 11): # From base 2 to base 10.
    new_base = convert(num, base)
    if is_palindrome(new_base):
        if not found:
            found = True # Mark as found
        else:  # palindrome has been found for more than once
            res.append(num)
            break
```
