import matplotlib.pyplot as plt
def different_prices(n):
    if n <= 0:
        return 0

    price = [0] * (n + 1)
    for i in range(1, n + 1):
        price[i] = price[i - 1] + 1

    df = [0] * (n + 1)
    df[1] = price[1]
    df[2] = price[2] + df[1]
    df[3] = min(df[2], df[1]) + price[3]

    path = [[] for _ in range(n + 1)]
    path[1] = [1]
    path[2] = [1, 2]
    path[3] = [1, 3]

    for i in range(3, n + 1):
        df[i] = min(df[i - 1], df[i - 3]) + price[i]
        if df[i - 1] < df[i - 3]:
            path[i] = path[i - 1] + [i]
        else:
            path[i] = path[i - 3] + [i]
        if i % 3 == 0:
            if df[i // 3] + price[i] < df[i]:
                df[i] = df[i // 3] + price[i]
                path[i] = path[i // 3] + [i]

    prices_optimal = [price[i] for i in path[n]]
    index_optimal = path[n]

    return df[n], prices_optimal, index_optimal

n = int(input('Введите значение n: '))
result, prices, index = different_prices(n)

all_price = [0] * len(prices)

for i in range(len(all_price)):
    all_price[i] = all_price[i - 1] + prices[i]

print(f'Минимальная сумма достичь {n}: {result}')
print('Цены за выбранные ступеньки:', prices)
print('Индексы выбранных ступенек:', index)
print('Полная цена за выбранные ступеньки:', all_price)

x = index
y = all_price

plt.plot(x, y)
plt.scatter(x, y, color='red', marker='o', label='Выбранные ступеньки')
plt.xlabel('Индексы ступенек')
plt.ylabel('Минимальная цена')
plt.title('Оптимальное решение')
plt.legend()
plt.show()
