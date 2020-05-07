base = int(input('Enter base: '))
x = int(input('Enter a number: '))
first_number = x
sis_numbers = []
while x > 0:
    sis_numbers.append(x % base)
    x //= base
if base > 10:
    alph_numbers = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
    for n in range(len(sis_numbers)):
        if sis_numbers[n] in alph_numbers:
            sis_numbers[n] = alph_numbers[sis_numbers[n]]
sis_numbers.reverse()
print(f'Число {first_number} в {base} системе исчисления', end=': ')
for val in sis_numbers:
    print(val, end='')
