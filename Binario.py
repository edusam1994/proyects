def binario(decimal):
    binario = ""
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario 
        decimal = decimal // 2
    return str(decimal) + binario

number = int(input("Enter the number to convert: "))
print(binario(number))
