def inches_cm(ic):
    return ic * 2.54   

inch = float(input("Enter Value in inches: "))  
cm = inches_cm(inch)
print(f"{inch} inches = {cm} cm")   
