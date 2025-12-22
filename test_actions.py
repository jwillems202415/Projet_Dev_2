import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime, time

from libs.reservation import Reservation
from actions import *

class TestActionAdd(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        '2025-12-25 19:30',           # date_res_input
        'Jean Dupont',                 # id_client
        '4',                           # nbr_conv
        '2',                           # nbr_enfants
        'oui',                         # chaise_haute
        'Allergie aux arachides',      # contr_alim 1
        '',                            # contr_alim fin
        '5',                           # num_table
        'Anniversaire',                # type_reserv
        'Gâteau surprise',             # commentaire
        'Marie'                        # id_empl
    ])

    @patch('builtins.print')
    def test_action_add_full_flow(self, mock_print, mock_input):
        # Mock du restaurant
        mock_restaurant = MagicMock()
        mock_restaurant.ajouter_reservation = MagicMock()

        # Appel de la fonction
        action_add(mock_restaurant)

        # Vérification des appels à print (optionnel, pour vérifier l'affichage)

        # Vérification que la réservation a bien été ajoutée
        mock_restaurant.ajouter_reservation.assert_called_once()
        reservation = mock_restaurant.ajouter_reservation.call_args[0][0]

        # Vérifications des attributs de la réservation
        self.assertEqual(reservation.identite_client, 'Jean Dupont')
        self.assertEqual(reservation.identite_employe, 'Marie')
        self.assertEqual(reservation.num_table, 5)
        self.assertEqual(reservation.nombre_personnes, 4)
        self.assertEqual(reservation.nombre_enfants, 2)
        self.assertEqual(reservation.contraintes_alimentaires, ['Allergie aux arachides'])
        self.assertEqual(reservation.date_reservation, '2025-12-25')
        self.assertEqual(reservation.service, 'soir')
        self.assertEqual(reservation.heure_debut, time(19, 30))
        self.assertEqual(reservation.heure_fin, '23:00')
        self.assertEqual(reservation.type_reservation, 'Anniversaire')
        self.assertEqual(reservation.commentaire, '[Chaise haute requise] Gâteau surprise')

    @patch('builtins.input', side_effect=[
        '',                             # date_res_input → default
        'Marie Curie',                  # id_client
        '',                             # nbr_conv → default 2
        '',                             # nbr_enfants → default 0
        '',                             # pas de chaise haute
        '',                             # pas de contraintes
        '3',                            # num_table
        '',                             # type_reserv → default "Normale"
        '',                             # commentaire
        ''                              # id_empl → default "Gaston"
    ])

    @patch('builtins.print')
    def test_action_add_default_values(self, mock_print, mock_input):
        mock_restaurant = MagicMock()
        mock_restaurant.ajouter_reservation = MagicMock()

        action_add(mock_restaurant)

        reservation = mock_restaurant.ajouter_reservation.call_args[0][0]

        self.assertEqual(reservation.identite_client, 'Marie Curie')
        self.assertEqual(reservation.identite_employe, 'Gaston')
        self.assertEqual(reservation.num_table, 3)
        self.assertEqual(reservation.nombre_personnes, 2)
        self.assertEqual(reservation.nombre_enfants, 0)
        self.assertEqual(reservation.contraintes_alimentaires, [])
        self.assertEqual(reservation.date_reservation, datetime.now().strftime('%Y-%m-%d'))
        self.assertEqual(reservation.service, 'soir')  # si l'heure est 20:00
        self.assertEqual(reservation.heure_debut, time(20, 0))
        self.assertEqual(reservation.heure_fin, '23:00')
        self.assertEqual(reservation.type_reservation, 'Normale')
        self.assertEqual(reservation.commentaire, '')

    @patch('builtins.input', side_effect=[
        '0123456789',           # date_res_input → format invalide ❗
        '2025-12-20 18:30',     # date_res_input → format valide ✔️

        '',                     # id_client → vide ❗
        'Bastien Chevillard',   # id_client → rempli ✔️

        '-6',                   # nbr_conv → négatif ❗
        '6',                    # nbr_conv → positif ✔️

        '-1',                   # nbr_enfants → négatif ❗
        '1',                    # nbr_enfants → positif ✔️

        'oui',                  # chaise_haute → OK
        '',                     # contr_alim → vide

        '-3',                   # num_table → négatif ❗
        '3',                    # num_table → positif ✔️

        '',                     # type_reserv → OK (default)
        '',                     # commentaire → OK
        ''                      # id_empl → OK (default)
    ])

    @patch('builtins.print')
    def test_action_add_invalid_inputs(self, mock_print, mock_input):
        mock_restaurant = MagicMock()
        mock_restaurant.ajouter_reservation = MagicMock()

        # Appel de la fonction
        action_add(mock_restaurant)

        
        mock_restaurant.ajouter_reservation.assert_called_once()

        # Vérifie que les messages d'erreur sont bien apparus
        mock_print.assert_any_call("❗ Format invalide. Utilisez le format YYYY-MM-DD HH:MM.\n")    # date_res_input
        mock_print.assert_any_call("❗ Ce champ est obligatoire et ne peut pas être vide.\n")       # id_client
        mock_print.assert_any_call("❗ Cette valeur ne peut pas être inférieure à 1.\n")            # nbr_conv
        mock_print.assert_any_call("❗ Cette valeur ne peut pas être négative.\n")                  # nbr_enfants
        mock_print.assert_any_call("❗ Cette valeur ne peut pas être négative.\n")                  # num_table

if __name__ == '__main__':
    unittest.main()
