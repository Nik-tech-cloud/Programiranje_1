def  preberi_vrstice(ime_datoteke):
    return open(ime_datoteke, encoding="utf8").read().splitlines()
    #return list(open(ime_datoteke, encoding="utf8"))

def preberi_csv(ime_datoteke):
    return [ (tuple( (x.split(";")))[0],tuple( (x.split(";")))[1],float(tuple( (x.split(";")))[2])) for x in open(ime_datoteke, encoding="utf8").read().splitlines() ]

def oblikuj(podatki):
    return [(f"Kraj: {terka[0]}, Vreme: {terka[1]}, Temperatura: {terka[2]}°C") for terka in podatki]

def oblikuj_tabelo(podatki):
    l = ["Kraj            Vreme           Temperatura (°C)"]
    l.append("------------------------------------------------")
    for kraj, vreme, temperatura in podatki:
        l.append(f"{kraj:<16}{vreme:<7}{temperatura:>25}")
    return l

def oblikuj_tabelo_f(podatki):
    l = ["Kraj            Vreme           Temperatura (°F)"]
    l.append("------------------------------------------------")
    for kraj, vreme, temperatura in podatki:
        l.append(f"{kraj:<16}{vreme:<7}{round(temperatura*(9/5)+32,1):>25}")
    return l

def oblikuj_pike(podatki):
    l = ["Kraj            Vreme           Temperatura (°F)"]
    l.append("------------------------------------------------")
    for kraj, vreme, temperatura in podatki:
        l.append(f"{kraj:.<16}{vreme:.<7}{round(temperatura * (9 / 5) + 32, 1):.>25}")
    return l

def oblikuj_pike(podatki):
    l = ["Kraj            Vreme           Temperatura (°F)"]
    l.append("------------------------------------------------")
    for kraj, vreme, temperatura in podatki:
        l.append(f"{kraj:.<16}{vreme:.<7}{round(temperatura * (9 / 5) + 32, 1):.>25}")
    return l














### ^^^ Naloge rešujte nad tem komentarjem. ^^^ ###

import unittest

class Testi(unittest.TestCase):

    def setUp(self):
        f = open("podatki.txt","w",encoding='utf-8')
        f.write("Ljubljana;oblačno;12.1\n")
        f.write("Maribor;sončno;9\n")
        f.write("Koper;sončno;14.7\n")
        f.close()

        self.podatki = [('Ljubljana', 'oblačno', 12.1), ('Maribor', 'sončno', 9.0), ('Koper', 'sončno', 14.7)]

    def test_preberi_vrstice(self):
        self.assertEqual(preberi_vrstice("podatki.txt"), ["Ljubljana;oblačno;12.1", "Maribor;sončno;9", "Koper;sončno;14.7"])

    def test_preberi_csv(self):
        self.assertEqual(preberi_csv("podatki.txt"), [('Ljubljana', 'oblačno', 12.1), ('Maribor', 'sončno', 9.0), ('Koper', 'sončno', 14.7)])

    def test_oblikuj(self):
        self.assertEqual(oblikuj(self.podatki),
                         ['Kraj: Ljubljana, Vreme: oblačno, Temperatura: 12.1°C',
                          'Kraj: Maribor, Vreme: sončno, Temperatura: 9.0°C',
                          'Kraj: Koper, Vreme: sončno, Temperatura: 14.7°C'])

    def test_oblikuj_tabelo(self):
        self.assertEqual(oblikuj_tabelo(self.podatki),
                         ['Kraj            Vreme           Temperatura (°C)',
                          '------------------------------------------------',
                          'Ljubljana       oblačno                     12.1',
                          'Maribor         sončno                       9.0',
                          'Koper           sončno                      14.7'])

    def test_oblikuj_tabelo_f(self):
        self.assertEqual(oblikuj_tabelo_f(self.podatki),
                         ['Kraj            Vreme           Temperatura (°F)',
                          '------------------------------------------------',
                          'Ljubljana       oblačno                     53.8',
                          'Maribor         sončno                      48.2',
                          'Koper           sončno                      58.5'])

    def test_oblikuj_pike(self):
        self.assertEqual(oblikuj_pike(self.podatki),
                         ['Kraj            Vreme           Temperatura (°F)',
                          '------------------------------------------------',
                          'Ljubljana.......oblačno.....................53.8',
                          'Maribor.........sončno......................48.2',
                          'Koper...........sončno......................58.5'])

    def test_oblikuj_fc(self):
        self.assertEqual(oblikuj_fc(self.podatki),
                         ['Kraj            Vreme        Temperatura °F (°C)',
                          '------------------------------------------------',
                          'Ljubljana.......oblačno..............53.8 (12.1)',
                          'Maribor.........sončno................48.2 (9.0)',
                          'Koper...........sončno...............58.5 (14.7)'])

    def test_shrani(self):
        lines = ['prva vrstica', 'druga vrstica', 'tretja vrstica']
        shrani(lines, 'datoteka.txt')
        f = open("datoteka.txt", "r")
        lines_f = f.read().splitlines()
        f.close()
        self.assertEqual(lines_f, lines)

    def test_najdaljse_besede(self):
        self.assertEqual(najdaljse_besede('ob znaku bo ura deset in pet minut'), 'znaku, deset, minut')

if __name__ == '__main__':
    unittest.main(verbosity=2)
