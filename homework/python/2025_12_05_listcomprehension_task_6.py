# 6 #
numbers = [65.0, -1.0, 4.0, 5.6, 5.6, -3.09, 12.9, 4.0, 5.0, -1.0, -0.001, 2.17, 3.0]
threshold = 5.0

output_list = [i for i, number in enumerate(numbers) if number > threshold]

print(output_list)
