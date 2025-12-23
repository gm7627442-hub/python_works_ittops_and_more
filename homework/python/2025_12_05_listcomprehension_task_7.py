# 7 #
input_list = ["жа", "ло", "ко", "за", "ти", "на", "ра", "на", "жа", "ба", "ко", "жа", "ль"]

output_list = [input_list[2 * i] + input_list[2 * i + 1] for i in range(len(input_list) // 2)]

print(output_list)
