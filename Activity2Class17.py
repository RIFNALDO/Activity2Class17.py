def fact(x):
    if x==0 or x==1:
        return 1 
    else:
        return x*fact(x-1)
    
print("The fact of 0: ",fact(5))
print("The fact of 1: ",fact(1))
print("The fact of 2: ",fact(3))
print("The fact of 5: ",fact(2))
print("The fact of 0: ",fact(6))