import re
password=input("Enter the passsword:")
x = True
while x:
    if (len(password)<6 or len(password)>12):
        break
    elif not re.search("[a-z]",password):
        break
    elif not re.search("[A-Z]",password):
        break
    elif not re.search("[0-9]",password):
        break
    elif not re.search("[$#@]",password):
        break
    else:
        print('valid password')
        x=False
        break
if x:
    print("invalid password")