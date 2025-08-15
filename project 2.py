#### print("Welcome to the pattern generator and pattern analyzer!")
while True:
    print("\nSelect an option")
    print("1. Generate a pattern")
    print("2. Analyze a Range of Number")
    print("3. Exit")
    choice = int(input("Enter a choice: "))
    if choice == 1:
        pattern = int(input("Enter the number of raws for pattern: "))
        print("\npattern:")
        for i in range(pattern+1):
            print("*" * i)
    elif choice == 2:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        if start > end:
            print("Enter correct value")
        else:
            sum = 0
            for i in range(start, end+1):
                if i%2 == 0:
                    print(f"number {i} is even")
                else:
                    print(f"number {i} is odd")
                sum = sum + i
            print(f"sum of all number from {start} to {end}:", sum)
    elif choice == 3:
        print("Exiting the program. GoodBye !")
    else:
        print("invalid choice, Please select correct option")
        break

        

