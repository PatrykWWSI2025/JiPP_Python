# Zliczanie słów w pliku

# Zadanie:
# Napisz program, który:

# odczyta plik o nazwie story.txt

# zliczy ile słów jest w pliku
# zignoruj puste linie

# wyświetli wynik, np.: "Liczba słów: 42"

# Podpowiedź:
# Użyj read() lub przejdź w pętli przez linie;
# rozdziel tekst używając .split() aby otrzymać słowa.

story = open("story.txt", "r")
zm = len(story.read().split())
print("Liczba słów:", zm, type(zm))
story.close()