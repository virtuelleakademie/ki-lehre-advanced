---
title: "Facilitator Notes: Block 2 (Dein eigenes Spec)"
draft: true
---

Internes Dokument für die Workshop-Leitung. Ergänzt die in-page Moderationshinweise in [Block 2](../workshop/block-2-spec-card/index.qmd).

## Zeitbudget (60 min)

| Min | Phase | Aktivität |
|-----|-------|-----------|
| 0:00-0:05 | Orientierung | Spec-Vorlage zeigen, Teilaufgabe wählen, Sektion 1 ausfüllen |
| 0:05-0:25 | Sektion 2 | Hypothesengenerator an eigenes Material; Output validieren, Sektion 2 füllen |
| 0:25-0:40 | Sektion 3 | LLM als Lernende-Simulator; Misconception generieren, Sektion 3 füllen |
| 0:40-0:55 | Paar-Review | Cross-discipline Paar liest sich gegenseitig die Specs |
| 0:55-1:00 | Wrap | Spec speichern, Vorschau auf Block 3 |

Block 2 ist die längste Eigenarbeitsphase des Workshops. Die Workshop-Leitung gibt die ersten 3 Minuten Orientierung, dann wandert sie zwischen den Tischen.

## Eröffnung Block 2 (nach der Pause)

> Jetzt baust du selbst, was du in Block 1 an der Multiple-Regression beobachtet hast. Vor euch liegt die Spec-Vorlage; sie hat drei Sektionen. Ihr wechselt im Lauf der Stunde zwischen zwei LLM-Rollen: erst Hypothesengenerator für Sektion 2, dann Lernende-Simulator für Sektion 3. Am Ende reviewt ihr euch gegenseitig in cross-discipline Paaren.

Die [Spec-Vorlage](../workshop/spec-sheet-template/index.qmd) und das [Beispiel-Spec](../workshop/spec-sheet-template/example-multiple-regression.md) parallel zeigen, sodass die Teilnehmenden beide griffbereit haben.

## Pacing-Cues für die Workshop-Leitung

Während der Eigenarbeit über die Schultern schauen und an folgenden Zeitmarken kurz sammeln:

- **Min 5:** alle haben Sektion 1 ausgefüllt? Wer noch nicht: kurz hören warum. Häufigster Grund: niemand hat eine Aufgabe mitgebracht. Backup-Szenarien anbieten.
- **Min 20:** Sektion 2 läuft? Wer noch nicht: hat der Hypothesengenerator-Prompt funktioniert? Häufigste Stolperstellen siehe unten.
- **Min 40:** Übergang zu Sektion 3. Kurz vorführen, wie der Lernende-Simulator-Prompt aussieht. Wer das LLM in dieser Rolle noch nicht gesehen hat: eine Minute Live-Demo am eigenen Laptop, projiziert.
- **Min 40:** Paar-Bildung ankündigen. Cross-discipline. Wer keine Partnerin aus ferner Disziplin findet: paar mit der nächstgelegenen.
- **Min 55:** Wrap. Spec speichern lassen (Markdown-Datei oder Zwischenablage). Vorschau auf Block 3: euer Spec wird in einem Werkzeug landen.

## Häufige Stolperstellen und Redirects

### Sektion 2 (Hypothesengenerator)

**"Das LLM liefert nur generische Punkte."** Häufig, wenn die Aufgabenstellung zu kurz ist. Frage: hat die Teilnehmende auch die Musterlösung mitgegeben? Ohne Lösungsweg hat das LLM nichts, woran es Schritte enumerieren kann.

**"Das LLM listet zwanzig Punkte, ich bin überfordert."** Erwartet. Botschaft: nicht alle behalten. Pro Punkt entscheiden behalten / korrigieren / verwerfen. Vier bis acht Einträge im Spec reichen.

**"Das LLM verwendet Begriffe, die in meinem Kurs nicht vorkommen."** Streichen. Das LLM hat aus seinem Trainingsmaterial andere Fachtraditionen gemischt. Behalten was passt, der Rest weg.

**"Das LLM hat etwas Wichtiges nicht erkannt."** Die Lehrperson ergänzt aus Erfahrung. Diese Ergänzung mit **B (beobachtet)** markieren — sie kommt aus der eigenen Lehrerfahrung, nicht aus dem LLM.

### Sektion 3 (Lernende-Simulator)

**"Die simulierte Antwort wirkt zu glatt."** Ist sie meistens. Die Misconception ist im Prompt zu allgemein formuliert. Helfen, sie spezifischer in Ich-Form zu schreiben (siehe Beispiele im [system-prompt-template.md](../workshop/spec-sheet-template/system-prompt-template.md)).

**"Die simulierte Antwort ist genau das, was meine Lernenden auch schreiben."** Gut. Die intuitive Grundlage der Misconception in Sektion 3 ausformulieren: *woher* kommt diese Sichtweise plausibel?

**"Ich habe keine Idee für eine Misconception."** Drei Auslöser: (1) Was korrigierst du regelmässig falsch? (2) Welche Stellen in der letzten Klausur haben dich überrascht? (3) Welche Frage hörst du immer wieder im Tutorat?

### Paar-Review

**Das Paar findet nichts.** Häufig wenn die Disziplinen zu nah sind. Versuchen, ein anderes Paar zu finden, oder die Aussenstehende gezielt fragen: "Welcher Eintrag ist mir als jemand, der das Fach nicht kennt, *nicht* verständlich?"

**Das Paar will umschreiben statt notieren.** Stoppen. Notieren reicht. Die Überarbeitung passiert zuhause oder in Block 3, wenn das Spec gegen das Werkzeug getestet wird.

## Typische Fragen aus dem Plenum

- *"Wieviele Einträge müssen in Sektion 2?"* — Vier bis acht. Mehr als acht wird unscharf, weniger als vier deckt die Aufgabe selten ab.
- *"Muss ich für jede Misconception einen Lernende-Simulator-Lauf machen?"* — Nicht zwingend. Manche Misconceptions kennst du aus eigener Erfahrung gut genug, dass du sie direkt schreiben kannst.
- *"Was ist mit Kompetenzen, die ich nicht selbst erkenne, aber das LLM auch nicht?"* — Genau das fängt die cross-discipline Paar-Review. Sie ist die zweite externe Perspektive nach dem LLM.

## Wenn das LLM nicht funktioniert

**Microsoft Copilot ist blockiert.** Backup: HuggingChat ohne Login. Funktioniert oft, kann aber langsam sein.

**Das LLM antwortet auf Englisch, obwohl der Prompt deutsch ist.** Im Prompt ergänzen: "Antworte ausschliesslich auf Deutsch."

**Die Teilnehmende hat kein LLM-Konto.** Eine Workshop-Leitung-Lizenz teilen oder zur Sitznachbarin setzen.

## Take-away Satz für Block 2

> Du hast ein erstes vollständiges Spec für deine Teilaufgabe. Es ist noch unscharf an manchen Stellen; das ist normal. In Block 3 sehen wir, wie das Werkzeug deinem Spec begegnet und an welchen Stellen es nachfragt.

Direkt in Block 3 überleiten.
