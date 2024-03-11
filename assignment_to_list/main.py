print("""
Try dropping only even numbers from 1 to 100 into a list with list comprehension.
""")
a = [x for x in range(1,101) if x % 2 == 0]
print(a)