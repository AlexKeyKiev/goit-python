result = 0

# Ввод первого числа
while True:
    operand_1 = input("\nEnter the first number: ")
    try:
        operand_1 = float(operand_1)
        break
    except ValueError:
        print("\nYou've entered a wrong number.\nPlease try again.")

count_sym = 0

while True:
    # Ввод оператора
    while True:
        symbol = input("\nEnter the symbol: ")
        if symbol in ("+", "-", "*", "/"):
            count_sym += 1
            break
        else:
            print("\nYou've entered a wrong symbol.\nPlease try again.")

    # Ввод следующего числа
    while True:
        operand_2 = input("\nEnter the number: ")
        try:
            operand_2 = float(operand_2)
            break
        except ValueError:
            print("\nYou've entered a wrong number.\nPlease try again.")
    
# Описание условий для оператора 'symbol'
    if symbol == "+" and count_sym == 1:
        result = operand_1 + operand_2
    elif symbol == "-" and count_sym == 1:
        result = operand_1 - operand_2
    elif symbol == "*" and count_sym == 1:
        result = operand_1 * operand_2
    elif symbol == "/" and operand_2 == 0 and count_sym == 1:
        print("\nDivision by zero is PROHIBITED !!!")
        break
    elif symbol == "/" and count_sym == 1:
        result = operand_1 / operand_2

# Описание условий для оператора 'symbol' со второй итерации
    elif symbol == "+" and count_sym > 1:
        result = result + operand_2
    elif symbol == "-" and count_sym > 1:
        result = result - operand_2
    elif symbol == "*" and count_sym > 1:
        result = result * operand_2
    elif symbol == "/" and operand_2 == 0 and count_sym > 1:
        print("\nDivision by zero is PROHIBITED !!!")
        break
    elif symbol == "/" and count_sym > 1:
        result = result / operand_2

# Запрос для прекращения ввода, и вывода результата, или для продолжения ввода
    equal = input("\nTo see the result press '='\nTo continue press any key\n")
    if equal == '=':
        print(result)
        break

    elif equal != '=':
        continue

input("\nThank you! Goodbye.\nEnter any key to exit\n")