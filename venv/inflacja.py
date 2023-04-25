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

# Styczeń 0.02%
month = "styczeń"
inflation = float(0.02)
#amount logika
# amount -> wysokość pożyczki minus (m-czna rata  * oprocentowanie )x inflacja
amount = start_amount - (monthly_payment + (monthly_payment * loan_interest) * inflation)
#less logika
#less -> początkowa kwota amount
less = float(start_amount - amount)

print(message.format(month=month, amount=amount, less=less))

#Luty 0%
month = "luty"
inflation = float(0.00)
#amount1 logika
# amount1 -> amount minus (m-czna rata  + oprocentowanie )x inflacja
amount1 = amount - (monthly_payment + (monthly_payment * loan_interest) * inflation)
#less logika
#less -> wynik styczniowy (amount) - amount 1
less1 = float(start_amount - amount1)

print(message.format(month=month, amount=amount1, less=less1))

#Marzec 2 %
month = "marzec"
inflation = float(0.02)
#amount2 logika
# amount2 -> amount1 minus (m-czna rata  + oprocentowanie )x inflacja
amount2 = float(amount1 - (monthly_payment + (inflation * loan_interest)))
#less logika
#less -> początkowa kwota amount
less2 = float(amount2 - less1)

print(message.format(month=month, amount=amount2, less=less2))

#kwiecień 1%
month = "kwiecień"
inflation = float(0.01)
#amount2 logika
# amount2 -> amount1 minus (m-czna rata  + oprocentowanie )x inflacja
amount3 = float(amount2 - (monthly_payment + (inflation * loan_interest)))
#less logika
#less -> początkowa kwota amount
less3 = float(amount2 - amount3)

print(message.format(month=month, amount=amount3, less=less3))

#maj 2 %
month = "maj"
inflation = float(0.02)
#amount2 logika
# amount2 -> amount1 minus (m-czna rata  + oprocentowanie )x inflacja
amount4 = float(amount3 - (monthly_payment + (inflation * loan_interest)))
#less logika
#less -> początkowa kwota amount
less4 = float(amount3 - amount4)

print(message.format(month=month, amount=amount4, less=less4))

#czerwiec 2%

month = "czerwiec"
inflation = float(0.02)
#amount2 logika
# amount2 -> amount1 minus (m-czna rata  + oprocentowanie )x inflacja
amount5 = float(amount4 - (monthly_payment + (inflation * loan_interest)))
#less logika
#less -> początkowa kwota amount
less5 = float(amount4 - amount5)

print(message.format(month=month, amount=amount5, less=less5))