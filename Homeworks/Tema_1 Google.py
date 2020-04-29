#Problema 1

# Name = input("Introduceti numele dumneavoastra: ")

# while True:
#     Text = input("Introduceti textul: ")
#     if Text.isdigit():
#         print("Sirul de numere a fost gasit de",Name)
#         break
#     elif Text.isalpha():
#         print("Sirul de caractere a fost gasit de",Name)
#         break
#     else:
#         print("Eroare: Introduceti alt text!")


#Problema 2

# while True:
#     Number = input("Introduceti numarul care trebuie verificat: ")
#     if Number.isdigit() or Number[1:].isdigit():
#         Number = int(Number)
#         if Number&1:
#             print("{} este impar".format(Number))
#             break
#         else:
#             print("{} este par".format(Number))
#             break
#     else:
#         print("Eroare: Nu ati introdus un numar viabil! Incercati din nou. ")



#Problema 3:

# from calendar import isleap
# while True:
#     Year = input("Introduceti anul: ")
#     if Year.isdigit():
#         Year = int(Year)
#         if isleap(Year):
#             print("{} este an bisect".format(Year))
#             break
#         else:
#             print("{} nu este an bisect".format(Year))
#             break
#     else:
#         print("Eroare: Nu ati introdus un an! Incercati din nou.")


#Problema 4:

# while True:
#     number = input("Introduceti numarul: ")
#     if number.isdigit() or (number.replace('.','',1).isdigit() and number.count('.') < 2):
#         if "." in number and int(number.split('.')[1]) != 0:
#             number = float(number)
#         else:
#             number = int(number.split('.')[0])
#         if number > 0:
#             if number < 10:
#                 print("{} este pozitiv si mai mic decat 10".format(number))
#                 break
#
#             else:
#                 print("{} este pozitiv dar este mai mare decat 10".format(number))
#                 break
#
#         elif number == 0:
#             print("Numarul introdus este 0 ")
#             break
#         else:
#             print(-1*number)
#             break
#     else:
#         print("Introduceti  alt numar:")


#Problema 5:

# print("1 – Afisare lista de cumparaturi\n2 – Adaugare element\n3 – Stergere element\n4 – Stergere lista de cumparaturi\n5 - Cautare in lista de cumparaturi ")

# while True:
#     Option = input("Introduceti numarul optiunii: ")
#     if Option == "1":
#         print("Afisare lista de cumparaturi")
#         break
#     elif Option == "2":
#         print("Adaugare element")
#         break
#     elif Option == "3":
#         print("Stergere element")
#         break
#     elif Option == "4":
#         print("Stergere lista de cumparaturi")
#         break
#     elif Option == "5":
#         print("Cautare in lista de cumparaturi")
#         break
#     else:
#         print("Alegerea nu exista. Reincercati")






