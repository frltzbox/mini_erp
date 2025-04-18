import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from kunden import kunde_hinzufuegen
from produkte import produkt_hinzufuegen
from bestellungen import bestellung_erstellen
from daten import lade_daten


def gui_starten():
    root = tk.Tk()
    root.title("📦 Mini-ERP System")
    root.geometry("800x600")
    root.configure(padx=15, pady=15)

    style = ttk.Style()
    style.configure("TNotebook", tabposition='n')
    style.configure("TLabel", font=("Segoe UI", 10))
    style.configure("TButton", font=("Segoe UI", 10))
    style.configure("TEntry", font=("Segoe UI", 10))

    tab_control = ttk.Notebook(root)

    # --- Kunden-Tab ---
    kunden_tab = ttk.Frame(tab_control, padding=15)
    tab_control.add(kunden_tab, text="👥 Kunden")

    ttk.Label(kunden_tab, text="👥 Kunde hinzufügen", font=("Segoe UI", 12, "bold")).grid(column=0, row=0, columnspan=2, pady=10)

    ttk.Label(kunden_tab, text="Name").grid(column=0, row=1, sticky="e", padx=10)
    name_entry = ttk.Entry(kunden_tab, width=30)
    name_entry.grid(column=1, row=1, pady=5)

    ttk.Label(kunden_tab, text="E-Mail").grid(column=0, row=2, sticky="e", padx=10)
    email_entry = ttk.Entry(kunden_tab, width=30)
    email_entry.grid(column=1, row=2, pady=5)

    kunden_text = tk.Text(kunden_tab, height=12, width=80, font=("Consolas", 10))
    kunden_text.grid(column=0, row=6, columnspan=2, padx=10, pady=10)

    def kunden_liste_anzeigen():
        kunden_text.delete(1.0, tk.END)
        kunden = lade_daten("data/kunden.json")
        for k in kunden:
            kunden_text.insert(tk.END, f"[{k['id']}] {k['name']} – {k['email']}\n")

    def kunde_speichern():
        name = name_entry.get()
        email = email_entry.get()
        if name and email:
            kunde_hinzufuegen(name, email)
            kunden_liste_anzeigen()
            messagebox.showinfo("Erfolg", "Kunde hinzugefügt")
        else:
            messagebox.showwarning("Fehler", "Alle Felder ausfüllen")

    ttk.Button(kunden_tab, text="➕ Hinzufügen", command=kunde_speichern).grid(column=1, row=3, sticky="e", pady=10)
    ttk.Button(kunden_tab, text="🔄 Aktualisieren", command=kunden_liste_anzeigen).grid(column=1, row=4, sticky="e", pady=5)
    kunden_liste_anzeigen()

    # --- Produkte-Tab ---
    produkte_tab = ttk.Frame(tab_control, padding=15)
    tab_control.add(produkte_tab, text="📦 Produkte")

    ttk.Label(produkte_tab, text="📋 Produkt hinzufügen", font=("Segoe UI", 12, "bold")).grid(column=0, row=0, columnspan=2, pady=10)

    ttk.Label(produkte_tab, text="Name").grid(column=0, row=1, sticky="e", padx=10)
    produkt_name = ttk.Entry(produkte_tab, width=30)
    produkt_name.grid(column=1, row=1, pady=5)

    ttk.Label(produkte_tab, text="Preis (€)").grid(column=0, row=2, sticky="e", padx=10)
    produkt_preis = ttk.Entry(produkte_tab, width=30)
    produkt_preis.grid(column=1, row=2, pady=5)

    ttk.Label(produkte_tab, text="Bestand").grid(column=0, row=3, sticky="e", padx=10)
    produkt_bestand = ttk.Entry(produkte_tab, width=30)
    produkt_bestand.grid(column=1, row=3, pady=5)

    produkt_text = tk.Text(produkte_tab, height=12, width=80, font=("Consolas", 10))
    produkt_text.grid(column=0, row=6, columnspan=2, padx=10, pady=10)

    def produkte_anzeigen():
        produkt_text.delete(1.0, tk.END)
        produkte = lade_daten("data/produkte.json")
        for p in produkte:
            produkt_text.insert(tk.END, f"[{p['id']}] {p['name']} – {p['preis']} € ({p['bestand']} Stück)\n")

    def produkt_speichern():
        try:
            name = produkt_name.get()
            preis = float(produkt_preis.get())
            bestand = int(produkt_bestand.get())
            if name:
                produkt_hinzufuegen(name, preis, bestand)
                produkte_anzeigen()
                messagebox.showinfo("Erfolg", "Produkt hinzugefügt")
            else:
                messagebox.showwarning("Fehler", "Name fehlt")
        except ValueError:
            messagebox.showerror("Fehler", "Preis und Bestand müssen Zahlen sein")

    ttk.Button(produkte_tab, text="➕ Hinzufügen", command=produkt_speichern).grid(column=1, row=4, sticky="e", pady=10)
    ttk.Button(produkte_tab, text="🔄 Aktualisieren", command=produkte_anzeigen).grid(column=1, row=5, sticky="e", pady=5)
    produkte_anzeigen()

    # --- Bestellungen-Tab ---
    bestellungen_tab = ttk.Frame(tab_control, padding=15)
    tab_control.add(bestellungen_tab, text="🛒 Bestellung")

    ttk.Label(bestellungen_tab, text="🛍️ Neue Bestellung", font=("Segoe UI", 12, "bold")).grid(column=0, row=0, columnspan=2, pady=10)

    kunden_liste = lade_daten("data/kunden.json")
    produkte_liste = lade_daten("data/produkte.json")

    ttk.Label(bestellungen_tab, text="Kunde").grid(column=0, row=1, sticky="e", padx=10)
    kunde_var = tk.StringVar()
    kunde_dropdown = ttk.Combobox(bestellungen_tab, textvariable=kunde_var, state="readonly", width=30)
    kunde_dropdown['values'] = [f"{k['id']}: {k['name']}" for k in kunden_liste]
    kunde_dropdown.grid(column=1, row=1, pady=5)

    ttk.Label(bestellungen_tab, text="Produkt").grid(column=0, row=2, sticky="e", padx=10)
    produkt_var = tk.StringVar()
    produkt_dropdown = ttk.Combobox(bestellungen_tab, textvariable=produkt_var, state="readonly", width=30)
    produkt_dropdown['values'] = [f"{p['id']}: {p['name']}" for p in produkte_liste]
    produkt_dropdown.grid(column=1, row=2, pady=5)

    ttk.Label(bestellungen_tab, text="Anzahl").grid(column=0, row=3, sticky="e", padx=10)
    anzahl_entry = ttk.Entry(bestellungen_tab, width=30)
    anzahl_entry.grid(column=1, row=3, pady=5)

    def bestellung_speichern():
        try:
            kunde_id = int(kunde_var.get().split(":")[0])
            produkt_id = int(produkt_var.get().split(":")[0])
            anzahl = int(anzahl_entry.get())
            bestellung_erstellen(kunde_id, produkt_id, anzahl)
            messagebox.showinfo("Erfolg", "Bestellung erstellt")
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler bei Bestellung: {e}")

    ttk.Button(bestellungen_tab, text="🧾 Bestellung erstellen", command=bestellung_speichern).grid(column=1, row=4, sticky="e", pady=10)

    # --- Umsatz-Tab ---
    umsatz_tab = ttk.Frame(tab_control, padding=15)
    tab_control.add(umsatz_tab, text="📊 Umsatz")

    ttk.Label(umsatz_tab, text="📈 Umsatzreport", font=("Segoe UI", 12, "bold")).pack(pady=10)

    umsatz_canvas_frame = ttk.Frame(umsatz_tab)
    umsatz_canvas_frame.pack(fill="both", expand=True, padx=20, pady=10)

    def zeige_umsatz_report():
        for widget in umsatz_canvas_frame.winfo_children():
            widget.destroy()

        bestellungen = lade_daten("data/bestellungen.json")
        produkte = lade_daten("data/produkte.json")

        umsatz = {}
        for b in bestellungen:
            pid = b["produkt_id"]
            preis = b["gesamtpreis"]
            name = next((p["name"] for p in produkte if p["id"] == pid), f"Produkt {pid}")
            umsatz[name] = umsatz.get(name, 0) + preis

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(umsatz.keys(), umsatz.values(), color='mediumseagreen')
        ax.set_title("Umsatz nach Produkt")
        ax.set_ylabel("Euro")
        ax.tick_params(axis='x', rotation=30)
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=umsatz_canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    ttk.Button(umsatz_tab, text="📊 Umsatz anzeigen", command=zeige_umsatz_report).pack(pady=5)

    # Tabs anzeigen
    tab_control.pack(expand=1, fill='both')
    root.mainloop()


if __name__ == "__main__":
    gui_starten()
