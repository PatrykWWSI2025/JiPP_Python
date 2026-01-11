#### Zapisz dane użytkownika do pliku

#Zadanie:
#Napisz program, który:

#zapyta użytkownika o imię i wiek

#zapisze dane do pliku user.txt w następującym formacie:

#Imię: Jan Wiek: 12


#Podpowiedź:
#Użyj input() aby odczytać dane od użytkownika i write() aby sformatować tekst za pomocą f-stringów.
dane = []
imie = input("Podaj imie:")
wiek = input("Podaj wiek:")
dane.append(f"Imie: {imie}")
dane.append(f"Wiek: {wiek}")
with open("user.txt", "w") as plik:
    for linia in dane:
        plik.write(linia + "\n")