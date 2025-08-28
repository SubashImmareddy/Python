a = int(input("Enter the numbers"))
b = int(input("Enter the numbers"))
c = int(input("Enter the numbers"))
def greatest(a,b,c):
 if(a>b and a>c):
  return a
 elif(b>a and b>c):
  return b
 elif(c>a and c>b):
  return c
 

print(greatest(a,b,c))

"""cant handle if numbers are equal ik"""
   