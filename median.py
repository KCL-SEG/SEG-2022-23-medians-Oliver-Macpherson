"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

median = 0
if(isinstance(numbers,int)):
    median = numbers
else:
    sorted = sorted(numbers)
    if (len(sorted)%2)!=0:
        median = sorted[len(sorted)//2]
    elif len(sorted)%2==0:
        lmid = len(sorted)//2
        umid = lmid-1
        median = (sorted[lmid]+sorted[umid])/2
    else:
        print('Something weird has happened.')

print(median)
