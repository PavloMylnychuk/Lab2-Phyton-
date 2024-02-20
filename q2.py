def find_first_term(x, epsilon):
    a0 = x
    an_minus_1 = a0
    n = 1

    while n <= 102:
        an = (2 / 7) * an_minus_1 + (x / (3 * (an_minus_1 ** 5)))
        if abs(an - an_minus_1) < epsilon:
            return an, n
        an_minus_1 = an
        n += 1

    return None, None


x_value = 1.5
epsilon_value = 1e-6

result_term, term_number = find_first_term(x_value, epsilon_value)
if result_term is not None:
    print(f"Перший член послідовності: {result_term}")
    print(f"Номер члена у послідовності: {term_number}")
else:
    print("Умова не виконана для перших 102 членів послідовності.")
