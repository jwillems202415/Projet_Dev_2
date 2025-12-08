import unittest
from client import Client

class TestClient(unittest.TestCase):

    def setUp(self):
        """Initialise un client pour les tests."""
        self.c = Client("Jean Dupont", 5, "0478123456")

    def test_creation_client(self):
        """Test de la création d'un client."""
        self.assertEqual(self.c.identite, "Jean Dupont")
        self.assertEqual(self.c.preference_table, 5)
        self.assertEqual(self.c.contact, "0478123456")

    def test_setter_identite_valide(self):
        """Test du setter identite avec une valeur valide."""
        self.c.identite = "Alice Martin"
        self.assertEqual(self.c.identite, "Alice Martin")

    def test_setter_identite_invalide(self):
        """Le setter identite ne doit pas accepter les chiffres."""
        with self.assertRaises(ValueError):
            self.c.identite = "Jean123"

    def test_setter_preference_table_valide(self):
        """Test du setter preference_table avec une valeur valide."""
        self.c.preference_table = 10
        self.assertEqual(self.c.preference_table, 10)

    def test_setter_preference_table_invalide(self):
        """Le setter preference_table doit lever une erreur si hors limites."""
        with self.assertRaises(ValueError):
            self.c.preference_table = 0
        with self.assertRaises(ValueError):
            self.c.preference_table = 13

    def test_setter_contact_valide(self):
        """Test du setter contact avec une valeur valide."""
        self.c.contact = "0488123456"
        self.assertEqual(self.c.contact, "0488123456")

    def test_setter_contact_invalide(self):
        """Le setter contact doit lever une erreur pour des valeurs invalides."""
        with self.assertRaises(ValueError):
            self.c.contact = "12345"
        with self.assertRaises(ValueError):
            self.c.contact = "0578123456"
        with self.assertRaises(TypeError):
            self.c.contact = 478123456

if __name__ == "__main__":
    unittest.main()
