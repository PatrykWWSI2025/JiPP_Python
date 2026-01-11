#### Zapisz listę do pliku – jedno słowo w linii

# Zadanie:
# Masz listę:

# words = ["apple", "banana", "cherry"]


# Napisz program, który zapisze tę listę do pliku o nazwie fruits.txt tak, aby każde słowo było w osobnej linii.

# Podpowiedź:
# Przejdź w pętli przez listę i użyj file.write() z "\n". Lub użyj "\n".join(list).

words = ["apple","banana","cherry"]
with open("fruits.txt", "w") as f:
    for word in words:
        f.write(word + "\n")