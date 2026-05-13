---
title: "Facilitator Notes: Block 3 (Spec im laufenden Werkzeug)"
draft: true
---

Internes Dokument für die Workshop-Leitung. Ergänzt die in-page Moderationshinweise in [Block 3](../workshop/block-3-multi-tool/index.qmd).

## Zeitbudget (45 min)

| Min | Phase | Aktivität |
|-----|-------|-----------|
| 0:00-0:05 | Demo | Werkzeug am Beispiel-Spec vorführen |
| 0:05-0:20 | Eigenes Spec einfügen | Teilnehmende kopieren ihr Spec ins Werkzeug, beobachten Output |
| 0:20-0:30 | Spec schärfen | Eine Iteration mit veränderter Spec, Vergleich der Outputs |
| 0:30-0:40 | Cross-discipline Role-Play | Paare aus Block 2; B spielt Lernende, A beobachtet Werkzeug-Reaktion |
| 0:40-0:45 | Wrap | Eine Runde "welche Schärfung wirkt am stärksten?" |

## Vor dem Block

**Werkzeug-Verfügbarkeit prüfen.** [Das Werkzeug](../workshop/block-3-multi-tool/tool.qmd) ist eine HuggingFace Space mit einer Anthropic-API-Anbindung. Bekannte Ausfallpunkte: HF Down, Anthropic API quota, Cold-start-Latenz. Vor dem Workshop kurz testen.

**Backup-Plan.** Falls das Werkzeug nicht erreichbar ist:

- Lokales `marimo run` als persönliches Fallback der Workshop-Leitung (vorab installiert).
- Screenshots aus einer Voraufnahme der Demo zum Vorzeigen.
- Cross-discipline Role-Play kann ohne Werkzeug stattfinden: A liest selbst das eigene Spec und entscheidet, welcher Eintrag B's Antwort adressieren würde.

## Eröffnung Block 3

> Du hast in Block 2 ein Spec gebaut. Jetzt sehen wir, wie ein Werkzeug damit umgeht. Wichtig: das Werkzeug ist nicht der Punkt. Der Punkt ist, dass du erkennst, wo dein Spec scharf genug ist und wo nicht.

Direkt in die Demo.

## Demo-Walkthrough (5 min)

1. [Das Werkzeug](../workshop/block-3-multi-tool/tool.qmd) öffnen.
2. Das [Beispiel-Spec zur Multiple Regression](../workshop/spec-sheet-template/example-multiple-regression.md) einfügen.
3. P(know)-Slider auf 0.3 setzen (eine Lernende, die das Material teilweise beherrscht).
4. "Hint generieren" klicken.
5. Den strukturierten Output zeigen: Hinweis, Begründung, nächster Schritt, metakognitive Frage.

Botschaft: dein Spec geht oben rein, eine kalibrierte Antwort kommt unten raus. Nicht auf die Pydantic-Architektur eingehen; die ist im [Take-Home dokumentiert](../workshop/take-home/api-werkzeug-erklaert.qmd).

## Häufige Stolperstellen und Redirects

### Eigenes Spec einfügen

**"Der Output ist generisch."** Spec war zu vage. Frage: welche Sektion wirkt unscharf? Meistens Sektion 2 (Skills/Knowledge zu allgemein formuliert) oder Sektion 3 (Misconception ohne intuitive Grundlage).

**"Der Output adressiert das Falsche."** Spec hat eine wichtige Komponente nicht enthalten. Lass die Teilnehmende benennen, was sie *vermutet*: was die Lernende eigentlich brauchen würde. Dieses fehlende Element in Sektion 2 ergänzen.

**"Der Output erfindet etwas."** Das Werkzeug interpoliert. Das Spec gibt nicht genug Constraints. Lass die Teilnehmende eine Verbot-Klausel formulieren: "antworte nicht zu Thema X."

**"Der Output ist auf Englisch."** Den Spec-Header ergänzen mit "Antworte ausschliesslich auf Deutsch."

### Spec-Schärfen

**Die Teilnehmende ist zögerlich, das Spec zu ändern.** Häufig bei perfektionistischen Teilnehmenden. Erlaubnis geben: "ändere nur einen Eintrag, nicht das ganze Spec. Eine Hypothese pro Iteration."

**Die zweite Iteration bringt keine sichtbare Veränderung.** Möglich. Bedeutet, dass die Schärfung zu klein war oder am falschen Eintrag passierte. Frage zurück: welcher Eintrag schien beim ersten Lauf am vagstent zu sein? An *dem* arbeiten.

### Cross-discipline Role-Play

**Das Paar weiss nicht, wie man Lernende spielt.** Eine Karte vor sich legen lassen ([role-play-cards.qmd](../workshop/block-3-multi-tool/role-play-cards.qmd)), eine Misconception aussuchen, in Ich-Form formulieren, dann mit der Spec-Antwort reagieren.

**B's "Lernende" bricht sofort aus der Rolle.** Häufig wenn die Misconception zu fremd ist. Eine andere Karte oder eine spezifischere Misconception wählen. Im Notfall: A liest ihre eigene Misconception laut vor und B übernimmt sie wörtlich.

## Typische Fragen aus dem Plenum

- *"Kann ich das Werkzeug nach dem Workshop weiter verwenden?"* — Ja. Die URL bleibt stabil. Im [Take-Home](../workshop/take-home/index.qmd) verlinkt.
- *"Was passiert mit meinen Daten?"* — Der Spec geht an die Anthropic-API; die Eingabe wird nicht zur Modellverbesserung verwendet (Anthropic-Policy für API-Aufrufe). Aber keine personenbezogenen Lernenden-Daten einfügen.
- *"Kann ich das Werkzeug auch mit OpenAI laufen lassen?"* — Ja, der Code ist offen. Erklärt im [Take-Home: Wie das Werkzeug funktioniert](../workshop/take-home/api-werkzeug-erklaert.qmd).

## Wenn das Werkzeug ausfällt

Sofortige Ansage:

> Das Werkzeug ist gerade nicht erreichbar. Das ist genau der Vorteil eines Specs: es lebt unabhängig vom Werkzeug. Wir machen den Block leicht abgewandelt.

Dann: Cross-discipline Role-Play OHNE das Werkzeug. A liest das eigene Spec laut vor, B spielt die Lernende, A entscheidet aus dem Spec, welcher Eintrag B's Antwort fangen würde. Das ist substantiell dieselbe Erfahrung wie mit dem Werkzeug.

## Take-away Satz für Block 3

> Du hast erlebt, dass die Qualität des Werkzeug-Outputs eine Funktion der Qualität deines Specs ist. Wo dein Spec scharf war, war der Output spezifisch. Im Closing ziehen wir die Verallgemeinerung: dasselbe Spec kann verschiedene Werkzeuge treiben, das Spec ist der dauerhafte Teil.

Direkt ins Closing überleiten.
