# Chapter 03: Repetition Structures

### Content
- Youtube video
- Notes
- Problem statement
- Solution
- References

# Youtube video
<div align="center">

[![Overview lecture](https://img.youtube.com/vi/wkfMoBoZvpk/0.jpg)](https://www.youtube.com/watch?v=wkfMoBoZvpk)

</div>


# Notes
Nothing yet :)

# Problem statement

finding-the-percentage problem on [Hackerank](https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true)

# Solution

```python
# Chapter 03
# Starting out with python 5th edition
# by: Hossam Hamdy
if __name__ == '__main__':
    n = int(input())
    student = dict()
    for i in range(0, n):
        x = input()
        x = x.split(" ")
        student[x[0]] = "{:.2f}".format((float(x[1]) + float(x[2]) + float(x[3])) / 3)
    query_name = input()
    print(student[query_name])
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