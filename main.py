import numpy as np
from functools import reduce


def lose(data):  # удаляем промахи
    n = len(data)
    mean = np.mean(data)
    sigma = (sum(list(map(lambda x: (x - mean)**2, data))) / (n - 1))**0.5
    x_max = reduce(lambda x1, x2: x1 if (abs(x1 - mean) > abs(x2 - mean)) else x2, data)

    data_2 = data.copy()
    data_2.remove(x_max)
    mean_x_max = np.mean(data_2)

    if abs(x_max - mean_x_max) <= 3 * sigma:
        return data
    else:
        print(f"{x_max} is lose, deleting {x_max}...")
        data.remove(x_max)
        return lose(data)


def composite_crit(data):  # составной критерий
    n = len(data)
    mean = np.mean(data)
    sigma_sm = (sum(list(map(lambda x: (x - mean)**2, data))) / n)**0.5
    sigma = (sum(list(map(lambda x: (x - mean)**2, data))) / (n-1))**0.5

    d = sum(list(map(lambda x: abs(x - mean), data))) / (n * sigma_sm)
    print("d: ", d)

    d_min, d_max = map(int, input("Enter d_min and d_max: ").split())

    if d_min < d < d_max:
        z, m_table = map(int, input("Enter table values \"z\" and \"m\":").split())
        m = sum(list(map(lambda x: 1 if abs(mean - x) > z * sigma else 0, data)))

        if m < m_table:
            return True
        else:
            return False
    else:
        return False



def main():
    print("1 - Выявление промахов")
    print("2 - составной критерий (определиение закона распределения)")
    print("3 - Многократные измерения (входит удаление промахов)")
    print("4 - Просто вывести средн.ариф., СКО, СКО смещ., СКО ср.ариф.")
    mode = int(input("Choose mod: "))
    data = list(map(int, input("Введите данные(через пробел):\n").split()))

    n = len(data)
    mean = np.mean(data)

    print("n:", n)
    print("mean:", mean)

    if mode == 1:  # промахи
        print("data before:", *data)
        print("Loses:")
        print("data after:", *lose(data))

    if mode == 2:  # составной критерий
        if len(data) < 15:
            print("Belonging to the normal distribution law isn't checked")
        if composite_crit(data):
            print("The data doesn't belong to the normal distribution law")
        else:
            print("The data belong to the normal distribution law")

    if mode == 3:  # многократные измерения
        print("Loses:")
        data = lose(data)
        n = len(data)
        mean = np.mean(data)

        # составной критерий
        d = composite_crit(data)

        sigma = (sum(list(map(lambda x: (x - mean)**2, data))) / (n-1))**0.5
        sigma_mean = sigma / n**0.5
        print("data:", *data)
        print("n:", n)
        print("mean:", mean)
        print("d:", d)
        print("sigma:", sigma)
        print("sigma_mean:", sigma_mean)

        return

    if mode == 4:
        n = len(data)  # количество измерений
        mean = np.mean(data)  # среднее арифметическое значение
        # среднее квадратичное отклонение (СКО)
        sigma = (sum(list(map(lambda x : (x - mean)**2, data))) / (n-1))**0.5
        # смещ. СКО - для составного критерия (определиение закона распределения)
        sigma_sm = (sum(list(map(lambda x : (x - mean)**2, data))) / n)**0.5
        # СКО среднего арифметического = СКО/sqrt(n) - для оценки многократных ихмерений
        sigma_mean = sigma / n**0.5

        print("data:", *data)
        print("sigma:", sigma)
        print("sigma_sm:", sigma_sm)
        print("sigma_mean:", sigma_mean)

        return


if __name__ == "__main__":
    main()