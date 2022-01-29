import numpy as np
from functools import reduce


def standard_deviation(data):
    return (sum(list(map(lambda x: (x - mean) ** 2, data))) / (n - 1)) ** 0.5


def offset_standard_deviation(data):
    return standard_deviation(data) * ((n - 1) / n) ** 0.5


def lose(data):  # remove misses
    n = len(data)
    mean = np.mean(data)
    sigma = standard_deviation(data)
    x_max = reduce(lambda x1, x2: x1 if (abs(x1 - mean) > abs(x2 - mean)) else x2, data)

    data_2 = data.copy()
    data_2.remove(x_max)
    mean_x_max = np.mean(data_2)

    if abs(x_max - mean_x_max) <= 3 * sigma:
        return data
    else:
        print(f"{x_max} is miss, deleting {x_max}...")
        data.remove(x_max)
        return lose(data)


def composite_criterion(data):
    n = len(data)
    mean = np.mean(data)
    sigma_offset = offset_standard_deviation(data)
    sigma = standard_deviation(data)

    d = sum(list(map(lambda x: abs(x - mean), data))) / (n * sigma_offset)
    print("d: ", d)

    d_min, d_max = map(float, input("Enter d_min and d_max(look appendix table 5): ").split())

    if d_min < d < d_max:
        z, m_table = map(float, input("Enter table values \"z\" and \"m\"(look appendix table 6: ").split())
        m = sum(list(map(lambda x: 1 if abs(mean - x) > z * sigma else 0, data)))

        if m < m_table:
            return True
        else:
            return False
    else:
        return False


def main():
    print("1 - Miss detection")
    print("2 - Composite criterion (definition of the distribution law)")
    print("3 - Multiple measurements (includes removal of misses))")
    print("4 - Just output mean, standard deviation, offset standard deviation, mean standard deviation")
    mode = int(input("Choose mod: "))
    data = list(map(float, input("Enter the data (separated by a space):\n").split()))

    if mode == 1:  # misses
        print("data before:", *data)
        print("Misses:")
        print("data after:", *lose(data))

    if mode == 2:  # composite criterion
        if len(data) < 15:
            print("Belonging to the normal distribution law isn't checked")
        elif composite_criterion(data):
            print("The data doesn't belong to the normal distribution law")
        else:
            print("The data belong to the normal distribution law")

    if mode == 3:  # multiple measurements
        print("data before:", *data)
        data = lose(data)
        print("Misses:")
        print("data after:", data)

        if composite_criterion(data):
            print("The data doesn't belong to the normal distribution law")
        else:
            print("The data belong to the normal distribution law")

        n = len(data)
        mean = np.mean(data)

        sigma = standard_deviation(data)
        sigma_mean = sigma / n ** 0.5
        print("data:", *data)
        print("n:", n)
        print("mean:", mean)
        print("sigma:", sigma)
        print("sigma_mean:", sigma_mean)

    if mode == 4:
        n = len(data)  # count of measurements
        mean = np.mean(data)
        sigma = standard_deviation(data)
        sigma_offset = offset_standard_deviation(data)
        # mean standard deviation = sigma/sqrt(n)
        sigma_mean = sigma / n ** 0.5

        print("data:", *data)
        print("n:", n)
        print("mean:", mean)
        print("sigma:", sigma)
        print("sigma_offset:", sigma_offset)
        print("sigma_mean:", sigma_mean)


if __name__ == "__main__":
    main()
