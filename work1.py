# print('a'*1980)
print('ш'*10)
print('ш'*10)
print('ш'*10)
print('ш'*10)
print('ш'*10)
print('ш'*10)
print('ш'*10)
print('ш'*10)
print('ш'*10)
print('ш'*10)

print("\n".join('ш ' * 10  for i in range(10)))
x = 0
a = '.'
b = 'o'
while x < 5:
    print((a+b)*10)
    print((b+a)*10)
    x += 1

for i in range(3):
    print((('*'*3 + '\n')*3 + ('о'*3 + '\n')*3)*3 +'\n' + 'o'*3 + '*'*3 + 'o'*3)
   
        


