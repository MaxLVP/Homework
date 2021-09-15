number = int(input('Введите число'))
divisors = []
for i in range(1, number//2+1):
    if number % i == 0:
        divisors.append(i)
divisors.append(number)
print(divisors)
