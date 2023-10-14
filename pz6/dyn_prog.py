def count_ways(n):
    if n<=1:
        return 1
    d=[0]*(n+1)
    d[1]=1
    for i in range(2,n+1):
        d[i]+=d[i-1]
        d[i]+=d[i-3]
        if i%3==0:
            d[i]+=d[i//3]
    return d[n]
n = int(input(('Введите значение n: ')))
result = count_ways(n)
print(f'Количество способов достичь {n} из точки 1: {result}')
