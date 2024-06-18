def evaluate_polynomial(polynomial, x):
    terms = polynomial.split('+')
    result = 0
    for term in terms:
        if 'x' in term:
            coefficient, power = term.split('x^')
            result += int(coefficient) * (x ** int(power))
        else:
            result += int(term)
    return result
x, k = map(int, input().split())
polynomial = input()
result = evaluate_polynomial(polynomial, x)
if result == k:
    print(True)
else:
    print(False)
