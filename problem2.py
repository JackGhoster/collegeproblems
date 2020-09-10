import math 


def zadachka():
    n = float(input("Введите значение n: "))
    U = math.sqrt(n/(n+1))
    t = math.acos(U)/2*math.pi

    return print("Значение напряжения = " + str(U) + "\nВремя = " + str(t))


if __name__ == "__main__":
    while True:
        zadachka()
        continue