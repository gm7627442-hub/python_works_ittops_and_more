# 8 #
input_list = ["лом", "********", "барбарис", "", [3, 4, 6], "ещё бы", range(7, 11), "+++++"]

output_list = [[item for item in iterable] for iterable in input_list]

print(output_list)
