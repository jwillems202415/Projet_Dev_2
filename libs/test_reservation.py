import unittest
from datetime import datetime
from reservation import Reservation
from table import Table
from horaire import Horaire

class TestReservation(unittest.TestCase):

    def setUp(self):
        # Création d'une réservation de base pour les tests
        self.reservation = Reservation(
            identite_client="Jean Dupont",
            identite_employe="Alice Martin",
            num_table=3,
            nombre_personnes=4,
            nombre_enfants=1,
            contraintes_alimentaires="Végétarien",
            date_reservation="2025-12-25",
            service="midi",
            heure_debut="12:30",
            heure_fin="14:00",
            type_reservation="Anniversaire",
            commentaire="Pas de gâteau, merci."
        )

    def test_creation_reservation(self):
        # Vérifie que les attributs sont bien initialisés
        self.assertEqual(self.reservation.identite_client, "Jean Dupont")
        self.assertEqual(self.reservation.identite_employe, "Alice Martin")
        self.assertEqual(self.reservation.num_table, 3)
        self.assertEqual(self.reservation.nombre_personnes, 4)
        self.assertEqual(self.reservation.nombre_enfants, 1)
        self.assertEqual(self.reservation.contraintes_alimentaires, "Végétarien")
        # On compare maintenant la date_reservation avec un string ou date selon l'implémentation
        self.assertEqual(str(self.reservation.date_reservation), "2025-12-25")
        self.assertEqual(self.reservation.service, "midi")
        self.assertEqual(self.reservation.heure_debut, "12:30")
        self.assertEqual(self.reservation.heure_fin, "14:00")
        self.assertEqual(self.reservation.type_reservation, "Anniversaire")
        self.assertEqual(self.reservation.commentaire, "Pas de gâteau, merci.")

    def test_nombre_personnes_valide(self):
        self.reservation.nombre_personnes = 3
        self.assertEqual(self.reservation.nombre_personnes, 3)

    def test_nombre_personnes_trop_grand(self):
        with self.assertRaises(ValueError):
            self.reservation.nombre_personnes = 10

    def test_nombre_personnes_trop_petit(self):
        with self.assertRaises(ValueError):
            self.reservation.nombre_personnes = 0

    def test_service_valide(self):
        self.reservation.service = "soir"
        self.assertEqual(self.reservation.service, "soir")

    def test_service_invalide(self):
        with self.assertRaises(ValueError):
            self.reservation.service = "matin"

    def test_heure_debut_valide(self):
        self.reservation.heure_debut = "12:00"
        self.assertEqual(self.reservation.heure_debut, "12:00")

    def test_heure_debut_invalide(self):
        with self.assertRaises(ValueError):
            self.reservation.heure_debut = "11:00"

    def test_heure_fin_valide(self):
        self.reservation.heure_fin = "14:30"
        self.assertEqual(self.reservation.heure_fin, "14:30")

    def test_heure_fin_invalide(self):
        with self.assertRaises(ValueError):
            self.reservation.heure_fin = "15:00"

    def test_date_reservation_lundi(self):
        with self.assertRaises(ValueError):
            self.reservation.date_reservation = "2025-12-22"

    # TESTS POUR DESCRIPTION, STR ET REPR
    def test_description(self):
        desc = self.reservation.description()
        self.assertIsInstance(desc, str)
        self.assertIn("Jean Dupont", desc)

    def test_str(self):
        s = str(self.reservation)
        self.assertIsInstance(s, str)
        self.assertIn("Jean Dupont", s)

    def test_repr(self):
        r = repr(self.reservation)
        self.assertIsInstance(r, str)
        self.assertIn("Jean Dupont", r)

if __name__ == "__main__":
    unittest.main()
