# Create a list that has 10, 23, 4, 26, 4, 75, 24, 54 values and with the help
# of while loop fetch the even numbers and print the numbes

lis=list((10, 23, 4, 26, 4, 75, 24, 54))
lis_even=[]
for i in lis:
    if i%2==0:
        lis_even.append(i)
print("Even values: ",lis_even)