from daten import lade_daten, speichere_daten

DATEIPFAD = "data/kunden.json"

def kunden_anzeigen():
    kunden = lade_daten(DATEIPFAD)
    for k in kunden:
        print(f"[{k['id']}] {k['name']} – {k['email']}")

def kunde_hinzufuegen(name, email):
    kunden = lade_daten(DATEIPFAD)
    neue_id = max([k["id"] for k in kunden], default=0) + 1
    kunden.append({"id": neue_id, "name": name, "email": email})
    speichere_daten(DATEIPFAD, kunden)
    print("Kunde erfolgreich hinzugefügt.")
