def wczytaj_tekst(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
            return plik.read()
    except FileNotFoundError:
        return None

def zapisz_slownik(slownik, nazwa_pliku='C:\\Users\\Student\\Desktop\\Obslugaplikow2\\dict.txt'):
    with open(nazwa_pliku, 'w', encoding='utf-8') as plik:
        for wyraz, liczba in slownik.items():
            plik.write(f'{wyraz} {liczba}\n')

def aktualizuj_slownik(tekst, slownik):
    for wyraz in tekst.split():
        wyraz = wyraz.lower().strip('.,!?')
        if wyraz:
            slownik[wyraz] = slownik.get(wyraz, 0) + 1

slownik = {}
tekst = wczytaj_tekst('C:\\Users\\Student\\Desktop\\Obslugaplikow2\\in.txt')

if tekst is None:
    print("Plik 'in.txt' nie istnieje.")

slownik_z_pliku = wczytaj_tekst('C:\\Users\\Student\\Desktop\\Obslugaplikow2\\dict.txt')

if slownik_z_pliku is not None:
    for linia in slownik_z_pliku.splitlines():
        wyraz, liczba = linia.split()
        slownik[wyraz] = int(liczba)

aktualizuj_slownik(tekst, slownik)
zapisz_slownik(slownik)
