import string
import random
import secrets
lletters=string.ascii_lowercase
uletters=string.ascii_uppercase
digits=string.digits
special_chars=string.punctuation

num=int(input("Enter the number of characters in your password:"))
while True:
    if num<8:
        ch=input("It is recommended for the password to be more than 8 characters long. Do you still wish to proceed?(y/n):)")
        if ch=='y':
            break
        else:
            num=int(input("Enter the number of characters:"))
    else:
        break

def pw(num):
    password_len=num
    choice = int(input("""1. Type 1 for Only Letters and Numbers
2. Type 2 for Only Letters and Symbol
3. Type 3 for Only Numbers and Symbol
4. Type 4 for Letters, Numbers and Symbol
Which combination do you want? : """))
    password = ""
    while True:
        if choice==1:
            selection_list=lletters+uletters+digits
            for i in range(password_len):
                password+= ''.join(secrets.choice(selection_list))
            print("Your password is:",password)
        elif choice==2:
            selection_list=lletters+uletters+special_chars
            for i in range(password_len):
                password+= ''.join(secrets.choice(selection_list))
            print("Your password is:",password)
        elif choice==3:
            selection_list=digits+special_chars
            for i in range(password_len):
                password+= ''.join(secrets.choice(selection_list))
            print("Your password is:",password)
        elif choice==4:
            selection_list=lletters+uletters+digits+special_chars
            for i in range(password_len):
                password+= ''.join(secrets.choice(selection_list))
            print("Your password is:",password)
        return password
pw(num)        
while True:
    c = input("Do you want to continue? (y/n): ")
    if c == 'y':
        num = int(input("Enter the number of characters in your password: "))
        pw(num)
    else:
        break
   
    
