---
title: "Spec-Vorlage: interne Notizen für die Workshop-Leitung"
draft: true
---

Internes Dokument für die Workshop-Leitung. Nicht in den Teilnehmenden-Materialien verlinkt. Hier liegt das theoretische Material, das aus der Teilnehmenden-Version der Spec-Vorlage (`workshop/spec-sheet-template/index.qmd`) entfernt wurde, um die kognitive Last im Workshop selbst zu reduzieren.

## Warum diese Notizen existieren

Die Teilnehmenden-Version der Spec-Vorlage hat drei einfache Sektionen (Lernaufgabe, Skills und Knowledge, Misconceptions). Die theoretische Struktur dahinter ist reicher und wird hier dokumentiert. Wer in der Leitung sicher entscheiden will, was im Raum benannt werden soll und was im Hintergrund läuft, findet hier die Begründungen.

## V/B-Disziplin (vermutet vs. beobachtet)

Bei jedem Spec-Eintrag ist die epistemische Quelle relevant:

- **Vermutet (V):** vom LLM vorgeschlagen oder von der Dozentin aus dem Bauch heraus formuliert, auf Plausibilität geprüft. Für möglich gehalten, aber nicht selbst an Studierenden gesehen.
- **Beobachtet (B):** an tatsächlichen Studierenden gesehen oder gehört. Mindestens ein konkreter Fall hängt daran.

Diese Trennung ist die strengste Disziplin des Spec-Schreibens. Ohne sie wird ein gut-klingendes LLM-Output zu einem autoritativ wirkenden Dokument, das eigentlich nicht überprüft ist.

**Warum die Trennung in der Teilnehmenden-Version nicht explizit ist:** sie verdoppelt die kognitive Last beim Schreiben (jeder Eintrag wird zweimal evaluiert) und kostet im 60-Minuten-Block mehr, als sie im Workshop selbst zurückgibt. Für die Nachbearbeitung nach dem Workshop ist sie zentral: dort kann die Dozentin V-Einträge schrittweise zu B-Einträgen aufwerten, indem sie an realen Studierenden-Antworten prüft.

## KLI-Taxonomie (Knowledge-Learning-Instruction)

Knowledge Components nach Koedinger, Corbett & Perfetti (2012) klassifiziert nach kognitiver Operation:

- **Faktenwissen (Abrufen):** ein einzelnes Item, das aus dem Gedächtnis abgerufen werden muss. Lernmechanismus: aktives Abrufen mit zeitlich verteilter Wiederholung.
- **Klassifikationswissen (Erkennen):** ein Muster oder eine Kategorie, die an einer neuen Instanz erkannt werden muss. Lernmechanismus: verschachtelte Übung mit kontrastierenden Beispielen und Nicht-Beispielen.
- **Erklärungswissen (Begründen):** eine Regel mit erklärender Struktur, die in neuen Situationen mit Verständnis angewandt werden muss. Lernmechanismus: Selbsterklärung an Worked Examples, produktives Scheitern.
- **Integrative Knowledge Components:** lassen sich nicht aus einer einzelnen Aufgabe ableiten. Erfordern Probing über mehrere Aufgaben hinweg. Häufigste blind-spot-Kategorie für Dozierende.

**Warum die Taxonomie in der Teilnehmenden-Version nicht benannt ist:** sie erfordert einen Theorieblock, den der Workshop in drei Stunden nicht mehr trägt, ohne andere Inhalte zu opfern. Die implizite Phrasierung (wissen / erkennen / erklären) der Teilnehmenden-Version erbt die Unterscheidungen, ohne sie als Typologie anzukündigen.

## Misconception-Muster (konzeptuelle Veränderung)

Die Forschung zur konzeptuellen Veränderung (Vosniadou, diSessa, Chi) kennt zwei Muster, die eine Misconception widerständig machen können:

- **Stabiles Modell.** Die Studentin hält die Misconception konsistent, über viele Aufgaben hinweg, auch unter klarem Kontext. Es hat sich zu einem festen Falschmodell verfestigt. Reparatur: Konfrontation mit kontrastiven Fällen, die das Modell zum Scheitern bringen.
- **Kontext-aktivierte Intuition.** Die Studentin rechnet manchmal richtig, manchmal nicht. Unter Zeitdruck, bei sprachlich-fluenten Falschformulierungen kommt die Alltagsintuition zurück. Reparatur: kontextspezifische Praxis.

In der Teilnehmenden-Version ist diese Unterscheidung kollabiert. Beide Muster fallen unter "intuitive Grundlage". Die Reparatur-Implikation ist im Workshop nicht zentral; sie wird in der Nachbearbeitung relevant.

## Falsifikationsnotiz

In der ursprünglichen Sektion D der Spec-Vorlage wählte die Teilnehmerin eine Knowledge Component und beschrieb das Verhalten, das ihre Decomposition falsifizieren würde. Beispiel: "Wenn Studierende, die ich klar als kompetente Korrelationsinterpretiererinnen einschätze, an dieser Teilaufgabe systematisch scheitern, dann ist Baustein 3 nicht das, was diese Aufgabe wirklich testet."

In der Neugestaltung ist die Falsifikationsnotiz in das Take-Home-Handout verschoben, als optionale Aufgabe nach dem Workshop. Begründung: ohne reale Studierenden-Antworten ist die Notiz hypothetisch und kostet im Workshop Zeit, die die produktivere Spec-Tuning-Schlaufe besser nutzt.

## Pruning-Protokoll

In der ursprünglichen Sektion war ein optionales Pruning-Protokoll vorgesehen: Vorschläge, die das LLM gemacht hatte, aber von der Dozentin verworfen wurden, mit Begründung. Eine leere Pruning-Liste bei vollem Spec ist diagnostisch ein Warnsignal: die Dozentin hat nicht gefiltert.

In der Neugestaltung ist das Pruning implizit. Die produktive Phase des Spec-Schreibens ist genau das Aussortieren von LLM-Vorschlägen. Eine separate Spalte dafür kostet Verwaltungsoverhead, ohne im 60-Minuten-Block zusätzliche Disziplin zu erzwingen.

## Vier LLM-Rollen vs. zwei

Die ältere Version der Workshop-Designs nannte vier LLM-Rollen:

1. Hypothesengenerator (LLM schlägt Knowledge Components vor)
2. Lernende-Simulator reaktiv (LLM antwortet auf die Aufgabe als Studentin mit definierten Defiziten)
3. Lernende-Simulator produktiv (LLM erzeugt Misconception-getriebene Falschantworten)
4. Falsifikator (LLM prüft, ob die Decomposition mit realen Antworten konsistent ist)

In der Neugestaltung sind Rollen 1 und 4 implizit (Hypothesengenerator in der Spec-Schreibphase, Falsifikator als post-Workshop-Habit) und Rollen 2 und 3 sind in eine Rolle "Lernende-Simulator" kollabiert. Begründung: Rollen 2 und 3 unterscheiden sich für Teilnehmende nicht beobachtbar.

## Cross-Referenz

- Die ausgearbeitete Statistik-Spec-Card in voller theoretischer Tiefe liegt in diesem Verzeichnis unter `spec-card-statistics-internal.md`.
- Die Notizen zur Workshop-Redesign-Entscheidung liegen in `workshop-redesign-notes.md`.
- Der Strategieplan zur Neugestaltung liegt in `/Users/andrew/.claude/plans/i-have-had-a-vast-swing.md`.
