---
title: "Facilitator Notes: Block 1 (Theorie und Beispiel)"
draft: true
---

Internes Dokument für die Workshop-Leitung. Ergänzt die in-page Moderationshinweise in [Block 1](../workshop/block-1-theorie-und-beispiel/index.qmd).

## Zeitbudget (35 min)

| Min | Phase | Aktivität |
|-----|-------|-----------|
| 0:00-0:05 | Eröffnungs-Slides | Drei Sätze (Hartes Problem, Expert Blind Spot, Das LLM als Hypothesengenerator) plus 30-Sek-Referenz auf die drei Wissenstypen |
| 0:05-0:30 | Worked Example | Live-Walkthrough durch die Multiple-Regression-Aufgabe |
| 0:30-0:35 | Spec-Vorschau | Spec-Vorlage zeigen, gefülltes Beispiel daneben halten, Brücke zu Block 2 schlagen |

## Eröffnung Block 1 (nach Einstieg)

> Was ihr gerade erlebt habt, hat einen Namen. In den nächsten fünf Minuten hört ihr drei Sätze, die den Workshop tragen. Dann zeige ich euch an einer konkreten Aufgabe, wie ein LLM denselben Effekt für euch arbeiten lässt.

Direkt zur ersten Slide.

## Die drei Eröffnungs-Slides

Wortlaut verbatim auf jeder Slide, langsam vorgelesen, mit Pausen:

1. **Ein schwieriges Problem.** Eine der schwierigsten pädagogischen Tätigkeiten beim Einsatz von KI in der Lehre ist nicht das Auswählen eines Werkzeugs, sondern das Spezifizieren dessen, was im Kopf der Lernenden passieren soll.
2. **Der Expert Blind Spot.** Lehrpersonen sehen oft nicht, was ihre Lernenden noch nicht wissen, weil Automatisierung viele Teilfertigkeiten unsichtbar gemacht hat.
3. **Das LLM als Hypothesengenerator.** Ein LLM, das als Person geprompted wird, die gerade die Vorgängerveranstaltung abgeschlossen hat, aber diese hier noch nicht kennt, kann Teilschritte aufzählen, die ein Experte überspringt. Die Annahme dahinter: in dieser Rolle teilt das LLM die automatisierten Routinen der Expertin nicht.

Nach jedem Satz eine bewusste Pause (ca. 3 Sekunden), nicht weiter elaborieren. Die Sätze tragen den ganzen Workshop; sie brauchen Raum, nicht Erklärung.

Direkt danach die Mini-Slide "Drei Typen von Wissensbausteinen" (~30 Sek): Faktenwissen (Abrufen), Klassifikationswissen (Erkennen), Erklärungswissen (Begründen), mit je einem Beispiel aus dem Worked Example. Volllänge im Block-1-Nachlesen-Tab.

## Worked-Example-Walkthrough (25 min)

Die [Worked-Example-Seite](../workshop/block-1-theorie-und-beispiel/worked-example-statistics.qmd) auf der Leinwand öffnen und gemeinsam durchgehen. Vier Stationen kommentieren, jede etwa 5 Minuten:

### Station 1: Die Daten und die Teilaufgabe (5 min)

Den simulierten Datensatz zeigen, die Aufgabenstellung lesen lassen. Botschaft: das ist eine Aufgabe, wie sie in einem Statistik-II-Kurs tatsächlich vorkommt; der Datensatz ist klein gehalten, damit die Tabellen lesbar bleiben.

### Station 2: Die typische Lernenden-Antwort (5 min)

Die als Zitat ausgewiesene Antwort vorlesen. **Inszenierte Pause:** "Diese Antwort gilt in den meisten Klausuren als vollständig richtig. Was übersieht eine Lehrperson, die diese Antwort durchwinkt?" Antworten aus dem Plenum kurz einsammeln, nicht auflösen.

### Station 3: Der Hypothesengenerator-Prompt und die Enumeration (10 min)

Den Prompt zeigen. Wichtig: den Prompt nicht erklären, sondern *zeigen*. Die Teilnehmenden werden den exakten Wortlaut in Block 2 brauchen; sie sehen ihn jetzt zum ersten Mal.

Die Enumeration in den drei Typen (Faktenwissen, Klassifikationswissen, Erklärungswissen) gemeinsam überfliegen, nicht jede Zeile lesen. Auf eine oder zwei Stellen pro Typ kurz zeigen, dann zur nächsten.

### Station 4: Die nicht thematisierten Voraussetzungen (5 min)

Auf die vier hervorgehobenen Punkte verweilen:

- "kontrolliert für" als bedingte Lesart (nicht als Eingriff)
- der Intercept $b_0$ und das Zentrieren
- warum $b_1$ und $r_{YX_1}$ unterschiedlich sind (Suppression)
- $R^2$ ist nicht additiv

Das ist die dramatische Stelle des Blocks. Nicht durchhetzen.

## Häufige Stolperstellen und Redirects

**"Ich verstehe das Beispiel nicht inhaltlich."** Bei nicht-Statistik-Teilnehmenden absehbar. Verweisen auf den Methoden-Fokus: "Die statistischen Details sind nicht relevant. Achtet darauf, *wie* das LLM die Voraussetzungen auflistet, nicht *was* es auflistet."

**"Hat das LLM nicht einfach erfunden, was es gesagt hat?"** Berechtigte Frage. Antwort: Ja, das LLM hat eine plausible Liste konstruiert, nicht eine gemessene. Genau deshalb gibt es in Block 2 die V/B-Disziplin: jeder Eintrag wird als *vermutet* markiert, bis die Lehrperson ihn an realen Lernenden geprüft hat. Auf die Caution-Box in der Worked-Example-Seite verweisen.

**"Wie weiss ich, dass die vier Blind-Spot-Stellen die richtigen sind?"** Sie sind nicht "die richtigen". Sie sind die vier, die in diesem Kurs nicht explizit gelehrt wurden, obwohl sie für die Antwort gebraucht werden. In einem anderen Kurs könnten andere Stellen die Blind Spots sein.

**Teilnehmende lesen den R-Code Wort für Wort.** Wenn das passiert: kurz unterbrechen und sagen, der R-Code dient nur dazu, das LLM mit konkretem Material zu füttern. Die Tabellen und Plots zeigen, was die Lernende lesen muss.

## Typische Fragen aus dem Plenum

- *"Kann ich auch ein anderes Modell als Claude verwenden?"* — Ja. ChatGPT, Copilot, HuggingChat funktionieren alle. Der Prompt ist modellunabhängig.
- *"Muss meine Aufgabe so technisch sein wie das Beispiel?"* — Im Gegenteil. Eine textuelle Aufgabe aus einem Sprachfach funktioniert mindestens so gut.
- *"Was ist mit längerem Material? Kann ich ein ganzes Skript einfügen?"* — Ja, solange es in das Kontextfenster passt. Bei sehr langen Materialien kann es helfen, die Musterlösung separat zu schicken.

## Wenn die Zeit knapp wird

Station 1 (Daten) kann auf 2-3 Minuten verkürzt werden. Station 4 (die Blind-Spot-Punkte) ist nicht kürzbar — das ist die methodische Pointe des Blocks. Die Spec-Vorschau am Ende kann auf 2-3 Minuten gekürzt werden, wenn die [Spec-Vorlage](../workshop/spec-sheet-template/index.qmd) und das [Beispiel-Spec](../workshop/spec-sheet-template/example-multiple-regression.md) im Take-Home stehen.

## Take-away Satz für Block 1

> Du hast gesehen, wie ein LLM in der Rolle einer noch nicht fortgeschrittenen Lernenden die Voraussetzungen einer Aufgabe externalisiert, die der Lehrperson selbst nicht mehr auffallen. In Block 2 machst du dasselbe mit deiner eigenen Aufgabe.

Direkt in die Pause überleiten, dann in Block 2 starten.
