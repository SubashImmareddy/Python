marks = int(input("Enter your marks:\n"))

if 90 <= marks <= 100:
    print("A Grade")
elif 80 <= marks < 90:
    print("B Grade")
elif 70 <= marks < 80:
    print("C Grade")
elif 60 <= marks < 70:
    print("D Grade")
elif 50 <= marks < 60:
    print("E Grade")
elif 0 <= marks < 50:
    print("F Grade")
else:
    print("Invalid marks")