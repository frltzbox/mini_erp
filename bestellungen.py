from daten import lade_daten, speichere_daten

KUNDEN_DATEI = "data/kunden.json"
PRODUKTE_DATEI = "data/produkte.json"
BESTELLUNGEN_DATEI = "data/bestellungen.json"

def bestellung_erstellen(kunde_id, produkt_id, anzahl):
    kunden = lade_daten(KUNDEN_DATEI)
    produkte = lade_daten(PRODUKTE_DATEI)
    bestellungen = lade_daten(BESTELLUNGEN_DATEI)

    kunde = next((k for k in kunden if k["id"] == kunde_id), None)
    produkt = next((p for p in produkte if p["id"] == produkt_id), None)

    if not kunde or not produkt:
        print("Kunde oder Produkt nicht gefunden.")
        return

    if produkt["bestand"] < anzahl:
        print("Nicht genug Bestand.")
        return

    produkt["bestand"] -= anzahl
    neue_id = max([b["id"] for b in bestellungen], default=0) + 1
    gesamtpreis = produkt["preis"] * anzahl

    bestellungen.append({
        "id": neue_id,
        "kunde_id": kunde_id,
        "produkt_id": produkt_id,
        "anzahl": anzahl,
        "gesamtpreis": gesamtpreis
    })

    speichere_daten(PRODUKTE_DATEI, produkte)
    speichere_daten(BESTELLUNGEN_DATEI, bestellungen)
    print("Bestellung erfolgreich gespeichert.")
