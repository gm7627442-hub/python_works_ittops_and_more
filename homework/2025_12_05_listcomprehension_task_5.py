# 5 #
numbers = [65.0, -1.0, 4.0, 5.6, 5.6, -3.09, 12.9, 4.0, 5.0, -1.0, -0.001, 2.17, 3.0]

output_list = [-number if number != 0 else number for number in numbers]

print(output_list)
