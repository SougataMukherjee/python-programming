high_income = False
good_credit = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")

# using ternary

age = 12
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

#type 2
name = input("Name: ")
age = int(input("Age: "))
price = float(input("Price: "))

A = int(input("Enter A: "))
G = input("Enter gender (M/F): ")

if (A == 1 or A == 2) and G == "M":
    print("Fee is 100")
elif A == 3 or A == 4 or G == "F":
    print("Fee is 200")
else:
    print("No fee")

