def s_print(sp):
    if sp == 0:
        return
    print("*"*sp)
    s_print(sp-1)
    
n=int(input("Enter numbers of lines: "))
s_print(n)
    