def Cubes(num):
    result = []
    for val in range(num): result.append(val**3)
    return result

def cubes(num):
    for i in range(num): yield(i**3)
    return

def CuBeS(num):
    for i in range(num): yield i ** 3

gen = CuBeS(15)


# for val in cubes(10): print(val, end= ' ')
# print()


# for num in Cubes(10):
#     print(num, end= ' ')