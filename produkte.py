from daten import lade_daten, speichere_daten

DATEIPFAD = "data/produkte.json"

def produkt_hinzufuegen(name, preis, bestand):
    produkte = lade_daten(DATEIPFAD)
    neue_id = max([p["id"] for p in produkte], default=0) + 1
    produkte.append({
        "id": neue_id,
        "name": name,
        "preis": preis,
        "bestand": bestand
    })
    speichere_daten(DATEIPFAD, produkte)
    print("Produkt erfolgreich hinzugefügt.")
