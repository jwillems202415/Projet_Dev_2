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
        "detail": lambda: action_detail(bonne_fourchette),
        "modif": lambda: action_modif(bonne_fourchette),
        "del": lambda: action_del(bonne_fourchette),
        "exit": action_exit,
    }

    while True:
        shell_input = input("> ")
        if shell_input in command_handlers:
            command_handlers[shell_input]()
        else:
            print(f"Commande inconnue : '{shell_input}'. Tapez 'help' pour obtenir la liste des commandes.")


if __name__ == "__main__":
    main()
