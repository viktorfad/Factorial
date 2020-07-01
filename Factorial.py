import math

def get_zeros(n):
    try:
        k = 0
        for i in str(math.factorial(n))[::-1]:
            if i == '0':
                k += 1
            else :
                return k
    except ValueError as e:
        print('Ошибка! \nЧисло, факториал которого необходимо вычислить, должно быть неотрицательным и интегральным! \nВы передали: n={}'.format(n))
        return
