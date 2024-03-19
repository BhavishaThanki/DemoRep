# Take three user inputs and print the greatest number from those inputs
# using if-else condition. Edge cases, if any, should also be handled.

a,b,c=map(int,input("Enter three space separated values a,b,c: ").split())
if a==b==c:
    print("All values are same!!")
elif a>=b and a>=c:
    print(f"{a} is the greatest number")
elif b>=a and b>=c:
    print(f"{b} is the greatest number")
else:
    print(f"{c} is the greatest number")
