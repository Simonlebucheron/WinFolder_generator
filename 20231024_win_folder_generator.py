# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:02:13 2023

@author: e_sdelai
"""

import os
from datetime import datetime

# La fonction mkdir_with_parents permet de créer de manière récursive
# un arbre de dossiers avec une seule instruction
def mkdir_with_parents(path):
    try:
        os.makedirs(path)
    except OSError as e:
        if not os.path.isdir(path):
            raise

# Chemin du dossier parent (situé dans le répertoire courant)
parent_folder = "./"

# Nom du dossier à créer
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
folder_name = f"{timestamp}_result"

# Chemin complet du dossier à créer
full_path = os.path.join(parent_folder, folder_name)

# Liste des dossiers à créer
dirs_to_create = [
    "PXI",
    "PXI/00_Archive",
    "PXI/01_Test benchs",
    "PXI/01_Test benchs/01_test bench Pierre",
    "PXI/01_Test benchs/02_test bench Paul",
    "PXI/01_Test benchs/99_test bench Jacques Template",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Cartes interfaces",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Cartes interfaces/01_carte interface Tom",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Cartes interfaces/02_carte interface Dick",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Cartes interfaces/99_Carte interface Template",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Cartes interfaces/99_Carte interface Template/Datasheet",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Cartes interfaces/99_Carte interface Template/Dossier de fabrication",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Cartes interfaces/99_Carte interface Template/Mecanique",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Cartes interfaces/99_Carte interface Template/Nomenclature",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Cartes interfaces/99_Carte interface Template/Photos",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Cartes interfaces/99_Carte interface Template/Routage",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Cartes interfaces/99_Carte interface Template/Schema electrique",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Cartes interfaces/99_Carte interface Template/Tests et mesures CI",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Cartes interfaces/99_Carte interface Template/Tests et mesures CI/Procedure",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Cartes interfaces/99_Carte interface Template/Tests et mesures CI/Rapports de tests",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Datasheet",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Dossier de fabrication",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Nomenclature",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Mecanique",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Photos",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Plans harnais",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Plans harnais/Interne baie",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Plans harnais/01_projet Marie",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Plans harnais/02_projet Jeanne",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Plans harnais/99_projet Francoise",
    "PXI/01_Test benchs/99_test bench Jacques Template/Hardware banc/Synoptique general",
    "PXI/01_Test benchs/99_test bench Jacques Template/Software banc",
    "PXI/01_Test benchs/99_test bench Jacques Template/Software banc/Configuration tools",
    "PXI/01_Test benchs/99_test bench Jacques Template/Software banc/01_projet Marie",
    "PXI/01_Test benchs/99_test bench Jacques Template/Software banc/02_projet Jeanne",
    "PXI/01_Test benchs/99_test bench Jacques Template/Software banc/99_projet Francoise Template",
    "PXI/01_Test benchs/99_test bench Jacques Template/Software banc/99_projet Francoise Template/release",
    "PXI/01_Test benchs/99_test bench Jacques Template/Software banc/99_projet Francoise Template/docs",
    "PXI/01_Test benchs/99_test bench Jacques Template/Software banc/99_projet Francoise Template/external tools",
    "PXI/01_Test benchs/99_test bench Jacques Template/Software banc/99_projet Francoise Template/src",
    "PXI/01_Test benchs/99_test bench Jacques Template/Maintenance banc",
    "PXI/01_Test benchs/99_test bench Jacques Template/Maintenance banc/Metrologie",
    "PXI/01_Test benchs/99_test bench Jacques Template/Maintenance banc/Metrologie/Rapport etalonnage",
    "PXI/01_Test benchs/99_test bench Jacques Template/Maintenance banc/Metrologie/Rapport de verification/calibration",
    "PXI/01_Test benchs/99_test bench Jacques Template/Maintenance banc/Outils de test",
    "PXI/01_Test benchs/99_test bench Jacques Template/Maintenance banc/Plan de maintenance",
    "PXI/01_Test benchs/99_test bench Jacques Template/Essais",
    "PXI/01_Test benchs/99_test bench Jacques Template/Essais/Procedures de test",
    "PXI/01_Test benchs/99_test bench Jacques Template/Essais/Rapports de test",
    "PXI/01_Test benchs/99_test bench Jacques Template/Essais/Revue qualite",
    "PXI/02_Projects",
    "PXI/02_Projects/01_Projet Marie",
    "PXI/02_Projects/02_projet Jeanne",
    "PXI/02_Projects/99_projet Francoise Template",
    "PXI/02_Projects/99_projet Francoise Template/Specification",
    "PXI/02_Projects/99_projet Francoise Template/Plan de cablage [link]",
    "PXI/02_Projects/99_projet Francoise Template/Hardware [link]",
    "PXI/02_Projects/99_projet Francoise Template/Software [link]",
]

# Création des dossiers
for directory in dirs_to_create:
    mkdir_with_parents(os.path.join(full_path, directory))

print("L'architecture de dossier a été créée avec succès !")