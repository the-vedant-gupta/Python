"""
Write a function get_stats(num) that takes a tuple of numbers and returns a tuple containing the
sum, average, mminimum and maximum. Unpack the returned tuple and print each value
"""

# marks = (45, 65, 87, 45, 33, 55)


def marks_insights(tpl):
    n = len(tpl)
    maxi = float("-inf")
    min = float("inf")
    total = 0
    for i in tpl:
        if i > maxi:
            maxi = i
        if i < min:
            min = i
        total += i
        average = total / n
    return maxi, min, total, average


numbers = ()
for i in range(5):
    value = int(input("Enter a number: "))
    numbers += (value,)

Maxi, Mini, Total, Average = marks_insights(numbers)

print(f"Tuple: {numbers}")
print(f"Maximum is : {Maxi}")
print(f"Minimum is : {Mini}")
print(f"Sum is : {Total}")
print(f"Average is : {Average:.2f}")
