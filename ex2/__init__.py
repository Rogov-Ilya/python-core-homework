import time

from ex2 import fetcher

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """

    def wrapper(func):
        # put your code here
        def leadTime(*args, **keywargs):
            totalTime = 0
            for n in range(num):
                start = time.time()
                func(*args, **keywargs)
                end = time.time()
                result = end - start
                print(f'Время выполнения прогона: {result}')
                totalTime += result
            print(f'Среднее время всех прогонов: {totalTime / num}')

        return leadTime

    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
