distance_array = [[0, 4, 0, 6], [2, 0, 1, 0], [0, 0, 2, 3], [1, 2, 3, 0]]
initial_user_city = 1
initial_cpu_city = 0
destination_city = 3
user_girlfriend_city = 2
number_of_cities = 4

gas_for_cpu = []

for i in range(distance_array[initial_cpu_city]):
    if distance_array[initial_cpu_city][i] != 0:
        if i == destination_city:
            gas_for_cpu.append(distance_array[initial_cpu_city][destination_city])
        else:
            for j in distance_array[i]:
                pass