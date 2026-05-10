---
title: "Tier 4: Coding-Agent (Walkthrough-Skript)"
---

::: {.callout-note icon=false}
Das Skript für die Tier-4-Demo (10 min). Die Lehrperson zeigt, wie ein Coding-Agent eine Spec Card als Datei lädt und die Diagnose programmatisch laufen lässt, einschliesslich Iteration und Batch-Auswertung.
:::

## Werkzeug-Auswahl

Zwei Optionen, beide gut für die Demo:

- **Claude Code** (CLI-Tool von Anthropic, lokal installierbar): zeigt agentisches Verhalten in einer Terminal-Umgebung. Klar lesbar, gut für Demonstration.
- **pi.dev** ([pi.dev](https://pi.dev/)): browserbasierter Coding-Agent, läuft ohne lokale Installation. Zugänglicher für Teilnehmende, die keine CLI-Erfahrung haben.

Wähle eines aus. In der Workshop-Materialien wird das gewählte Tool als Standard genannt; das andere wird als Alternative verlinkt.

## Vorbereitung der Demo

Vorbereitete Dateien im Demo-Verzeichnis:

- `spec-card.md`: die Spec Card der Statistik-Novizin (oder eine andere kompakte Spec Card aus dem Workshop)
- `models.py`: Pydantic-Schema (kopiert aus `hf-spaces/diagnostic-tool-shell/`)
- `scenarios.json`: die sechs Szenarien
- `.env` mit `ANTHROPIC_API_KEY` (nicht ins Repo committen)

## Walkthrough-Skript

### Schritt 1: Den Agent öffnen, die Spec Card zeigen (1 min)

"Hier ist die Spec Card, die wir in Block 2 gebaut haben, als Markdown-Datei. Der Coding-Agent hat Zugriff auf diese Datei und auf das `models.py`-Schema."

Demo-Aktion: `cat spec-card.md` (oder den Inhalt im Editor zeigen). Kurz auf die Sektionen verweisen.

### Schritt 2: Erste Aufgabe an den Agent (3 min)

Aufgabe an den Agent (genau so eingeben):

> "Lies `spec-card.md` und `models.py`. Schreibe ein Python-Skript `diagnose.py`, das eine einzelne Studierendenantwort entgegennimmt, die Spec Card als System-Prompt verwendet, das Anthropic-Tool-Use-API aufruft mit `models.DiagnosticResult` als Schema, und das validierte Ergebnis ausgibt. Teste das Skript dann auf der ersten kalibrierten Antwort von Szenario `nursing-pharmacology` aus `scenarios.json`."

Demo-Aktion: dem Agent zuschauen, wie er:

- die Dateien liest
- das Skript schreibt
- es ausführt
- das Ergebnis ausgibt

Kommentar: "Beachtet, dass der Agent das tut, was wir in Block 3 als Tier 3 gesehen haben, aber autonom: er schreibt den Code selbst, statt dass wir ihn vorschreiben."

### Schritt 3: Iteration (3 min)

Wenn das erste Ergebnis nicht plausibel ist (oder selbst wenn doch), Folgeaufgabe:

> "Lass denselben Code über alle drei kalibrierten Antworten von `nursing-pharmacology` laufen. Vergleiche die Diagnosen: für jede Antwort, schreibe in eine Tabelle, was der Tag in `scenarios.json` ist und was die Diagnose tatsächlich war. Sind sie konsistent?"

Demo-Aktion: Agent erweitert das Skript, lässt es laufen, liefert eine Tabelle.

Kommentar: "Das ist Batch-Diagnose. Ein Chat-Tool kann das auch, aber es ist mühsam: Antwort kopieren, einfügen, Antwort kopieren, einfügen. Der Agent macht es in einem Aufruf."

### Schritt 4: Spec-Iteration (2 min)

Wenn die Diagnose abweicht von den kalibrierten Tags, Folgeaufgabe:

> "Die Antwort C wurde als `schema_gap` getaggt, aber das Modell hat sie als `germane_disengagement` klassifiziert. Vorschlag, was in der Spec Card geändert werden könnte, damit die Unterscheidung schärfer wird. Schlag eine konkrete Änderung in `spec-card.md` vor."

Demo-Aktion: Agent liest die Spec Card erneut, identifiziert die problematische Stelle, schlägt eine Formulierung vor.

Kommentar: "Das ist der Punkt, an dem das Werkzeug die Spec Card *zurückspielt*: aus dem Misstand des Tools lernst du etwas darüber, wo deine Spezifikation lückenhaft war."

### Schritt 5: Ausstieg (1 min)

"Was wir in Tier 4 gesehen haben: derselbe Inhalt wie Tier 3, aber agentisch. Der Agent kann iterieren, batchen, vorschläge zur Spec Card machen. Das ist die Klasse von Werkzeug, die produktive Zusammenarbeit zwischen Lehrperson und KI ermöglicht, weil die KI Code schreiben und ausführen kann, nicht nur Texte produzieren."

## Worauf in der Demo zu achten ist

- Der Agent verwendet die Spec Card als *Datei*, nicht als Prompt. Das macht die Spec Card zu einem versionierbaren, teilbaren Artefakt: anders als ein Prompt, der in einem Chat-Fenster lebt und beim Schliessen verloren geht.
- Wenn der Agent etwas falsch macht (er schreibt das Schema falsch oder nutzt einen falschen Endpunkt), kannst du es beobachtbar korrigieren. Anders als bei Tier 1 oder 2 kannst du den Code nachvollziehen.
- Der Agent kann auch *etwas anderes* mit der Spec Card tun, was die anderen Tiers nicht können: zum Beispiel eine Roundtrip-Validierung schreiben (Spec Card → Test-Skript → Vergleich mit kalibrierten Tags → Vorschlag zur Spec-Verbesserung). Das ist die Klasse von Werkzeug, die langfristig die Spec-Card-Methode am stärksten unterstützt.

## Falls die Demo schiefgeht

Backup: das Tier-3-Notebook (Marimo) ist immer verfügbar. Wenn der Coding-Agent crashed oder die API-Antwort schlecht ausfällt, fällt die Demo auf das Marimo-Notebook zurück, das vorher schon gezeigt wurde. Zeit-Budget der Demo: 10 min, mit hartem Cut-off, damit der abschliessende Diskussionsblock erhalten bleibt.
