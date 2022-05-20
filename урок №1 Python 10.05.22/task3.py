number = float(input("ввдеите число: "))

sing = "позитивное" if number > 0 else "негативное"

# abs модуль +- для числа
# len функция для определения количества знаков с учётом +_ длинна строки если используется str
if number == 0:
    print("вариант - 0")
elif len(str(abs(number))) == 1:
    print(f"один знак и {sing}")
elif len(str(abs(number))) == 2:
    print(f"один знак и {sing}")
elif len(str(abs(number))) == 3:
    print(f"один знак и {sing}")
else:
    print(f"многозначительное и {sing}")

# допилить с учётом запятих и знаков после них
