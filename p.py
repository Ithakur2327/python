year = int(input("Enter a year: "))
if year%4 ==0 & year%100 !=0 & year% 400 ==0:
    print(year, "leap year")
else:
    print(year, "not a leap year")

