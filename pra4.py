# Create a lambda function that should double or multiply the number (that we will be passing in the lambda function) by 2. Store the lambda function in a variable named 'double_num'
a=int(input("Enter a number: "))
double_num=lambda a: 2*a
print(double_num(a))