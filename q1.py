def calculate_sum(x, a, epsilon):
    current_sum = 0.0
    term = 1.0
    k = 1

    while abs(term) > epsilon:
        current_sum += term
        term = (-1) ** k * x ** (6 * k) / (a ** (5 + k))
        k += 1

    return current_sum, k - 1

x_value = 2.0
a_value = 3.0
epsilon_value = 1e-6

result_sum, terms_count = calculate_sum(x_value, a_value, epsilon_value)
print(f"Значення суми: {result_sum}")
print(f"Кількість врахованих доданків: {terms_count}")
