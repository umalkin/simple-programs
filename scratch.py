num = [a for a in range(32)]
print(num)

for a in num:
    if a  == 0:
        print('not')
    elif a % 15 == 0:
        print('fizz buzz')
    elif a % 3 == 0:
        print('fizz')
    elif a % 5 == 0:
        print('buzz')
    else:
        print('not')
