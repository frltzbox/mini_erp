from kunden import kunden_anzeigen, kunde_hinzufuegen
from produkte import produkt_hinzufuegen
from bestellungen import bestellung_erstellen

def hauptmenue():
    while True:
        print("\n--- Mini-ERP ---")
        print("1: Kunden anzeigen")
        print("2: Kunde hinzufügen")
        print("3: Produkt hinzufügen")
        print("4: Bestellung erstellen")
        print("0: Beenden")
        auswahl = input("Auswahl: ")

        if auswahl == "1":
            kunden_anzeigen()
        elif auswahl == "2":
            name = input("Name: ")
            email = input("E-Mail: ")
            kunde_hinzufuegen(name, email)
        elif auswahl == "3":
            name = input("Produktname: ")
            preis = float(input("Preis: "))
            bestand = int(input("Bestand: "))
            produkt_hinzufuegen(name, preis, bestand)
        elif auswahl == "4":
            kunde_id = int(input("Kunden-ID: "))
            produkt_id = int(input("Produkt-ID: "))
            anzahl = int(input("Anzahl: "))
            bestellung_erstellen(kunde_id, produkt_id, anzahl)
        elif auswahl == "0":
            break
        else:
            print("Ungültige Eingabe.")

if __name__ == "__main__":
    hauptmenue()
