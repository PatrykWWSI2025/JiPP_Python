# Odczytaj liczby z pliku i oblicz ich sumę
# Zadanie:
# Masz plik numbers.txt z jedną liczbą w linii, na przykład:

# 10
# 3
# 7
# -2


# Napisz program, który:

# odczyta liczby z pliku

# przekształci je na int

# obliczy ich sumę 
# -2


# Napisz program, który:

# odczyta liczby z pliku

# przekształci je na int

# obliczy ich sumę
# wyświetli wynik

# Podpowiedź:
# Użyj int(line.strip()) i przechowuj bieżącą sumę w zmiennej.

liczby = open("numbers.txt", "r")
wynik = 0
for line in liczby:
    wynik += int(line.strip())
print("Suma liczb:", wynik, type(wynik))
liczby.close()