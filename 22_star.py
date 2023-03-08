for i in range(1, 10):
    print("*"*i)

for i in range(0, 10):
    print(" "*(10-i-1),end="")
    print("*"*(i*2+1),end="")
    print(" "*(10-i-1))