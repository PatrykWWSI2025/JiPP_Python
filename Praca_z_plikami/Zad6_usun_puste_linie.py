#### Usuń puste linie z pliku

#Zadanie:
#Masz plik raw.txt zawierający puste i niepuste linie.

#Napisz program, który:

#odczyta wszystkie linie z raw.txt

#usunie puste linie (linie puste lub zawierające tylko białe znaki)

#zapisze tylko niepuste linie do nowego pliku o nazwie clean.txt

#Podpowiedź:
#Użyj .strip() aby sprawdzić, czy linia jest pusta; jeśli line.strip() != "", zachowaj ją.

with open("raw.txt", "r") as plik:
    with open("clean.txt", "w") as clean:
        for line in plik:
            if line.strip() != "":
                clean.write(line)