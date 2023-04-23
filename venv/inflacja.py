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
username = input("Witaj! Jest to aplikacja obliczająca wartość zadłużenia kredytowego. " \
                 "Podaj proszę swoje imię by rozpocząć:   ")
print(f"Drogi/a {username}! \n Podaj proszę wysokość początkową kredytu, oprocentowanie kredytu oraz kwotę raty.")

message = ("{month} \n Twoja pozostała kwota kredytu w miesiącu {month} to {amount}, \n to {less} mniej niż w poprzednim miesiącu.")

start_amount = int(input('Teraz podaj wartość kredytu:  '))
loan_interest = float(input('Następnie podaj wartość oprocentowania:  '))
monthly_payment = float(input('Teraz podaj kwotę raty miesięcznej, \n na tej podstawię '\
'aplikacja obliczy pozostałą sumę do spłaty zadłużenia:  '))

# Styczeń
month = "styczeń"
inflation = 0.5
#amount logika
# amount -> wysokość pożyczki minus (m-czna rata  + oprocentowanie )+ inflacja
amount = start_amount - (monthly_payment + (monthly_payment * loan_interest) * inflation)
#less logika
#less -> początkowa kwota amount
less = start_amount - amount

print(message.format(month=month, amount=amount, less=less))








