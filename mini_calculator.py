first=input("enter first number:")
first=int(first)

while True:
    operator=input("enter operator (+,-,*,/,%):")
    second=input("enter second number:")
    second=int(second)
    if operator== "+":
        result=first+second
    elif operator== "-":
        result=first-second
    elif operator== "*":
        result=first*second
    elif operator== "/":
        result=first/second
    elif operator== "%":
        result=first%second
    else:
        result = None
        print("invalid operation")

    print(result)
    first=result
    con = input('continue ? [[y]/n]')
    
    if con == 'n':
        break

    