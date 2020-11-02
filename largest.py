a= []
num = int(input("Enter the range of number: "))
for i in range (1, num+1):
    b=int(input("Enter a number: "))
    a.append(b)
a.sort()
print("The largest number is:" ,a[num-1])
