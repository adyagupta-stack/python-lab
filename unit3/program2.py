nos=int(input("Enter total subjects:"))
b=0
for i in range(nos):
    a=int(input("Enter mark of subject:"))
    b+=a
c=b/nos
print("The Average is ",c)
if c>90:
    print("Grade A")
elif c>80:
    print("Grade B")
elif c>70:
    print("Grade C")
else:
    print("Sorry you are fail :(")
    
