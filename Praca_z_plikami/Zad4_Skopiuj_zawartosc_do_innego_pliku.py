#### Skopiuj zawartość pliku do innego pliku
# Zadanie:
# Napisz program, który:

# odczyta zawartość pliku numbers.txt

# skopiuje wszystko do nowego pliku o nazwie copy.txt

# Podpowiedź:
# Użyj read() aby pobrać całą zawartość na raz lub kopiuj linię po linii.

with open("numbers.txt", "r") as plik:
    zawartosc = plik.read()

with open("copy.txt", "w") as cpy:
    cpy.write(zawartosc)