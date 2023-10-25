def calculate(n1,n2,op):
    try:

        if op in ["+", "-", "/", "*"]:

            if op == "+":
                ans = n1 + n2

            elif op == "-":
                ans = n1 - n2

            elif op == "*":
                ans = n1 * n2

            elif op == "/":
                ans = n1 / n2
            return ans
        else:
            return 'ERROR'
    except:
        return 'ERROR'
    
    



