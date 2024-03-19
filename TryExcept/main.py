"""
Imagine you have a list of strings.
Print the strings in this list that contain only numbers to the screen.
Don't forget to use try,except blocks while doing this.
"""

liste = ["345","NewYork","324a","14","Furkan"]
for i in liste:
    try:
        i = int(i)
        print(i)
    except:
        pass