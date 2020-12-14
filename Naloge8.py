def capitalize(seznam):
    return [x.capitalize() for x in seznam]

def icapitalize(seznam):
    for x,y in enumerate(seznam):
        seznam[x] = y.capitalize()

def zamenjano(s, menjave):
    rez = []
    for x in (s):
        if x not in menjave:
            rez.append(x)
            continue
        rez.append(menjave[x])
    return rez

def zamenjaj(s, menjave):
    for y,x in enumerate(s):
        if x not in menjave:
            s[y] = x
            continue
        s[y] = menjave[x]

def alterniraj(s):
    x = 0
    if s[x] >= 0:
        poz = True
        iscemoNeg = True
    else:
        poz = False
        iscemoNeg = False
    x = 1
    while x != len(s):
        if s[x] > 0:
            poz = True
        else:
            poz = False
        if iscemoNeg == True:
            if poz == True:
                s.pop(x)
            elif poz == False:
                poz = False
                iscemoNeg = False
                x = x + 1
        elif iscemoNeg == False:
            if poz == False:
                s.pop(x)
            elif poz == True:
                poz = True
                iscemoNeg = True
                x = x + 1

def dodaj_isti(s):
    g = s.copy()
    for x in g:
        s.append(x.c)

def dodaj_enak(s):
    g = s.copy()
    for x in g:
        s.append(x.copy())


### ^^^ Naloge rešujte nad tem komentarjem. ^^^ ###

import unittest

class TestSpremenljivke(unittest.TestCase):
    def test_capitalize(self):
        orig = ['marko', 'Miha', 'maja', 'Monika']
        imena = orig[:]
        cimena = ['Marko', 'Miha', 'Maja', 'Monika']
        self.assertEqual(capitalize(imena), cimena)
        self.assertEqual(imena, orig)

    def test_icapitalize(self):
        imena = ['marko', 'Miha', 'maja', 'Monika']
        cimena = ['Marko', 'Miha', 'Maja', 'Monika']
        self.assertIsNone(icapitalize(imena))
        self.assertEqual(imena, cimena)

    def test_zamenjano(self):
        orig = ["Ana", "Ana", "Berta", "Ana", "Cilka"]
        imena = orig[:]
        z = zamenjano(imena, {"Ana": "Peter", "Berta": "Ana"})
        self.assertEqual(z, ["Peter", "Peter", "Ana", "Peter", "Cilka"])
        self.assertEqual(imena, orig)

    def test_zamenjaj(self):
        imena = ["Ana", "Ana", "Berta", "Ana", "Cilka"]
        self.assertIsNone(zamenjaj(imena, {"Ana": "Peter", "Berta": "Ana"}))
        self.assertEqual(imena, ["Peter", "Peter", "Ana", "Peter", "Cilka"])

    def test_alterniraj(self):
        seznam = [3, 4, -1, 1, -5, -2, -1, 7, -8]
        self.assertIsNone(alterniraj(seznam))
        self.assertEqual(seznam, [3, -1, 1, -5, 7, -8])

        seznam = [-1, 1, -5, -2, -1, 7, 8]
        self.assertIsNone(alterniraj(seznam))
        self.assertEqual(seznam, [-1, 1, -5, 7])

        seznam = [-1, -2]
        self.assertIsNone(alterniraj(seznam))
        self.assertEqual(seznam, [-1])

        seznam = [2]
        self.assertIsNone(alterniraj(seznam))
        self.assertEqual(seznam, [2])

    def test_dodaj_isti(self):
        s = [[1, 2], [3], [7, 1, 2]]
        self.assertIsNone(dodaj_isti(s))
        s[0].clear()
        self.assertEqual(s, [[], [3], [7, 1, 2], [], [3], [7, 1, 2]])

    def test_dodaj_enak(self):
        s = [[1, 2], [3], [7, 1, 2]]
        self.assertIsNone(dodaj_enak(s))
        s[0].clear()
        self.assertEqual(s, [[], [3], [7, 1, 2], [1, 2], [3], [7, 1, 2]])

    def test_poenoti(self):
        s = [[1, 2], [3], [1, 2], [1, 2], [3]]
        poenoti(s)
        s[2].append(9)
        self.assertEqual(s, [[1, 2, 9], [3], [1, 2, 9], [1, 2, 9], [3]])

    def test_razenoti(self):
        s = [[]] * 10
        s[0].append(1)
        self.assertEqual(s, [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1]])
        razenoti(s)
        s[1].append(2)
        self.assertEqual(s, [[1], [1, 2], [1], [1], [1], [1], [1], [1], [1], [1]])

    def test_slikaj(self):
        self.assertEqual(slikaj(abs, [-5, 8, -3, -1, 3]), [5, 8, 3, 1, 3])
        self.assertEqual(slikaj(len, "Daydream delusion limousine eyelash".split()), [8, 8, 9, 7])
        self.assertEqual(slikaj(lambda x: x+1, [1,2,3]), [2,3,4])


if __name__ == '__main__':
    unittest.main(verbosity=2)
