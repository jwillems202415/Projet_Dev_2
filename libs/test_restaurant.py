import unittest
import os
from restaurant import Restaurant
from client import Client
from reservation import Reservation

class TestRestaurant(unittest.TestCase):
    
    def setUp(self):
        """Initialisation avant chaque test."""
        # Fichier temporaire pour ne pas écraser les vrais fichiers
        self.fichier_test = "test_reservations.json"
        if os.path.exists(self.fichier_test):
            os.remove(self.fichier_test)
        
        self.resto = Restaurant(fichier_reservations=self.fichier_test)
        self.client = Client("Jean Dupont", 5, "0478123456")
        self.reservation = Reservation(
            identite_client=self.client.identite,
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
    
    def tearDown(self):
        """Nettoyage après chaque test."""
        if os.path.exists(self.fichier_test):
            os.remove(self.fichier_test)
    
    def test_nom_et_chef(self):
        self.assertEqual(self.resto.nom(), "La Bonne Fourchette")
        self.assertEqual(self.resto.chef(), "Gaston")
    
    def test_ajouter_reservation(self):
        self.resto.ajouter_reservation(self.reservation)
        self.assertIn(self.reservation, self.resto.reservations)
        # Vérifier que le fichier JSON a été créé
        self.assertTrue(os.path.exists(self.fichier_test))
    
    def test_supprimer_reservation(self):
        self.resto.ajouter_reservation(self.reservation)
        self.resto.supprimer_reservation(self.reservation)
        self.assertNotIn(self.reservation, self.resto.reservations)
    
    def test_voir_reservations(self):
        self.resto.ajouter_reservation(self.reservation)
        desc_list = self.resto.voir_reservations()
        self.assertEqual(len(desc_list), 1)
        self.assertIn("Jean Dupont", desc_list[0])
    
    def test_supprimer_reservation_inexistante(self):
        # Supprimer une réservation qui n’existe pas ne doit pas lever d’erreur
        try:
            self.resto.supprimer_reservation(self.reservation)
        except Exception as e:
            self.fail(f"supprimer_reservation a levé une exception {e}")

if __name__ == "__main__":
    unittest.main()