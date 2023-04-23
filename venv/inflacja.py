"""Stwórz program, który na podstawie

tabeli inflacji wartości
oprocentowania kredytu,
kwoty początkowej kredytu
stałej wartości raty
wyliczy wartość zadłużenia w każdym miesiącu przez 2 nadchodzące lata.

Niech program wydrukuje dla każdego miesiąca następującą linię:
Twoja pozostała kwota kredytu to X, to Y mniej niż w poprzednim miesiącu.

Napisz program tak, by wysokość początkowego kredytu, oprocentowanie kredytu (ponad inflację)
i kwota raty były pobierane ze standardowego wejścia (terminal).

"""
username = input("Witaj! Jest to aplikacja obliczająca wartość zadłużenia kredytowego." \
                "Podaj proszę swoje imię by rozpocząć:   ")
print(f"Drogi/a {name}! \n Podaj proszę wysokość początkową kredytu, oprocentowanie kredytu oraz kwotę raty.".format(name=username))


start_amount = int(input('Teraz podaj wartość kredytu:  '))
loan_interest = int(input('Następnie podaj wartość oprocentowania:  '))
monthly_payment = int(input('Teraz podaj kwotę raty miesięcznej, na tej podstawię \n aplikacja obliczy pozostałą sumę do spłaty zadłużenia:  '))
inflation
amount = start_amount - (monthly_payment * loan_interest * inflation)
message = ("Twoja pozostała kwota kredytu to {amount}, to {less} mniej niż w poprzednim miesiącu.")

print




