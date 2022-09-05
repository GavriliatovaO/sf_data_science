"""Игра угадай число
Компьютер сам загадывает число и сам его угадывает
"""

import numpy as np

def random_predict(number= np.random.randint(1, 101)) -> int:
    """Компьютер сам загадывает рандомное число и сам его угадывает

    Args:
        number (_type_, optional): Рандомно загаданное число от 1 до 100 включительно. Defaults to np.random.randint(1, 101).

    Returns:
        int: Количество попыток
    """
    predict_number = np.random.randint(1, 101) # загадываем рандомное число, используя генератор рандомных чисел
    count = 0 # счетчик попыток
    low = 1 # минимальное значение рассматриваемого интервала
    high = 100 # максимальное значение рассматриваемого интервала
    
    while True:
        count += 1
        if number not in range(1, 101): # проверка числа, заданного пользователем
            print(f'Число {number} не входит в заданный интервал')
            break # конец игры и выход из цикла
            
        if predict_number > number:
            high = predict_number - 1
            predict_number = (high + low) // 2
        elif predict_number < number:
            low = predict_number + 1
            predict_number = (high + low) // 2
        else:
            #print(f'Компьютер угадал загаданное число {number} за {count} попыток.')
            #break # конец игры и выход из цикла
            return count

#print(random_predict())


def score_game(random_predict) -> int:
    """ Определяет среднее количество попыток из 1000 раз угадывания числа нашего алгоритма
    Args:
        random_predict ([type]): Функция загадывания и угадывания рандомного числа от 1 до 100
    Returns:
        int: Среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадаваем 1000 раз список чисел от 1 до 100
    
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")


if __name__ == "__main__":
    # RUN
    score_game(random_predict)