# task №1

lend = input("Скільки складаж шлях від пункту А до пункту Б: ")
velo = input("З якою швидкістю Ви будете рухатись?: ")
hours = int(lend)/int(velo)
hour = round(hours)
time = hours * 3600
minutes = (time // 60)%60
second = time%60
print("Ваш шлях складає", hour, "годин", int(minutes), "хвилин", int(second),"секунд")

# task №2

age = 25
name = "John"
print("My name is " + str(name) + " and I am " + str(age))