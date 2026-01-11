# Utwórz słownik filmów. Niech  kluczem będzie nazwa filmu, a parą wartości dwie liczby: kryteria wiekowe oraz liczba dostępnych biletów

movies = {"Harry Potter":[12,5], "Awatar":[12,2], "Batman":[18,3], "World of warcraft":[13,4]}

# Utwórz pętlę, która będzie działać w nieskończoność

while True:
    
    # Pobierz tytuł filmu od użytkownika, usuń spacje z początku i końca a następnie zamień frazę na format tytułowy (pierwsza litera każdego słowa jest wielka)
    film = input("Wprowadź tytuł filmu lub wpisz exit aby zakończyć): ").strip().title()
    
    # Stwórz instrukcję warunkową if. Jeśli wybrany film jest odostępny w słowniku, kontynuuj
    # Pozwól użytkownikowi zakończyć pętlę wpisując "exit"
    if film.lower() == 'exit':
        print("Zakończono rezerwację")
        break

    # Sprawdź, czy film jest dostępny
    if film not in movies:
        print("Film niedostępny.")
        continue

    # Zapytaj użytkownika o wiek
    try:
        wiek = int(input("Wprowadź swój wiek: "))
    except ValueError:
        print("Podano nieprawidłowy wiek.")
        continue

    # Jeśli użytkownik znajduje się w grupie docelowej, sprawdź dostępność miejsc
    # Jeśli liczba dostępnych miejsc jest wartością dodatnią, zmiejsz pulę dostępnych miejsc o 1
    if wiek >= movies[film][0]:
        if movies[film][1] > 0:
            movies[film][1] -= 1
            print(f"Kupiłeś bilet na {film}. Pozostało {movies[film][1]} miejsc.")
        else:
            print("Brak dostępnych biletów.")
    else:
        print("Nie spełniasz kryteriów wiekowych.")