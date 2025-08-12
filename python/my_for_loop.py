# type 1
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

# type 2
for i in range(1, 11):
    print(15 * i)

# type 3
for i in range(1, 100, 2):
    print(i)

# type 4
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print("Total even numbers:", count)
