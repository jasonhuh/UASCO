The problem requires to break it down to two steps:
1. Implement a function to convert a base 10 number to any base (between 1 ~ 20).
2. Implement a function that determins if a given string is palindrom or not.

### Step 1 - Convert a number to any base
```python
def convert(num, B):
    digits = '0123456789ABCDEFGHIJK'
    res = []
    while num > 0:
        res.append(digits[num % B])
        num //= B
    return ''.join(reversed(res))
```

### Step 2 - Determin if a given string is palindrom or not
```python
def is_palindrom(s):
    return all(s[i] == s[-i-1] for i in range(len(s)//2))
```
