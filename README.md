# DEBUG
### Simple debug on Python

# Dependencies
**Python 3.x required.** All libraries used in the code are built into Python

# How to use
## variable DEBUG
The debug variable can take the values ​​**True or False**
### Example
```python
from DEBUG import DEBUG

try:
    ...
except Exception as e:
    if DEBUG:
        print(e)
```

## decorator _timer
A decorator that measures **the duration of a program** and _returns_ it

### Example
```python
from DEBUG import _timer
# time is built-in function
import time


@_timer
def test():
    time.sleep(5)


f = test
print(f())
# output: 0:00:05.004447
```
