#write a Python program that accepts a sentence and find the number of 
#words, digits, uppercase letters and lowercase letters.
s=input("Enter a sentence:")
w,d,l,u=0,0,0,0
l_w=s.split()
w=len(l_w)
for c in s:
    if c.isdigit():
        d=d+1
    elif c.islower():
        l=l+1
    elif c.isupper():
        u=u+1
print("words",w,"upper",u,"lower",l,"digits",d)
