if 'rrr' in 'fff rrr yyy jjj':
    z = 3+56
    print('z')
    print('ggg')
else:
    print('hhh')

name = "Jhon"
if name == "Fred":
    print("Oh, hello Fred")

elif name == "Jhon":
    print("Whazap Jhon")

elif name == "Sara":
    print("Hi, Sara")
else:
    print("Hi evryone")

    # ошибки не учитыватся при воспроизведении в случае совпадения одного из значения
if "a" in "bar":
    print("foo")
elif 1/0:
    print("This won`t happen")
elif var:
    print("This won`t either")

    #  однорядные операторы if ( не рекомендуется в связи не читабельностью [PEP-8])
if "f" in "foo": print("1"); print("2"); print("3"); print("4");
elif "d" in "ddd:": print("6"); print("5")
else: print("in else")

debugging = True


if debugging: print("We testing code")

    #условные выражения тренарный оператор

age = 29
s = "small" if age < 30 else "grandpa=)"


x= y = 40
z= 1 + x if x > y else y + 2




