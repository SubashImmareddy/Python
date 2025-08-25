v = int(input("Enter a number:\n"))
x = int(input("Enter a number:\n"))
y = int(input("Enter a number:\n"))
z = int(input("Enter a number:\n"))

if (v>x and v>y and v>z):
    print(f"{v} is greatest")
elif (x>v and x>y and x>z):
    print(f"{x} is greatest")
elif (y>z and y>x and y>v):
    print(f"{y} is greatest")
elif (z>y and z>x and z>v):
    print(f"{z} is greatest")