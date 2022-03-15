# Chapter 03: Decision Structures and Boolean Logic

### Content
- Youtube video
- Notes
- Problem statement
- Solution
- References

# Youtube video
<div align="center">

[![Overview lecture](https://img.youtube.com/vi/q9go5Hlb02k/0.jpg)](https://www.youtube.com/watch?v=q9go5Hlb02k)

</div>


# Notes
Nothing yet :)

# Problem statement
if-else problem on [Hackerank](https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true)

# Solution

```python
# Chapter 03
# Starting out with python 5th edition
# by: Hossam Hamdy


#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    # even
    if n % 2 == 0:
        if n in range(2, 6):
            print("Not Weird")
        elif n in range(6, 21):
            print("Weird")
        elif n > 20:
            print("Not Weird")

    else:
        print("Weird")
```
# References
- Starting out with Python 5th edition
---

<br>
<div align="center">

Youtube Channel: [Hossam Hamdy](https://www.youtube.com/channel/UCePX533CZyOpMyGGZqxJtAg) <br>
LinkedIn: [Hossam Hamdy](https://www.linkedin.com/in/h0ssamhamdy/)<br>
Blog: [0xGhazy](https://0xghazy.wordpress.com)
</div>