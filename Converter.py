# -*- coding: utf-8 -*-

Currencies = {"USD": 1.0, "RUB": 71.75, "JPY": 109.39, "EUR": 0.9}


def conveyor(summ: float, current: str, received: str) -> float:
    heft = summ / Currencies[current]
    return round(heft * Currencies[received], 2)


print(conveyor(100, "RUB", "USD"))