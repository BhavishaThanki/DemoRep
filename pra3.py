# Create a function named ‘check_string’, the function should accept a string
# data from the user and the function should check if the user input contains
# the letter ‘s’ in it. If it contains the letter ‘s’ then print- ‘The string is
# containing the letter ‘s’’, if not then print- ‘The string doesn’t contain the
# letter ‘s’.

# def check_string(mystr):
#     for i in mystr:
#         if i=="s" or i=="S":
#             flag=1
#             break
#         else:
#             flag=0
#     if flag==1:
#         print(f"'{mystr}' is containing the letter 's' ")
#     else:
#         print(f"'{mystr}' doesn't contain the letter 's'")

def check_string(mystr):
    if mystr.find("s")!=-1:
        print(f"'{mystr}' is containing the letter 's' ")
    else:
        print(f"'{mystr}' doesn't contain the letter 's'")

strin=input("Enter String: ")
check_string(strin)
