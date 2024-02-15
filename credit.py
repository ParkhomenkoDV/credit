import math

S = float(input('Кредит (руб): '))
q = float(input('Годовая процентная ставка (%): '))
q = q / 12 / 100  # перевод в месячные доли
d = float(input('Ежемесячные выплаты (руб): '))

if S * (1 + q) - S > d:
    print('\nИпотека не выплатится НИКОГДА!')
    input()
    exit()

m = 0
while (S >= 0) and (S != math.inf) and (m <= 40 * 12):
    print()
    m += 1
    print('Год', (m // 12) + 1, 'Месяц', m)
    print('Долг (руб):', round(S, 3))
    S = S * (1 + q)
    print('Долг после начисления процентов (руб):', round(S, 3))
    S -= d
    print('Долг после выплат (руб):', round(S, 3))

input()
