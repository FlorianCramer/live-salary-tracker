# 💸 Live Salary Counter (Tkinter)

Ein minimalistischer Desktop-Gehaltscounter in Python.
Die App zeigt in Echtzeit, wie viel vom Monatsgehalt seit dem letzten Zahltag bereits verdient wurde – aktualisiert alle 100 ms.

Perfekt für Nerds, Produktivitätsfans und alle, die Zahlen gerne live wachsen sehen.

---

## ✨ Features

* Echtzeit-Berechnung des verdienten Gehalts
* Frei wählbares Monatsbrutto
* Individueller Zahltag (1–31)
* Automatische Berechnung des aktuellen Gehaltszeitraums
* Cleanes Tkinter-GUI
* Läuft lokal ohne Internet

---

## 🧠 Wie funktioniert die Berechnung?

Die App berechnet den aktuellen Gehaltszeitraum basierend auf deinem Zahltag:

* Zeitraum = letzter Zahltag → nächster Zahltag
* Zeitanteil im aktuellen Zeitraum = Fortschritt der Zeit
* Verdientes Gehalt = Monatsgehalt × Zeitanteil

Formel:

```
earned = (vergangene Sekunden / Gesamtsekunden des Zeitraums) * Monatsgehalt
```

Die Anzeige wird alle **100 ms** aktualisiert.

---

## 🖥️ Screenshot (Beschreibung)

UI enthält:

* Eingabefeld für Monatsbrutto
* Eingabefeld für Zahltag
* Start-Button
* Große Live-Anzeige des verdienten Betrags

---

## 🧾 Nutzung

1. Monatsbrutto eingeben (z.B. `3500`)
2. Zahltag eingeben (z.B. `28`)
3. **Start** klicken
4. Zuschauen, wie dein Geld live wächst 💰

---

## ⚠️ Hinweis

Die App ist ein Motivations-/Visualisierungstool und keine Finanzsoftware.
Steuern, Abzüge, Boni etc. werden bewusst nicht berücksichtigt.
