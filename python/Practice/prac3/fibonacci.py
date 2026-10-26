def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end = " ")
        a,b = b, a+b

n_terms = 10
print(f"fibo suq up to {n_terms} terms:")
fibo(n_terms)
