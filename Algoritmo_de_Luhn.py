def calculate_luhn(numero):
    numMap = map(int, str(numero))
    num = list(numMap)
    check_digit = 10 - sum(num[-2::-2] + [sum(divmod(d * 2, 10)) for d in num[::-2]]) % 10
    return 0 if check_digit == 10 else check_digit
    

print("Imgrese un numero de 10 digitos")
numero = int(input())

calculate_luhn(numero)