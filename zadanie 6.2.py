def oblicz(liczba1, liczba2):
    suma = liczba1 + liczba2
    roznica = liczba1 - liczba2
    return suma, roznica

print(oblicz(10,20))
print(oblicz(-12.5, 10.5))
x, y = oblicz(-10., 20.5)
print(f"Suma - {x} Roznica - {y}")
