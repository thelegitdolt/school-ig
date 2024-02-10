import numpy as np

nd_arr = np.array([1, 2, 3, 4, 5])

print(nd_arr.__repr__())
print(nd_arr)

nd_arr3D = np.array([
    [
        [1, 2, 3], [3, 4, 6], [7, 8, 3.1415926]
    ],
    [
        [1, 2, 4], [8, 16, 32], [64, 128, 256]
    ],
    [
        [1, 1, 2], [3, 5, 8], [13, 21, 34]
    ]
])



# dimensions of the array
print(nd_arr.shape)


thing = np.arange(1, 20)
print(thing)

logged_thing = np.log(thing)
print(logged_thing)

list_with_0_to_20_11 = np.linspace(0, 20, 11)
geom_space = np.geomspace(1, 10000, 5)
two_power_21 = 2 << 21

# arrays can have many dimensions! tables! and stuff!


