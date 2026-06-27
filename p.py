number=int(input("Enter number:"))

digits= len(str(number))
s=0
while number !=0:
    n= number%10
    s += n ** digits
    number //=10

if(s==number):
    print("The number is a special number")
else:
    print("The number is not a special number")
    

