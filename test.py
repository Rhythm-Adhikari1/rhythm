def main():
    expression =input("expression: ")
    expression =expression.split(' ')
    x=float(expression[0])
    y=float(expression[2])
    match expression[1]:
        case '+' : result= x + y
        case '*' : result =x * y
        case '-' : result = x-y
        case '/' : result = x/y
        case _: 
            print("inappropriate  operand")
            return
    
    print(result)

main()