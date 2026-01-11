# Prosty program kalkulatora

# Utwórz funkcję dodawania dwóch liczb
def add(a, b):     
   return a + b

# Utwórz funkcję odejmowania dwóch liczb
def subtract(a, b):
    return a - b

# Utwórz funkcję mnożenia dwóch liczb
def multiply(a, b):
    return a * b

# Utwórz funkcję dzielenia dwóch liczb
def divide(a, b):
    if b == 0:
        return "nie można dzielić przez zero!"
    return a / b

# Wyświetl listę operacji

print ("Please select the operation.")    
print ("a. Add")    
print ("b. Subtract")    
print ("c. Multiply")    
print ("d. Divide")   

# Pozwól użytkownikowi wybrać żądane działanie na podstawie wyświetlonej listy poleceń
    
op = input("Please enter choice (a/ b/ c/ d): ")   
if op not in ["a", "b", "c", "d"]:
    print("Niepoprawna operacja!")
else:
     
# Przechwyć 2 liczby wprowadzone przez użytkownika i przekonwertuj je na format liczby całkowitych

    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))



# Logika do wykonywania określonej operacji za pomocą instrukcji IF -ELIF -ELSE.

    if op == "a":
        wynik = add(a,b)
    elif op == "b":
        wynik = subtract(a,b)
    elif op == "c":
        wynik = multiply(a,b)
    elif op == "d":
        wynik = divide(a,b)
    else:
        wynik = "niepoprawy wybór operacji!"


# Jeśli użytkownik wybierze operację, która nie jest dostępna, wyświetl komunikat o błędzie


print("Wynik: ", wynik)