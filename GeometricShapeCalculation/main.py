"""
Now let's do the geometric shape calculation. First, ask the user whether
they want to find the type of triangle or quadrilateral.

If the user answers "Rectangle", ask for 4 sides and try to find out whether
this quadrilateral is a square, a rectangle or an ordinary quadrilateral.

If the user answers "Triangle", ask for 3 sides and try to find out whether this triangle is isosceles,
equilateral or an ordinary triangle. If the given sides do not indicate a triangle,
write "Does not specify a triangle" on the screen.
"""
type = input("Triangle or Quadrilateral?: ")
if(type == "Triangle"):
    edge1 = int(input("Enter the edge1: "))
    edge2 = int(input("Enter the edge2: "))
    edge3 = int(input("Enter the edge3: "))
    if(abs(edge2 - edge3) < edge1 <  edge2 + edge3 and abs(edge1 - edge3) < edge2 < edge1 + edge3 and abs(edge1 - edge2) < edge3 < edge1 + edge2):
        if(edge1 == edge2 == edge3):
            print("Equilateral Triangle")
        elif(edge1 == edge2 or edge2==edge3 or edge1 == edge3):
            print("Isosceles Triangle")
        else:
            print("Ordinary Triangle")
    else:
        print("These edges do not specify a triangle")
elif(type =="Quadrilateral"):
    edge1 = int(input("Enter the edge1: "))
    edge2 = int(input("Enter the edge2: "))
    edge3 = int(input("Enter the edge3: "))
    edge4 = int(input("Enter the edge4: "))
    if(edge1 == edge2 == edge3 == edge4):
        print("Square")
    elif(edge1 == edge2 or edge1 == edge3 or edge1 == edge4):
        print("Rectangle")
    else:
        print("Ordinary Quadrilateral")
else:
    print("Incorrect Entry!")