
# Chapter 02: Input, Processing, and Output

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
Write a Python program that reads the `employee's name`, `number of hours worked`, `hourly payment`, and the `rate of taxes`, and then prints the `employee's previous data with the value of the net salary`.

<div align="center">

![flow](https://user-images.githubusercontent.com/60070427/157214845-091a6aeb-067e-40df-a6a5-90d9b00bd383.png)

</div>

# Solution

```python
# Chapter 02
# Starting out with python 5th edition
# by: Hossam Hamdy

#
## [+] Reading data from the accountant
#

# reading employee name
employee_name = input("Employee name: ")

# reading working hours in float
employee_working_hours = float(input("Working hours: "))

# reading pay per hour in float
employee_pay_per_hour = float(input("Pay per hour: "))

# reading taxes rate in float
taxes_rate = float(input("Taxes rate: %"))


#
## [+] Perform processing
#

# calculate employee slary
salary = employee_pay_per_hour * employee_working_hours

# calculate the taxes value
taxes_value = taxes_rate * salary

# calculate net salary
net_salary = salary - taxes_rate

#
## [+] Display out puts
#

print(f"""\n
    [+] Report for {employee_name}
    ------------------------------
    Employee name: {employee_name}
    Employee working hours: {employee_working_hours}
    Employee pay per hour: {employee_pay_per_hour}
    Employee salary: {salary}$
    Taxes rate: {taxes_rate}%
    ----------------------
    Employee net salary: {net_salary}$
""")
```
# References
- Starting out with Python 5th edition
- [Python in a Nutshell Oreilly](https://www.oreilly.com/library/view/python-in-a/0596001886/ch04s03.html)
- [Formating in python](https://zetcode.com/python/fstring)
- [Flowchart creator](https://app.diagrams.net)
---

<br>
<div align="center">

Youtube Channel: [Hossam Hamdy](https://www.youtube.com/channel/UCePX533CZyOpMyGGZqxJtAg) <br>
LinkedIn: [Hossam Hamdy](https://www.linkedin.com/in/h0ssamhamdy/)<br>
Blog: [0xGhazy](https://0xghazy.wordpress.com)
</div>