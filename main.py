def main():
    while True:
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))

        print("""
                1. Add
                2. Subtract
                3. Multiply
                4. Divide
        """)

        c = input("Operation (1/2/3/4): ")

        if c == 1:
            print(x + y)
        if c == 2:
            print(x - y)
        if c == 3:
            print(x * y)
        if c == 4:
            print("Quotient: " + str(x / y))
            print("Remainder: " + str(x % y))

        m = input("Want to do more calculation [Y/n]: ")

        if m.lower() == 'y' or 'yes':
            continue
        elif m.lower() == 'n' or 'no':
            break
        else:
            continue

main()