

my_list = [3,1,5,7,8,1,5,2]
print(my_list)
print(type(my_list))

print(my_list[0])
print(my_list[3])
print(my_list[-1])

print(len(my_list))

my_other_list = ['hi' , True, 1, 1.3,[10, 11]]
print(my_other_list[4][0])

for i in range(len(my_other_list)):
    print(i,   ' ->  ', my_other_list[i])

for i in my_other_list:
    print(i)

    numbers = [3, 1, 6, 4, 8, 9, 5, 2]
    print(numbers)
    numbers.append(15) # inserta algo al final
    numbers.append(53)
    print(numbers)
    numbers.pop() # estrae al ultimo valor
    print(numbers)
    numbers.reverse() # invierte los elementos
    print(numbers)
    numbers.sort() # ordena los elementos
    print(numbers)
    numbers.clear()
    print(numbers)
