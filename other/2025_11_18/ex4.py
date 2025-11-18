import copy
import pprint  # Для красивого вывода


heavy_data = [
    1,
    2,
    [
        "dsf",
        [1, 2, 3],
        "dfdsh",
        []
    ],
    7,
    [
        [3, 2, 1],
        [3, 2, 4],
    ]
]


# Вот это создаст полную (глубокую) копию,
# то есть все вложенные объекты будут
# тоже скопированы
heavy_data_copy = copy.deepcopy(heavy_data)


print(heavy_data_copy)
pprint.pprint(heavy_data_copy, indent=4, depth=5, width=20)
