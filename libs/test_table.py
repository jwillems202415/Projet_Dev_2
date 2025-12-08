import unittest
from table import Table

class TestTable(unittest.TestCase):

    def setUp(self):
        # Création d'une table pour les tests
        self.table = Table("Table impressionniste", 1, 4, "Baie vitrée")

    def test_nom(self):
        self.assertEqual(self.table.nom, "Table impressionniste")

    def test_numero(self):
        self.assertEqual(self.table.numero, 1)

    def test_capacite(self):
        self.assertEqual(self.table.capacite, 4)

    def test_emplacement(self):
        self.assertEqual(self.table.emplacement, "Baie vitrée")

    def test_str(self):
        s = str(self.table)
        self.assertIsInstance(s, str)
        self.assertIn("Table impressionniste", s)
        self.assertIn("Numéro: 1", s)
        self.assertIn("Capacité: 4", s)
        self.assertIn("Emplacement: Baie vitrée", s)

    def test_repr(self):
        r = repr(self.table)
        self.assertIsInstance(r, str)
        self.assertIn("Table impressionniste", r)
        self.assertIn("1", r)
        self.assertIn("4", r)
        self.assertIn("Baie vitrée", r)

if __name__ == "__main__":
    unittest.main()
