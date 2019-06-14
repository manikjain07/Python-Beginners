number = int(input("Enter a Number of whose Factorial you want to Find: "))

fact = 1

for j in range(1,number+1):

    if number!=0:
        fact = fact*j

    else:
        fact = 1

print("The Factorial of %d is %d." %(number,fact))