print("""
Print only the numbers 
divisible by 3 from 1 to 100 onto the screen. 
Try to do this with *continue*.
""")

for i in range(1,100):
    if(i % 3 != 0):
        continue
    print(i)