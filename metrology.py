from functools import reduce


def average(data):
    return sum(data) / len(data)


def standard_deviation(data):
    n = len(data)
    mean = average(data)
    return (sum(list(map(lambda x: (x - mean) ** 2, data))) / (n - 1)) ** 0.5


def offset_standard_deviation(data):
    n = len(data)
    return standard_deviation(data) * ((n - 1) / n) ** 0.5


def lose(data):  # remove misses
    mean = average(data)
    sigma = standard_deviation(data)
    x_max = reduce(lambda x1, x2: x1 if (abs(x1 - mean) > abs(x2 - mean)) else x2, data)

    data_2 = data.copy()
    data_2.remove(x_max)
    mean_x_max = average(data_2)

    if abs(x_max - mean_x_max) <= 3 * sigma:
        return data
    else:
        print(f"{x_max} is miss, deleting {x_max}...")
        data.remove(x_max)
        return lose(data)


def composite_criterion(data):
    n = len(data)
    mean = average(data)
    sigma_offset = offset_standard_deviation(data)
    sigma = standard_deviation(data)

    d = sum(list(map(lambda x: abs(x - mean), data))) / (n * sigma_offset)
    print("d: ", d)

    d_min, d_max = map(float, input(f"Enter the d_min and d_max for n = {n} (look appendix table 5): ").split())

    if d_min < d < d_max:
        z, m_table = map(float, input(f"Enter the table values \"z\" and \"m\" for n = {n} (look appendix table 6): ").split())
        m = sum(list(map(lambda x: 1 if abs(mean - x) > z * sigma else 0, data)))

        if m < m_table:
            return True
        else:
            return False
    else:
        return False


def main():
    mode = 0
    while mode < 5:
        print("1 - Miss detection")
        print("2 - Composite criterion (definition of the distribution law)")
        print("3 - Multiple measurements (includes removal of misses))")
        print("4 - Output mean, standard deviation, offset standard deviation, mean standard deviation")
        print("5 - Exit")
        mode = int(input("Choose mod: "))
        if mode > 4:
            break
        data = list(map(float, input("Enter the data(separated by a space):\n").split()))

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
            print("Misses:")
            data = lose(data)
            print("data after:", *data)

            if composite_criterion(data):
                print("The data doesn't belong to the normal distribution law")
            else:
                print("The data belong to the normal distribution law")

            n = len(data)
            mean = average(data)

            sigma = standard_deviation(data)
            sigma_mean = sigma / n ** 0.5

            print("n:", n)
            print("mean:", mean)
            print("standard deviation:", sigma)
            print("mean standard deviation:", sigma_mean)

        if mode == 4:
            n = len(data)  # count of measurements
            mean = average(data)
            sigma = standard_deviation(data)
            sigma_offset = offset_standard_deviation(data)
            # mean standard deviation = sigma/sqrt(n)
            sigma_mean = sigma / n ** 0.5

            print("n:", n)
            print("mean:", mean)
            print("standard deviation:", sigma)
            print("offset standard deviation:", sigma_offset)
            print("mean standard deviation:", sigma_mean)


if __name__ == "__main__":
    main()
