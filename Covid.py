import collections as col

def osebe(obiski):
    return set([x for x,y in obiski])

def aktivnosti(obiski):
    return set([y for x,y in obiski])

def udelezenci(aktivnost, obiski):
    return set([x for x,y in obiski if aktivnost == y])

def po_aktivnostih(obiski):
    return {y: udelezenci(y,obiski) for x,y in obiski} #to bi se dalo napisati brez uporabe funkcje, but why not

def skupine(obiski):
    return [y for x,y in po_aktivnostih(obiski).items()]

def okuzeni(skupi, nosilci):
    return set([y for x in ([g for g in skupi for c in g if c in nosilci]) for y in x if y not in nosilci])

def zlati_prinasalec(skupin):
     return min([x for x in set([f for x in skupin for f in x]) if len({x: okuzeni(skupin,x) for x in set([f for x in skupin for f in x])}[max({x: okuzeni(skupin,x) for x in set([f for x in skupin for f in x])},key=lambda k: len({x: okuzeni(skupin,x) for x in set([f for x in skupin for f in x])}[k]))]) == len({x: okuzeni(skupin,x) for x in set([f for x in skupin for f in x])}[x])])

def korakov_do_vseh(skupine, prvi):
    group = skupine.copy()
    infected = set()
    infected.add(prvi)
    krog = 0
    if len(skupine) == 0:
        return 0
    new_infected = None
    while len(group) !=  0:
        krog += 1
        krog_okuženih = []
        for x in reversed(group):
            for y in x:
                if y in infected:
                    krog_okuženih.append(x)
                    group.remove(x)
                    break
        for x in krog_okuženih:
            for y in x:
                infected.add(y)
        if new_infected == None:
            None
        elif len(new_infected) == len(infected):
            return None
        new_infected = infected.copy()
    return krog






import unittest
import random
import ast


class TestObvezna(unittest.TestCase):
    ime = "".join(random.choice("qwertyuiop") for _ in range(10))
    aktivnost = "".join(random.choice("asdfghjkl") for _ in range(10))
    rnd_obiski = [(ime, aktivnost)]

    obiski = [("Ana", "kava"), ("Berta", "kava"), ("Cilka", "telovadba"),
              ("Dani", "zdravnik"), ("Ana", "zdravnik"), ("Cilka", "kava"),
              ("Ema", "telovadba")]

    def test_osebe(self):
        self.assertEqual({"Ana", "Berta", "Cilka", "Dani", "Ema"}, osebe(self.obiski))
        self.assertEqual({self.ime}, osebe(self.rnd_obiski))
        self.assertEqual(set(), osebe([]))

    def test_aktivnosti(self):
        self.assertEqual({"zdravnik", "kava", "telovadba"}, aktivnosti(self.obiski))
        self.assertEqual({self.aktivnost}, aktivnosti(self.rnd_obiski))
        self.assertEqual(set(), aktivnosti([]))

    def test_udelezenci(self):
        self.assertEqual({"Ana", "Berta", "Cilka"}, udelezenci("kava", self.obiski))
        self.assertEqual(set(), udelezenci("sprehod", self.obiski))
        self.assertEqual({self.ime}, udelezenci(self.aktivnost, self.rnd_obiski))
        self.assertEqual(set(), udelezenci(self.aktivnost, []))

    def test_po_aktivnostih(self):
        self.assertEqual({
            "kava": {"Ana", "Berta", "Cilka"},
            "zdravnik": {"Ana", "Dani"},
            "telovadba": {"Cilka", "Ema"}},
            po_aktivnostih(self.obiski))
        self.assertEqual({self.aktivnost: {self.ime}}, po_aktivnostih(self.rnd_obiski))

    def test_skupine(self):
        def form(s):
            return sorted(s, key=lambda x: "-".join(sorted(x)))

        self.assertEqual(
            form([{"Ana", "Berta", "Cilka"}, {"Dani", "Ana"}, {"Cilka", "Ema"}]),
            form(skupine(self.obiski)))

        self.assertEqual(
            form([{self.ime}]),
            form(skupine([(self.ime, self.aktivnost)])))

    def test_okuzeni(self):
        skupine = [{"Ana", "Berta", "Cilka"}, {"Dani", "Ana"}, {"Cilka", "Ema"}, {"Fanči"}]

        self.assertEqual({"Berta", "Cilka", "Dani"},
                         okuzeni(skupine, {"Ana"}))
        self.assertEqual({"Ana", "Berta", "Ema"},
                         okuzeni(skupine, {"Cilka"}))
        self.assertEqual({"Ana", "Cilka"},
                         okuzeni(skupine, {"Ema", "Dani"}))
        self.assertEqual({"Ana", "Ema"},
                         okuzeni(skupine, {"Cilka", "Berta"}))
        self.assertEqual({"Berta", "Cilka", "Dani"},
                         okuzeni(skupine, {"Ana", "Ema"}))
        self.assertEqual({"Cilka"},
                         okuzeni(skupine, {"Ema"}))
        self.assertEqual(set(),
                         okuzeni(skupine, {"Fanči"}))
        self.assertEqual(set(),
                         okuzeni(skupine, set()))
        self.assertEqual({self.ime},
                         okuzeni([{self.ime, self.aktivnost}], {self.aktivnost}))

    def test_zlati_prinasalec(self):
        self.assertEqual(
            "Ana",
            zlati_prinasalec([{"Ana", "Berta", "Cilka"}, {"Dani", "Ana"}, {"Cilka", "Ema"}, {"Cilka"}]))
        self.assertEqual(
            "Cilka",
            zlati_prinasalec([{"Fanči", "Berta", "Cilka"}, {"Dani", "Fanči"}, {"Cilka", "Ema"}, {"Cilka"}]))
        self.assertEqual(
            "Cilka",
            zlati_prinasalec([{"Fanči", "Berta", "Cilka"}, {"Dani", "Fanči"}, {"Cilka", "Ema"}, {"Fanči"}]))

    def test_korakov_do_vseh(self):
        skupine = [{"Cilka", "Ema", "Jana", "Saša"},
                   {"Ema"},
                   {"Fanči", "Greta", "Saša"},
                   {"Greta", "Nina"},
                   {"Greta", "Olga", "Rebeka"},
                   {"Micka", "Ana", "Klara"},
                   {"Fanči", "Iva", "Berta", "Špela"},
                   {"Klara", "Cilka", "Dani"},
                   {"Petra", "Dani", "Lara", "Špela"}]
        self.assertEqual(5, korakov_do_vseh(skupine, "Ana"))
        self.assertEqual(4, korakov_do_vseh(skupine, "Klara"))
        self.assertEqual(4, korakov_do_vseh(skupine, "Dani"))
        self.assertEqual(3, korakov_do_vseh(skupine, "Ema"))

        skupine.append({"Tina"})
        self.assertIsNone(korakov_do_vseh(skupine, "Ema"))
        self.assertIsNone(korakov_do_vseh(skupine, "Tina"))
        skupine[-1].add("Urša")
        skupine[-1].add("Vesna")
        skupine.append({"Zala", "Žana"})
        self.assertIsNone(korakov_do_vseh(skupine, "Ema"))
        self.assertIsNone(korakov_do_vseh(skupine, "Tina"))


class TestOneLineMixin:
    functions = {elm.name: elm
                 for elm in ast.parse(open(__file__, "r", encoding="utf-8").read()).body
                 if isinstance(elm, ast.FunctionDef)}

    def assert_is_one_line(self, func):
        func
        body = self.functions[func.__code__.co_name].body
        self.assertEqual(len(body), 1, "\nFunkcija ni dolga le eno vrstico")
        self.assertIsInstance(body[0], ast.Return, "\nFunkcija naj bi vsebovala le return")

    def test_nedovoljene_funkcije(self):
        dovoljene_funkcije = {
            "preberi_zapiske", "osebe", "aktivnosti", "udelezenci",
            "po_aktivnostih", "skupine", "okuzeni", "zlati_prinasalec",
            "korakov_do_vseh"}
        for func in self.functions:
            self.assertIn(func, dovoljene_funkcije, f"\nFunkcija {func} ni dovoljena.")


class TestDodatna(unittest.TestCase, TestOneLineMixin):
    def test_oneline(self):
        for func in (osebe, aktivnosti, udelezenci, po_aktivnostih, skupine):
            self.assert_is_one_line(func)


class TestIzziv(unittest.TestCase, TestOneLineMixin):
    def test_oneline(self):
        for func in (okuzeni, zlati_prinasalec):
            self.assert_is_one_line(func)


if __name__ == "__main__":
    unittest.main()
