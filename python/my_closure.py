def create_multiply(fact):
    def multiply(num):
        return num*fact
    return multiply


double = create_multiply(2)
triple = create_multiply(3)

print(double(2))
print(triple(2))
