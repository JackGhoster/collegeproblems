import math


a = float(input("Введите a: "))

while a > 1 or a < -1:
    print("С этим числом не получится провести операцию, попробуйте число в пределах от -1 до 1 включая: ")
    a = float(input("Введите a: "))


b = float(input("Введите b: "))

while b > 1 or b < -1:
    print("С этим числом не получится провести операцию, попробуйте число в пределах от -1 до 1 включая: ")
    b = float(input("Введите b: "))


z = float(input("Введите z: "))
x = float(input("Введите x: "))


firstPart = (math.sqrt(math.fabs(x) + math.cos(x)**3 + z**4))
secondPart = (math.log(x) - math.asin((b * x) - a))
finalPart = firstPart/secondPart

print("Ответ: " + "\nПервая часть: "+ str(firstPart) + "\nВторая часть: " + str(secondPart)
        + "\nФинальный ответ: " + str(finalPart))
