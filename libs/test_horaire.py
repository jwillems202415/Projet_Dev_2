import unittest
from datetime import time
from horaire import Horaire

class TestHoraire(unittest.TestCase):

    def setUp(self):
        """Initialise un horaire pour les tests."""
        self.h = Horaire("09:00", "18:00")

    def test_creation_horaire(self):
        """Test de la création d'un horaire."""
        self.assertIsInstance(self.h.ouverture, time)
        self.assertIsInstance(self.h.fermeture, time)
        self.assertEqual(self.h.ouverture.strftime("%H:%M"), "09:00")
        self.assertEqual(self.h.fermeture.strftime("%H:%M"), "18:00")

    def test_setter_ouverture_valide(self):
        """Test du setter ouverture avec une valeur valide."""
        self.h.ouverture = "08:30"
        self.assertEqual(self.h.ouverture.strftime("%H:%M"), "08:30")

    def test_setter_fermeture_valide(self):
        """Test du setter fermeture avec une valeur valide."""
        self.h.fermeture = "19:00"
        self.assertEqual(self.h.fermeture.strftime("%H:%M"), "19:00")

    def test_setter_ouverture_invalide(self):
        """Le setter doit lever une erreur pour une valeur invalide."""
        with self.assertRaises(ValueError):
            self.h.ouverture = "25:00"

    def test_setter_fermeture_invalide(self):
        """Le setter doit lever une erreur pour une valeur invalide."""
        with self.assertRaises(ValueError):
            self.h.fermeture = "ab:cd"

if __name__ == "__main__":
    unittest.main()
