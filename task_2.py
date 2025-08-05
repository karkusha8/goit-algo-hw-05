import re
from typing import Callable

# Генератор, який шукає дійсні числа в тексті
def generator_numbers(text: str):
    pattern = r'\s\d+\.\d+\s'
    matches = re.findall(pattern, text)
    for match in matches:
        yield float(match.strip())

# Функція для обчислення суми
def sum_profit(text: str, func: Callable):
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}")