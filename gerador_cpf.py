from random import randint

num = str(randint(100000000, 999999999))


new_cpf = num
reverse = 10
total = 0


for i in range(19):
    if i > 8:
        i -= 9
    total += int(new_cpf[i]) * reverse

    reverse -= 1
    if reverse < 2:
        reverse = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        new_cpf += str(d)

print(new_cpf)