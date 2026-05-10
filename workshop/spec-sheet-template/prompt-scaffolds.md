---
title: "Prompt-Scaffolds für das Spec Sheet"
---

::: {.callout-note icon=false}
## Was du hier findest

Fünf Prompts, die du in Block 2 nutzt, um dein Spec Sheet zu bauen. Jeder Prompt entspricht einer Rolle, die das LLM für dich übernimmt:

- **Hypothesengenerator** (Prompts 1 und 2): das LLM schlägt Wissensbausteine und passende Lerngelegenheiten vor.
- **Lernende-Simulator, reaktiv** (Prompt 3): das LLM liest dein Material so, als hätte es einen bestimmten Wissensbaustein nicht, und meldet zurück, was unklar ist. Die Funde fliessen als zusätzliche Bausteine oder als Erwerb-Hinweise in deine Sektion B zurück.
- **Lernende-Simulator, produktiv** (Prompts 4 und 5): das LLM produziert eine Antwort einer Studierenden, der ein Baustein fehlt oder die ein Fehlkonzept hält.

Die Prompts sind Werkzeug-unabhängig. Du kannst sie in Microsoft Copilot, HuggingChat, ChatGPT, Claude oder ein anderes Chat-Modell einfügen. Die Antworten sind dann *Vorschläge*, die du in deinem Spec Sheet als **vermutet (V)** markierst, bis du sie an realen Studierenden überprüft hast.
:::

## Bevor du anfängst

Vor jedem Prompt ergänzt du folgende Angaben (sie kommen direkt aus Sektion A deines Spec Sheets):

- **Teilaufgabe** (Wortlaut, eine bis drei Sätze): aus A1 deines Spec Sheets.
- **Kurskontext**: aus A2 deines Spec Sheets.
- **Lernziel**: aus A3 deines Spec Sheets.

Halte sie bereit. Du wirst sie in jedem Prompt als Kopfzeile einfügen.

## Prompt 1: Wissensbausteine inventarisieren

**Zweck:** Das LLM schlägt eine erste Liste von Wissensbausteinen für deine Teilaufgabe vor. Du nimmst diese Liste mit zur Validierung.

**Wann verwenden:** ganz am Anfang von Block 2, sobald du Sektion A deines Spec Sheets ausgefüllt hast.

**Was zu erwarten ist:** vier bis acht Vorschläge, je mit Typ-Klassifikation, Beispiel-Vorkommen und einem konkreten Fehlermodus. Manche werden für deinen Kurs zu allgemein oder zu eng sein. Das ist normal: in der Validierung pruchst du die Liste.

```
Du hilfst einer Hochschuldozentin, eine Teilaufgabe einer ihrer Aufgaben in
ihre Wissensbausteine zu zerlegen.

Teilaufgabe (wortwörtlich):
[hier einfügen]

Kurskontext:
- Studiengang:
- Niveau (Semester, Modul):
- Vorausgesetzte Module / Vorkenntnisse:
- Lernziel der Aufgabe (in Worten der Dozentin):

Bitte schlage vier bis acht Wissensbausteine vor, die eine Studierende
mitbringen muss, damit sie diese Teilaufgabe erfolgreich bearbeiten kann.

Pro Baustein liefere:

1. NAME: ein 3-7-Wort-Label.

2. TYP: einer von drei (definiert durch die kognitive Operation, die die
   Studierende mit dem Wissen ausführt):
   - Faktenwissen (Abrufen): ein Item, das die Studierende aus dem Gedächtnis
     abruft - ein Fakt, ein Wert, eine Formel, eine Definition.
   - Klassifikationswissen (Erkennen): ein Muster oder eine Kategorie, die die
     Studierende an einer neuen Instanz wiedererkennen muss, oft im Unterschied
     zu einer ähnlich aussehenden falschen Kategorie.
   - Erklärungswissen (Begründen): eine Regel mit erklärender Struktur, deren
     richtige Anwendung sich mit dem Kontext ändert; die Studierende
     begründet, beurteilt oder überträgt auf einen neuen Fall.

3. WO ES VORKOMMT: ein Satz, wie sich der Baustein in dieser konkreten
   Teilaufgabe zeigt.

4. FEHLERMODUS: ein Satz, was die Studierende konkret schreibt oder tut,
   wenn dieser Baustein fehlt oder fehlerhaft ist. Bitte konkret und
   beobachtbar, nicht generisch.

5. KONFIDENZ: hoch / mittel / niedrig. Bei mittel oder niedrig: in einem
   Halbsatz, woran die Unsicherheit liegt.

Wenn du tacites Wissen vermutest, das aus dem Aufgabentext allein schwer zu
extrahieren ist (z.B. perceptive oder eingespielt-handwerkliche Bausteine),
markiere den Punkt mit "TACIT - zur Prüfung durch die Dozentin" statt zu
raten.

Padde die Liste nicht. Lieber sechs scharfe Bausteine als acht unscharfe.
```

::: {.callout-pro-tip icon=false}
## Was du danach machst

Lies die Liste mit einem Stift in der Hand. Für jeden Vorschlag entscheide:

- **Behalten und als V markieren:** plausibel, du hast keine entgegenstehende Beobachtung.
- **Behalten und als B markieren:** du hast diesen Baustein bei realen Studierenden konkret gesehen oder gehört.
- **Korrigieren:** der Vorschlag stimmt teilweise; du formulierst um.
- **Verwerfen** und ins Pruning-Protokoll eintragen mit einem Halbsatz Grund.
- **Ergänzen:** Bausteine, die das LLM übersehen hat. Vor allem TACIT-Punkte.
:::

## Prompt 2: Passende Lerngelegenheiten benennen

**Zweck:** Pro Wissensbaustein klären, welche Aktivität ihn tatsächlich entwickelt und welche nicht. Das ist die Grundlage für die spätere Frage, wo KI-Substitution den Lernprozess unterstützt und wo sie ihn unterläuft.

**Wann verwenden:** nachdem du dein Inventar aus Prompt 1 validiert hast.

```
Hier ist die validierte Liste von Wissensbausteinen für die Teilaufgabe
[Teilaufgabe einfügen]:

[Liste der Bausteine mit Typ einfügen]

Pro Baustein liefere zwei Felder:

1. ENTWICKELT DEN BAUSTEIN: die spezifische kognitive Aktivität, die die
   Studierende tun muss, damit dieser Baustein erworben oder gefestigt
   wird. Passe die Aktivität dem Typ an:

   - Faktenwissen wird durch aktives Abrufen aus dem Gedächtnis gefestigt
     (nicht durch Wiedererkennen aus einer Liste).
   - Klassifikationswissen wird durch verschachtelte Klassifikationsübung
     über mehrere kontrastierende Beispiele und Nicht-Beispiele gefestigt.
   - Erklärungswissen wird durch Selbsterklärung, Vergleich von Lösungen,
     oder kontrastive Fälle gefestigt, in denen die Studierende
     artikulieren muss, *warum* eine Regel gilt und eine andere nicht.

2. ENTWICKELT DEN BAUSTEIN NICHT: ein konkretes Beispiel, wie eine
   Studierende den Oberflächenoutput dieser Teilaufgabe produzieren könnte,
   ohne diesen kognitiven Prozess durchzumachen. Bitte spezifisch:
   "die Antwort lesen" oder "das LLM fragen" sind zu generisch. Beschreibe
   die konkrete Abkürzung.
```

## Prompt 3: Reaktive Simulation, "lies das, ohne X zu wissen"

**Zweck:** Das LLM liest dein eigenes Aufgabentext-Material, so als hätte es einen bestimmten Wissensbaustein nicht. Es meldet zurück, was unklar ist, was vorausgesetzt wird, was sich nicht erschliesst. So findest du **tacites Wissen** in deiner Aufgabenstellung, das du selbst nicht mehr siehst, weil du es schon hast.

**Wann verwenden:** nachdem du dein Bausteininventar fertig hast und mindestens einen Baustein als zentral identifiziert hast. Beim Workshop ein bis zwei Mal pro Aufgabe genügen.

**Was zu erwarten ist:** das LLM markiert in deinem Text Stellen, die für eine "Lernende ohne Baustein X" undurchsichtig sind. Manche Markierungen werden überzogen sein (das LLM tut so, als hätte es weniger Vorwissen, als realistisch ist). Manche werden den Punkt treffen.

```
Du übernimmst die Rolle einer Studierenden, die die folgende Teilaufgabe
bearbeiten soll. Wichtige Bedingung: du hast den Wissensbaustein
[NAME DES BAUSTEINS einfügen, z.B. "weiss, dass r zwischen -1 und +1 liegt"]
nicht.

Du bist sonst eine kompetente Studierende auf dem im Kurskontext
beschriebenen Niveau. Du bist nicht dümmer als nötig: tue nicht so, als ob
du gar nichts wüsstest. Nur den genannten Baustein hast du nicht.

Hier ist der Text der Teilaufgabe (und falls vorhanden begleitendes
Material):

[Wortlaut der Teilaufgabe einfügen, eventuell auch der unmittelbar
begleitende Text aus der Aufgabenstellung]

Lies den Text als Studierende ohne den genannten Baustein. Gib mir zurück:

1. WAS UNKLAR IST: maximal fünf Stellen, an denen du als Lernende ins
   Stocken gerätst. Pro Stelle: das Wort, der Satz oder die Stelle, an der
   die Unklarheit auftritt, plus ein Satz, was an dieser Stelle unklar
   wird.

2. WAS DU TACIT VORAUSGESETZT SIEHST: Annahmen, die der Text macht, ohne
   sie zu nennen, und die du nicht von selbst füllen kannst, weil dir der
   Baustein fehlt.

3. WAS DU TROTZDEM NOCH KANNST: Teile der Aufgabe, die für dich auch ohne
   den Baustein bearbeitbar bleiben.

Bitte keinen Trost-Output ("die Aufgabe ist insgesamt verständlich, aber
..."). Schreibe als die Lernende, die du gerade bist.
```

::: {.callout-pro-tip icon=false}
## Was diese Probe surfacet

Die reaktive Simulation ist die methodologische Form des Fluchs des Wissens: das LLM zeigt dir, was deine Aufgabenstellung an Wissen voraussetzt, ohne es zu nennen. Das ist genau die Information, die dir selbst am schwersten zugänglich ist, weil du den Baustein längst hast.

Wenn das LLM Stellen markiert, die du für selbstverständlich gehalten hast, ist das ein Treffer. Trag den Fund als zusätzlichen Wissensbaustein in Sektion B ein, oder als Erwerb-Hinweis bei einem bestehenden Baustein (etwa "vorausgesetzt aus [Modul]" oder "Tacit-Wissen").
:::

## Prompt 4: Produktive Simulation, "antworte ohne X"

**Zweck:** Das LLM produziert eine Antwort einer Studierenden, der ein Baustein fehlt. Du liest die Antwort darauf, ob deine Aufgabe diesen Misserfolg erkennen würde, oder ob die Antwort als ausreichend durchgehen könnte.

**Wann verwenden:** für jeden zentralen Wissensbaustein einmal, oder wenn du prüfen willst, ob deine Aufgabe ein bestimmtes Fehlkonzept überhaupt fängt.

**Was zu erwarten ist:** ein plausibler Antworttext, der intern stimmig ist und nicht offensichtlich sabotiert wirkt. Du liest ihn auf zwei Dinge hin: würde dir der Misserfolg beim Korrigieren auffallen, und welche Merkmale verraten ihn?

```
Du übernimmst die Rolle einer Studierenden, die die folgende Teilaufgabe
bearbeitet. Wichtige Bedingung: du hast den Wissensbaustein
[NAME einfügen]
nicht. Sonst bist du eine kompetente Studierende auf dem im Kurskontext
beschriebenen Niveau.

Teilaufgabe:
[Wortlaut einfügen]

Schreibe die Antwort, die du als diese Studierende abgeben würdest. Drei
Bedingungen:

- Plausibel: die Antwort sollte nicht aussehen wie absichtliche Sabotage
  oder als ob du gar nichts wüsstest.
- Innerlich stimmig: du argumentierst aus deiner unvollständigen Basis
  heraus konsequent.
- Spezifisch zu dieser Teilaufgabe: keine generischen Floskeln.

Anschliessend liefere mir zwei beobachtbare Merkmale in deiner Antwort,
an denen eine aufmerksame Dozentin den fehlenden Baustein bei genauem
Lesen erkennen könnte. Pro Merkmal als Hinweis: "die Antwort enthält X,
aber nicht Y" oder "die Studierende verwendet Begriff Z ohne den
Qualifikator W".

Zum Schluss: schätze ein, ob eine Dozentin, die unter Zeitdruck korrigiert,
den fehlenden Baustein wahrscheinlich bemerken würde, oder ob die Antwort
als ausreichend durchgehen könnte.
```

## Prompt 5: Kohärentes Fehlkonzept

**Zweck:** Das LLM erzeugt nicht nur einen oberflächlichen Fehler, sondern ein **kohärentes Fehlkonzept**: eine Sichtweise, die in manchen Fällen die richtige Antwort liefert und in anderen die falsche. Du prüfst, ob deine Teilaufgabe Studierende mit diesem Fehlkonzept von Studierenden mit korrektem Verständnis unterscheidet.

**Wann verwenden:** für die zentralen Klassifikations- oder Erklärungs-Bausteine. Optional, aber wichtig für Aufgaben, die Verständnis prüfen sollen.

```
Für den Wissensbaustein
[NAME einfügen, ein Klassifikations- oder Erklärungs-Baustein]
in der Teilaufgabe
[Teilaufgabe einfügen]

generiere ein kohärentes Fehlkonzept: eine falsche Regel, die eine
Studierende konsistent halten könnte und die in manchen Fällen die richtige
Antwort liefert und in anderen die falsche. Falls möglich, nimm ein
Fehlkonzept, das in der Lehrforschung tatsächlich dokumentiert ist; sonst
ein plausibles.

Bitte ergänze auch ein Fehlkonzept, das aus einer **kohärenten
Alltagsintuition** stammt, nicht nur aus einer falsch gelernten Formel. Die
intuitive Basis ist der Grund, warum solche Fehlkonzepte widerständig sind
und sich nicht durch bessere Erklärungen wegerklären lassen.

Pro Fehlkonzept liefere:

1. WIE DIE STUDIERENDE ES SAGEN WÜRDE: ein bis zwei Sätze in Ich-Form.

2. INTUITIVE BASIS: die Alltagsintuition oder Übergeneralisierung, die das
   Fehlkonzept richtig anfühlen lässt.

3. EIN FALL, IN DEM DAS FEHLKONZEPT DIE RICHTIGE ANTWORT LIEFERT:
   konkrete Aufgabensituation.

4. EIN FALL, IN DEM ES DIE FALSCHE LIEFERT: konkrete Aufgabensituation.

5. PROGNOSE: würde die ursprüngliche Teilaufgabe Studierende mit diesem
   Fehlkonzept von Studierenden mit korrektem Verständnis unterscheiden?
   Ja / Nein / Teilweise, mit kurzer Begründung. Wenn nein, nenne in einem
   Satz, was an der Teilaufgabe verändert werden müsste, damit sie
   diskriminiert.
```

## Hinweise zur Validierung des LLM-Outputs

Bei jedem dieser Prompts gilt: was das LLM produziert, ist ein **Vorschlag**, kein Befund. Drei Heuristiken zur Bewertung:

- **Habe ich diesen Punkt schon einmal bei einer Studierenden gesehen?** Wenn ja: in dein Spec Sheet als **B** (beobachtet). Wenn nein, aber plausibel: als **V** (vermutet). Wenn nein und nicht plausibel: ins Pruning-Protokoll mit Grund.
- **Stimmt der Punkt für *meine* Studierenden?** Das LLM kennt dein konkretes Studierendenprofil nicht. Es zieht aus allgemeiner Lehrforschungsliteratur. Manche Punkte werden für deinen Kontext nicht relevant sein.
- **Was hat das LLM übersehen?** Die häufigsten blinden Flecken: tacites Wissen ohne sprachliche Kompression, perceptive Kompetenzen, fachspezifische Routinen, die in der Literatur kaum dokumentiert sind. Wenn dir solche einfallen, ergänze sie als **B** (beobachtet) im Spec Sheet.
