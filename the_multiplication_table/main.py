print("""
Try to print a multiplication table on the screen with numbers from 1 to 10.
""")
for i in range(1,10):
    print("For {}\n------------".format(i))
    for j in range(1,10):
        print("{} x {} = {}".format(i,j,i*j))
    print("\n")
