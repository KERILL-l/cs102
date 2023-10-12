while True:
    print("Write first number:")
    try:
        n1 = float(input())
        print("Correct operations: + - * /")

        print("Write operation:")
        op = input()

        if op in ["+", "-", "/", "*"]:
            print("Write second number:")
            n2 = float(input())

            if op == "+":
                ans = n1 + n2

            elif op == "-":
                ans = n1 - n2

            elif op == "*":
                ans = n1 * n2

            elif op == "/":
                ans = n1 / n2

            print(str(ans) + "\n")
        else:
            print("ERROR\n")
    except:
        print("ERROR\n")
