def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    return b**2 - 4*a*c

def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    D = discriminant(a, b, c)
    if D > 0:
        return((-b+D**0.5)/(2*a), (-b-D**0.5)/(2*a))
    elif D == 0:
        return ((-b)/(2*a))
    else:
        return ("корней нет")

if __name__ == '__main__':
    print(solution(1, 8, 15))
    print(solution(1, -13, 12))
    print(solution(-4, 28, -49))
    print(solution(1, 1, 1))