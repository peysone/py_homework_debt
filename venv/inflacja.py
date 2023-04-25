import os

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

print()
print("\u001b[31;1m" + "ROK 2022")
print("\u001b[33;1m")

#styczeń 0.02%
month = "styczeń"
inflation = float(0.02)
#amount logika
# amount -> wysokość pożyczki minus (m-czna rata  * (m-czna rata * oprocentowanie )x inflacja)
amount = start_amount - (monthly_payment + (monthly_payment * loan_interest) * inflation)
#less logika
#less -> początkowa kwota - amount
less = float(start_amount - amount)

print(message.format(month=month, amount=amount, less=less))

#Luty 0%
month = "luty"
inflation = float(0.00)
#amount1 logika
# amount1 -> amount minus (m-czna rata  * (m-czna rata * oprocentowanie )x inflacja)
amount1 = amount - (monthly_payment + (monthly_payment * loan_interest) * inflation)

less1 = float(start_amount - amount1)

print(message.format(month=month, amount=amount1, less=less1))

#Marzec 2 %
month = "marzec"
inflation = float(0.02)
amount2 = amount1 - (monthly_payment + (monthly_payment * loan_interest) * inflation)

less2 = float(start_amount - amount2)

print(message.format(month=month, amount=amount2, less=less2))

#kwiecień 1%
month = "kwiecień"
inflation = float(0.01)
amount3 = amount2 - (monthly_payment + (monthly_payment * loan_interest) * inflation)

less3 = float(start_amount - amount3)

print(message.format(month=month, amount=amount3, less=less3))

#maj 2 %
month = "maj"
inflation = float(0.02)
amount4 = amount3 - (monthly_payment + (monthly_payment * loan_interest) * inflation)

less4 = float(start_amount - amount4)

print(message.format(month=month, amount=amount4, less=less4))

#czerwiec 2%

month = "czerwiec"
inflation = float(0.02)
amount5 = amount4 - (monthly_payment + (monthly_payment * loan_interest) * inflation)

less5 = float(start_amount - amount5)

print(message.format(month=month, amount=amount5, less=less5))

# lipiec 2%

month = "lipiec"
inflation = float(0.02)
amount6 = amount5 - (monthly_payment + (monthly_payment * loan_interest) * inflation)

less6 = float(start_amount - amount6)

print(message.format(month=month, amount=amount6, less=less6))

# sierpień 2%
month = "sierpień"
inflation = float(0.02)
amount7 = amount6 - (monthly_payment + (monthly_payment * loan_interest) * inflation)

less7 = float(start_amount - amount7)

print(message.format(month=month, amount=amount7, less=less7))

# wrzesień 2%

month = "wrzesień"
inflation = float(0.02)
amount8 = amount7 - (monthly_payment + (monthly_payment * loan_interest) * inflation)

less8 = float(start_amount - amount8)

print(message.format(month=month, amount=amount8, less=less8))

# październik 1%

month = "październik"
inflation = float(0.01)
amount9 = amount8 - (monthly_payment + (monthly_payment * loan_interest) * inflation)

less9 = float(start_amount - amount9)

print(message.format(month=month, amount=amount9, less=less9))

# listopad 2%

month = "listopad"
inflation = float(0.02)
amount10 = amount9 - (monthly_payment + (monthly_payment * loan_interest) * inflation)

less10 = float(start_amount - amount10)

print(message.format(month=month, amount=amount10, less=less10))

# grudzień 0%

month = "grudzień"
inflation = float(0.00)
amount11 = amount10 - (monthly_payment + (monthly_payment * loan_interest) * inflation)

less11 = float(start_amount - amount11)

print(message.format(month=month, amount=amount11, less=less11))
print()
print ("\u001b[31;1m" + "ROK 2023")
print("\u001b[33;1m")

# Styczeń 0.02%
month = "styczeń"
inflation = float(0.02)
#amount logika
# amount -> wysokość pożyczki minus (m-czna rata  * (m-czna rata * oprocentowanie )x inflacja)
amountA = amount11 - (monthly_payment + (monthly_payment * loan_interest) * inflation)
#less logika
#less -> początkowa kwota - amount
lessA = float(start_amount - amountA)

print(message.format(month=month, amount=amountA, less=lessA))

#Luty 0%
month = "luty"
inflation = float(0.00)
#amount1 logika
# amount1 -> amount minus (m-czna rata  * (m-czna rata * oprocentowanie )x inflacja)
amountB = amountA - (monthly_payment + (monthly_payment * loan_interest) * inflation)

lessB = float(start_amount - amountB)

print(message.format(month=month, amount=amountB, less=lessB))

#Marzec 2 %
month = "marzec"
inflation = float(0.02)
amountC = amountB - (monthly_payment + (monthly_payment * loan_interest) * inflation)

lessC = float(start_amount - amountC)

print(message.format(month=month, amount=amountC, less=lessC))

#kwiecień 0%
month = "kwiecień"
inflation = float(0.01)
amountD = amountC - (monthly_payment + (monthly_payment * loan_interest) * inflation)

lessD = float(start_amount - amountD)

print(message.format(month=month, amount=amountD, less=lessD))

#maj 1 %
month = "maj"
inflation = float(0.02)
amountE = amountD - (monthly_payment + (monthly_payment * loan_interest) * inflation)

lessE = float(start_amount - amountE)

print(message.format(month=month, amount=amountE, less=lessE))

#czerwiec 1%

month = "czerwiec"
inflation = float(0.01)
amountF = amountE - (monthly_payment + (monthly_payment * loan_interest) * inflation)

lessF = float(start_amount - amountF)

print(message.format(month=month, amount=amountF, less=lessF))

# lipiec 1%

month = "lipiec"
inflation = float(0.01)
amountG = amountF - (monthly_payment + (monthly_payment * loan_interest) * inflation)

lessG = float(start_amount - amountG)

print(message.format(month=month, amount=amountG, less=lessG))

# sierpień 2%
month = "sierpień"
inflation = float(0.02)
amountH = amountG - (monthly_payment + (monthly_payment * loan_interest) * inflation)

lessH = float(start_amount - amountH)

print(message.format(month=month, amount=amountH, less=lessH))

# wrzesień 0%

month = "wrzesień"
inflation = float(0.00)
amountI = amountH - (monthly_payment + (monthly_payment * loan_interest) * inflation)

lessI = float(start_amount - amountI)
#lessI wróć xd

print(message.format(month=month, amount=amountI, less=lessI))

# październik 1%

month = "październik"
inflation = float(0.01)
amountJ = amountI - (monthly_payment + (monthly_payment * loan_interest) * inflation)

lessJ = float(start_amount - amountJ)

print(message.format(month=month, amount=amountJ, less=lessJ))

# listopad 0%

month = "listopad"
inflation = float(0.00)
amountK = amountJ - (monthly_payment + (monthly_payment * loan_interest) * inflation)

lessK = float(start_amount - amountK)

print(message.format(month=month, amount=amountK, less=lessK))

# grudzień 1%

month = "grudzień"
inflation = float(0.01)
amountL = amountK - (monthly_payment + (monthly_payment * loan_interest) * inflation)

lessL = float(start_amount - amountL)

print(message.format(month=month, amount=amountL, less=lessL))
