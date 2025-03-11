def verificar_numero():
    number = int(input('Insert a number: '))
    resultado = []

    if number > 0:
        resultado.append(f'The number {number} is positive.')
    elif number < 0:
        resultado.append(f'The number {number} is negative.')
    else:
        resultado.append(f'The number {number} is zero.')

    if number % 2 == 0:
        resultado.append(f'The number {number} is even.')
    else:
        resultado.append(f'The number {number} is odd.')

    if number % 3 == 0:
        resultado.append(f'The number {number} is divisible by 3.')
    else:
        resultado.append(f'The number {number} is not divisible by 3.')

    print(' '.join(resultado))

verificar_numero()