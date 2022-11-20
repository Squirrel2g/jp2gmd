# for i in range(1,101):
#   print(i, end=' ')
# for d in range(101,-1,-1):
#   print(d, end='jp')
# for x in range(7, 77, 7):
#   print(x, end=' ')
# for z in range(20,0,-2):
#   print(z, end=' ')
# x=int(input('podaj liczbę\n'))
# for z in range(0,x):
#   print(3*'( ͡° ͜ʖ ͡°)')
# Lista_zakupów=['chleb','masło','ser','twaróg',5]
# print(Lista_zakupów[0], Lista_zakupów[1])
# Lista_zakupów[2]='mleko'
# print(Lista_zakupów)
# print(Lista_zakupów[-1], Lista_zakupów[-2])

# zestaw_1=[]
# x=input('podaj liczbę')
# for z in range(x):
#   zestaw_1.append((random.randint(1, 100)))
#   print(zestaw_1)

import random
# Utwórz listę zestaw_1 zawierającą liczby losowe z przedziału [1, 10]. Liczbę elementów listy podaje
# użytkownik. Wyświetl listę
# import random
# # zestaw_1 = []
# x = int(input("podaj liczbę x: "))
# y = int(input("podaj liczbę y: "))
# # for i in range(x):
# #     zestaw_1.append(random.randint(1, 10))
# zestaw_1 = [random.randint(1, 10) for i in range(x)]
# print("lista x:", zestaw_1)
# zestaw_2 = [random.randint(5, 15) for i in range(y)]
# print("lista x:", zestaw_2)
# d = input('podaj liczbe')
# if d in zestaw_1 and zestaw_2Utwórz listę punkty będącą listą punktów zdobytych z pewnego egzaminu przez grupę 15 studentów.
# --------------------------------------------------------------------------------------------
# zestaw_1 = []
# print("podaj długość listy")
# l = int(input())
# for x in range(l):
#     n = random.randint(1, 10)
#     zestaw_1.insert(x, n)
#     print(zestaw_1[x], end=" ; ")
# zestaw_2 = []
# print()
# print("podaj długość drugiej listy")
# l = int(input())
# for x in range(l):
#     n = random.randint(5, 15)
#     zestaw_2.insert(x, n)
#     print(zestaw_2[x], end=" ; ")
# print()
# y = int(input())
# if y in zestaw_1:
#     print("liczba w zestawie 1")
# elif y in zestaw_2:
#     print("liczba w zestawie 2")
# else:
#     print("liczby nie ma w zestawach")
# zestaw_1_2 = zestaw_1 + zestaw_2
# print(zestaw_1_2)
# print(zestaw_1_2.sort())
# print(zestaw_1_2)
# -------------------------------------------------------------------------------------------

# Punkty niech będą liczbami rzeczywistymi z przedziału [0; 50]. Następnie
# • Wyświetl informację o największej i najmniejszej ilości zdobytych punktów
# • Wyświetl indeks pierwszego wystąpienia punktów podanych przez użytkownika. Jeżeli taka liczba
# punktów nie występuje na liście, wyświetl odpowiedni komunikat
# • Oblicz średnią punktów liczbę punktów z egzaminu
# • Oblicz, ile osób zdobyło punkty powyżej, a ile poniżej średniej
# • Wyświetl punkty poniżej średniej
# • Wyświetl punkty powyżej średniej
