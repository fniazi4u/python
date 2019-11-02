import re
def validate(val = []):
    #stri =val.split(',')

    for p in val:
        if len(p) <8 or len(p) >15:
            print ("Password length should be more than 6 characters and less than 15 characters: "+(p))
            continue
        #else:
            #pass
        if not re.search("[a-z]",p):
            print ("Password should contain atleast one lower case character :"+(p))
            continue
        elif not re.search("[0-9]",p):
            print("Password should contain atleast one numeric character :" +(p))
            continue
        elif not re.search("[A-Z]",p):
            print("Password should contain atleast one upper case character :"+(p))
            continue
        elif not re.search("[$#@%&~]", p):
            print("Password should contain atleast one special character :"+(p))
            continue
        elif re.search("\s",p):
            print("Password can not contain white spaces :" + (p))
            continue
        else:
            print( "Correct password :"+p)
            pass
        #val.append(p)


validate(["d#%%ZZcdc","sDD$$" ])