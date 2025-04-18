import json
import os

def lade_daten(dateipfad):
    if not os.path.exists(dateipfad):
        return []
    with open(dateipfad, "r") as f:
        return json.load(f)

def speichere_daten(dateipfad, daten):
    with open(dateipfad, "w") as f:
        json.dump(daten, f, indent=2)
