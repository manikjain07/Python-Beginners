name = input("Enter your Name: ")

name_length = len(name)

for i in range(0,name_length):

    for j in range(0,i+1):

        print(name[j],end="")

    print()