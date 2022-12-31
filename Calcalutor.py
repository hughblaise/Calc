First =  float(input("Enter first Number =>"))
Sec = float(input ("Enter Second Number =>"))
Opr = str(input("Enter Operation (+, -, *, /) => "))

if Opr == "+":
    total = First + Sec
    print (total)
elif Opr == "-":
    total = First - Sec
    print (total)
elif Opr == "*":
    total = First * Sec
    print (total)
elif Opr == "/":
    total = First / Sec
    print (total)
else:
    total = str("Please Enter a valid Operation")
    print("invalid operator" )