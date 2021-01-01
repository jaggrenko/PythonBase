def fact_n(num):
    for i in range(1, num + 1):
        yield i


fact = 1
n = 70

for el in fact_n(n):
    fact *= el
    print(el)
print(f'{n}! = {fact}')
