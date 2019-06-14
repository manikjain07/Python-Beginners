def main():
    number1 = int(input("Enter a Number: "))
    number2 = int(input("Enter another Number: "))
    sum()

def sum(number1,number2):
    number_sum = number1 + number2
    print("The sum of %d and %d is %d" %(number1,number2,number_sum))

if __name__ == '__main__':main()

