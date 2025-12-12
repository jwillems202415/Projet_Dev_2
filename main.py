from datetime import datetime, timedelta, time
import sys
from pathlib import Path
import json
import os
import platform
import re
from actions import *

# Ajouter le dossier libs au path pour que Python trouve les modules
# sys.path.insert(0, str(Path(__file__).parent / "libs")) # Nécessaire lors de l'utilisation d'un venv ?

# Imports des classes depuis libs (sans préfixe 'libs.')
from libs.client import Client
from libs.reservation import Reservation
from libs.restaurant import Restaurant

def clear_terminal():
    """Nettoie le terminal de manière portable."""
    if platform.system() == "Windows":
        os.system("cls")
    else:  # Linux/macOS
        os.system("clear")

# reservations_data_file = "reservations.json" Cassé pour le moment

# ------------------------------------------------------------------------------
# PROGRAMME
def main():
    clear_terminal()
    print(r"""
        _            ____
        | |    __ _  | __ )  ___  _ __  _ __   ___
        | |   / _` | |  _ \ / _ \| '_ \| '_ \ / _ \
        | |__| (_| | | |_) | (_) | | | | | | |  __/
        |_____\__,_| |____/ \___/|_| |_|_| |_|\___|
        |  ___|__  _   _ _ __ ___| |__   ___| |_| |_ ___
        | |_ / _ \| | | | '__/ __| '_ \ / _ \ __| __/ _ \
        |  _| (_) | |_| | | | (__| | | |  __/ |_| ||  __/
        |_|  \___/ \__,_|_|  \___|_| |_|\___|\__|\__\___|
        version 0.3
        """)
    print(f"Bienvenue dans le gestionnaire des réservations.\nTapez « help » pour obtenir la liste des commandes disponibles.")
    bonne_fourchette = Restaurant() # Initialisation du restaurant

    command_handlers = { # « Gestionnaire » des commandes
        "help": action_help,
        "add": lambda: action_add(bonne_fourchette),
        "list": lambda: action_list(bonne_fourchette),
        "delete": action_del,
        "exit": action_exit,
    }

    global reservations
    # Charger les données enregistrées.

    try:
        with open(reservations_data_file, "r", encoding="utf-8") as f:
            reservations = json.load(f)
        print("✅ Données chargées depuis reservation.json")
    except:
        print("❗ Attention : Aucun fichier « reservations.json » trouvé. Un nouveau fichier sera alors créé. Interrompez immédiatement l'application pour annuler.\n")
        reservations = {}

    while True:
        shell_input = input("> ")
        if shell_input in command_handlers:
            command_handlers[shell_input]()
        else:
            print(f"Commande inconnue : '{shell_input}'. Tapez 'help' pour obtenir la liste des commandes.")


if __name__ == "__main__":
    main()
