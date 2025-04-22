import numpy as np  # type: ignore

temp = []
avg_list = []


def moving_average(data_list, window_size):
    # print(data_list, window_size)

    for i in range(len(data_list) - window_size + 1):
        window = data_list[i:i+window_size]
        window_average = sum(window) / window_size
        avg_list.append(window_average)

    # print(avg_list)
    return avg_list


data = np.random.randint(10, size=5)
window_size = 3

moving_average(data, window_size)
