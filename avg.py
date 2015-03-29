n = input("Enter count of numbers: ")
n = int(n)

count = 1
sum = 0

while count <= n:
    number = input("Enter number: ")
    number = int(number)

    sum = sum + number

    count += 1
avg  = sum / n    
print("The average of numbers is %d" % avg)
