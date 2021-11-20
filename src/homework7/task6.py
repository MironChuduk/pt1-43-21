"""
Написать программу которая находит ближайшую
степень двойки к введенному числу. 10(8), 20(16), 1(1), 13(16)
"""


def search(num):
    power = 0
    index = 0
    while abs((2 ** index) - num) > abs((2 ** (index + 1)) - num):
        index += 1
        power = 2 ** index
    return power


my_num = int(input("Введите число: "))
print(f"Ближайшая к числу степень двойки: {search(my_num)}")
