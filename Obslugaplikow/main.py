from statistics import variance
'''
#zad1
with open("C:\\Users\\Student\\Desktop\\Obslugaplikow\\liczby.txt","r") as file:
    data = file.readlines()
    data = [int(i) for i in data]
print(data)
#suma
el = 0
for i in data:
    el+=i
print(el)
#srednia
sr = el/len(data)
print(sr)
#wariancja
print(variance(data))
#dominanta
N = 15
maxL = 0
maxW = 0
for i in range(0,N):
    W = data[i]
    L = 0
    for j in range(0,N):
        if (data[j] == W):
            L=L+1
        if (L > maxL):
            maxL = L
            maxW = W
for i in data:
    print(i)
print('Najczestszy element ' + str(maxW) + ' wystapil: ' + str(maxL) + ' razy')
#min i max
najmniejsza = None
najwieksza = None
for i in data:
    if najmniejsza == None or najmniejsza > i: 
        najmniejsza = i
        
    if najwieksza == None or najwieksza < i:
        najwieksza = i
        
print ("najmniejsza liczba to:", najmniejsza)
print ("największa liczba to:", najwieksza)
'''
#zad2
def cezar(tryb,klucz,tekst):
    wynik = ""
    for znak in tekst:
        if znak.isalpha():
            if znak.isupper():
                poczatek = ord("A")
            else:
                poczatek = ord("a")
                kod = (ord(znak) - poczatek + tryb * klucz) % 26 + poczatek
                wynik += chr(kod)
        else:
            wynik += znak
    return wynik
    

plik_in = open("C:\\Users\\Student\\Desktop\\Obslugaplikow\\in.txt", "r")
tekst = plik_in.read()
plik_in.close()

wybor = input("Wybierz tryb: 1-szyfrowanie, 2-deszyfrowanie")
if wybor == "1":
    tryb = 1 #szyfrowanie
elif wybor == "2":
    tryb = -1 #deszyfrowanie
else:
    print("Niepoprawny wybor")
    exit()

klucz = int(input("Podaj klucz: "))
if klucz < 0 or klucz >25:
    print("Niepoprawny klucz")
    exit()

wynik = cezar(tryb,klucz,tekst)

plik_out = open("C:\\Users\\Student\\Desktop\\Obslugaplikow\\out.txt", "w")
plik_out.write(wynik)
plik_out.close()

print("Tekst został zapisany")
