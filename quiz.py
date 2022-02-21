#CS175
#Thomas Schulz
#rainfall.py

a = 0
Sum = 0
x = int(input("Enter number of years: "))
while x < 1 or x > 10:
    x = int(input("Enter number of years: "))
    if x < 1 or x > 10:
        print("Invalid years..!!!")
for i in range(x):
    print("Enter Rainfall in year", i+1," : ")
    for i in range(12):
        print("Enter Rainfall in month", i+1, ": ", end =' ')
        V = float(input())
        Sum = Sum + V
        a= a + 1
Avg = Sum/a
print("Total rainfall = ", Sum)
print("Average rainfall per month = ", Avg)
