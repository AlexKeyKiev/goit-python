# Ввод первого числа
while True:
    operand_1 = input("\nEnter the number: ")
    try:
        operand_1 = float(operand_1)
        break
    except ValueError:
        print("\nYou've entered a wrong number.\nPlease try again.")

while True:
# Ввод оператора
    while True:
        symbol = input("\nEnter the symbol: ")
        if symbol in ("+", "-", "*", "/"):
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

    input("\nTo see the result press '='\n")

# Описание условий для оператора 'symbol'
    if symbol == "+":
        result = operand_1 + operand_2
        print(result)
        break
    elif symbol == "-":
        result = operand_1 - operand_2
        print(result)
        break
    elif symbol == "*":
        result = operand_1 * operand_2
        print(result)
        break
    elif symbol == "/" and operand_2 == 0 :
        print("\nDivision by zero is prohibited!")
        break
    elif symbol == "/":
        result = operand_1 / operand_2
        print(result)
        break

# Заглушка для того, чтоб окно терминала не сразу закрывалось
input("\nThank you! Goodbye.\nEnter any key to exit\n")
