def main():
    number1 = int(input("Enter a Number: "))
    number2 = int(input("Enter another Number: "))
    sum(number1,number2)

def sum(number1,number2):
    number_sum = int(number1) + int(number2)
    print("The sum of %s and %s is %d." %(number1,number2,number_sum))

if __name__ == '__main__':main()

