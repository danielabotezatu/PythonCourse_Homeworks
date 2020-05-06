from calendar import isleap
while True:
    cnp = input("Introduceti codul numeric personal: ")
    if cnp.isdigit():
        if len(cnp) == 13:
            info = {}
            info.update({'Sex': int(cnp[0])})
            if cnp[0] == "1" or cnp[0] == "2":
                info.update({'Anul nasterii': 1900 + int(cnp[1:3])})
            elif cnp[0] == "3" or cnp[0] == "4":
                info.update({'Anul nasterii': 1800 + int(cnp[1:3])})
            elif cnp[0] == "5" or cnp[0] == "6":
                info.update({'Anul nasterii': 2000 + int(cnp[1:3])})
            else:
                info.update({'Anul nasterii': int(cnp[1:3])})
            if cnp[3] == '0':
                info.update({'Luna': int(cnp[4])})
            info.update({'Ziua': int(cnp[5:7])})
            info.update({'Judet': int(cnp[7:9])})
            info.update({'Cod personal' : int(cnp[9:12])})
            info.update({'Cifra de control': int(cnp[12]) })
            break
        elif len(cnp) < 13:
            print("Nu ati introdus suficiente date")
        else:
            print("Ati introdus prea multe date")

    else:
        print("Nu ati introdus corect datele")

#print(info)

years = { 1: [1900, 1999] , 2: [1900, 1999] , 3: [1800, 1899], 4: [1800, 1899], 5: [2000, 2099], 6: [ 2000, 2999],
          7: 'Persoana straina rezidenta in Romania', 8: 'Persoana straina'}
months = {1: 31, 2: 29 if isleap(info['Anul nasterii']) else 28, 3: 31, 4: 30 , 5: 31, 6: 30, 7: 31, 8:31, 9: 30, 10:31, 11: 30, 12: 31 }

def cifra_de_control_check(x, cnp):
    lista = [2, 7, 9, 1, 4, 6, 3, 5 ,8, 2, 7, 9]
    c = 1 if sum(int(cnp[i]) * lista[i] for i in range(12)) % 11 == 10 else sum(int(cnp[i]) * lista[i] for i in range(12)) % 11
    if c is x:
        return True
    return False

def info_check(info):

    if info['Sex'] not in years:
        return print("Sexul nu este introdus corect")  # verificare gender

    if not 1 <= info['Luna'] <= 12:
        return print("Luna nu este introdusa corect")  # verificare luna

    if not 1 <= info['Ziua'] <= months[info['Luna']]:
        return print("Ziua nu este introdusa corect")  # verificare zi

    if not (1 <= info['Judet']<= 46 or info['Judet'] in [51, 52]):
        return print("Codul judetului nu este introdus corect")  #verificarea codului de judet

    if not 1 <= info['Cod personal'] <= 999:
        return print("Codul personal nu este corect") #verificarea codului personal

    if not cifra_de_control_check(info['Cifra de control'], cnp):
        return print("Cifra de control nu este corecta") #verificarea cifrei de control

    return print("CNP - ul introdus este corect!")

info_check(info)
