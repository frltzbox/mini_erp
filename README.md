##  Ziel des Projekts

Das Projekt simuliert zentrale Geschäftsprozesse kleiner Unternehmen:

- Kundenmanagement
- Produktverwaltung (inkl. Lagerbestand)
- Bestellabwicklung (inkl. Bestandsänderung)

---

##  Technologien

- Programmiersprache: **Python 3**
- Datenformat: **JSON** (für einfache Dateispeicherung)
- Ausführung: **Konsolenbasiert**
- Struktur: **Modular (getrennte Module für Kunden, Produkte, Bestellungen)**

---

## Projektstruktur

```
mini_erp/
│
├── main.py                # Hauptmenü
├── kunden.py              # Kundenverwaltung
├── produkte.py            # Produktverwaltung
├── bestellungen.py        # Bestellabwicklung
├── daten.py               # Daten speichern/laden
├── data/                  # JSON-Dateien (Datenbank-Ersatz)
│   ├── kunden.json
│   ├── produkte.json
│   └── bestellungen.json
└── README.md              # Diese Datei
```

---

##  Beispiel-Funktionalitäten

-  Kunden anlegen und anzeigen
-  Produkte inkl. Preis und Lagerbestand hinzufügen
-  Bestellungen erstellen mit automatischer Bestandsreduzierung
-  Fehlerbehandlung bei leerem Lager oder ungültiger Eingabe

---

## Ausführung

```bash
python3 main.py
python3 gui.py
```

Voraussetzung: Python 3.8+

---
