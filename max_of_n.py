n = input("Enter count of numbers: ")
n = int(n)

count = 1
sum = 0
numbers = []

while count <= n:
    number = input("Enter number: ")
    number = int(number)
    numbers = numbers + [number]
    count += 1


max = numbers[0]

for num in numbers:
    if num > max:
        max = num
print("The maximum number is %d" % max)
