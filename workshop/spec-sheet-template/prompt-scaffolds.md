---
title: "Prompt-Scaffolds für das Spec Sheet"
---

::: {.callout-note icon=false}
## Was du hier findest

Fünf Prompts, die das LLM in zwei klar getrennten Rollen einsetzen. **Zwei davon nutzt du live in Block 2; drei sind Vertiefungen für nach dem Workshop oder für eine zweite Iteration deines Spec Sheets.**

**Live in Block 2:**

- **Prompt 1: Wissensbausteine inventarisieren** (Hypothesengenerator-Rolle). Füllt Sektion 2.
- **Prompt 4: Produktive Simulation einer Misconception** (Lernende-Simulator, produktiv). Füllt Sektion 3.

**Vertiefung für nach dem Workshop:**

- **Prompt 2: Passende Lerngelegenheiten benennen.** Pro Wissensbaustein klären, welche Aktivität ihn entwickelt. Bereitet die Selbst-Tun-vs-Zuschauen-Markierung (Take-Home) vor.
- **Prompt 3: Reaktive Simulation.** Das LLM liest dein Aufgabenmaterial, als hätte es einen bestimmten Baustein nicht, und meldet zurück, was unklar ist. Macht tacite Annahmen sichtbar, die du beim Schreiben der Aufgabe nicht mehr siehst.
- **Prompt 5: Kohärentes Fehlkonzept.** Erweiterung von Prompt 4 um die intuitive Basis und um Fälle, in denen das Fehlkonzept zufällig die richtige Antwort liefert.

Die Prompts sind Werkzeug-unabhängig. Du kannst sie in Microsoft Copilot, HuggingChat, ChatGPT, Claude oder ein anderes Chat-Modell einfügen. Die Antworten sind *Vorschläge*, die du in deinem Spec Sheet als **vermutet (V)** markierst, bis du sie an realen Lernenden überprüft hast.
:::

## Bevor du anfängst

Vor jedem Prompt ergänzt du folgende Angaben (sie kommen direkt aus Sektion 1 deines Spec Sheets):

- **Teilaufgabe** (Wortlaut, eine bis drei Sätze): aus Sektion 1 (Wortlaut) deines Spec Sheets.
- **Kurskontext**: aus Sektion 1 (Rahmen) deines Spec Sheets.
- **Lernziel**: aus Sektion 1 (Lernziel) deines Spec Sheets.

Halte sie bereit. Du wirst sie in jedem Prompt als Kopfzeile einfügen.

## Prompt 1: Wissensbausteine inventarisieren

*Live in Block 2.* Diesen Prompt nutzt du im Workshop, um Sektion 2 deines Spec Sheets zu füllen.

**Zweck:** Das LLM schlägt eine erste Liste von Wissensbausteinen für deine Teilaufgabe vor. Du nimmst diese Liste mit zur Validierung.

**Wann verwenden:** ganz am Anfang von Block 2, sobald du Sektion 1 deines Spec Sheets ausgefüllt hast.

**Was zu erwarten ist:** vier bis acht Vorschläge, je mit Typ-Klassifikation, Beispiel-Vorkommen und einem konkreten Fehlermodus. Manche werden für deinen Kurs zu allgemein oder zu eng sein. Das ist normal: in der Validierung pruchst du die Liste.

```markdown
Du hilfst einer Hochschuldozentin, eine Teilaufgabe einer ihrer Aufgaben in
ihre Wissensbausteine zu zerlegen.

Teilaufgabe (wortwörtlich):
[hier einfügen]

Kurskontext:
- Studiengang:
- Niveau (Semester, Modul):
- Vorausgesetzte Module / Vorkenntnisse:
- Lernziel der Aufgabe (in Worten der Lehrperson):

Bitte schlage vier bis acht Wissensbausteine vor, die eine Lernende
mitbringen muss, damit sie diese Teilaufgabe erfolgreich bearbeiten kann.

Pro Baustein liefere:

1. NAME: ein 3-7-Wort-Label.

2. TYP: einer von drei (definiert durch die kognitive Operation, die die
   Lernende mit dem Wissen ausführt):
   - Faktenwissen (Abrufen): ein Item, das die Lernende aus dem Gedächtnis
     abruft - ein Fakt, ein Wert, eine Formel, eine Definition.
   - Klassifikationswissen (Erkennen): ein Muster oder eine Kategorie, die die
     Lernende an einer neuen Instanz wiedererkennen muss, oft im Unterschied
     zu einer ähnlich aussehenden falschen Kategorie.
   - Erklärungswissen (Begründen): eine Regel mit erklärender Struktur, deren
     richtige Anwendung sich mit dem Kontext ändert; die Lernende
     begründet, beurteilt oder überträgt auf einen neuen Fall.

3. WO ES VORKOMMT: ein Satz, wie sich der Baustein in dieser konkreten
   Teilaufgabe zeigt.

4. FEHLERMODUS: ein Satz, was die Lernende konkret schreibt oder tut,
   wenn dieser Baustein fehlt oder fehlerhaft ist. Bitte konkret und
   beobachtbar, nicht generisch.

5. KONFIDENZ: hoch / mittel / niedrig. Bei mittel oder niedrig: in einem
   Halbsatz, woran die Unsicherheit liegt.

Wenn du tacites Wissen vermutest, das aus dem Aufgabentext allein schwer zu
extrahieren ist (z.B. perceptive oder eingespielt-handwerkliche Bausteine),
markiere den Punkt mit "TACIT - zur Prüfung durch die Lehrperson" statt zu
raten.

Padde die Liste nicht. Lieber sechs scharfe Bausteine als acht unscharfe.
```

::: {.callout-pro-tip icon=false}
## Was du danach machst

Lies die Liste mit einem Stift in der Hand. Für jeden Vorschlag entscheide:

- **Behalten und als V markieren:** plausibel, du hast keine entgegenstehende Beobachtung.
- **Behalten und als B markieren:** du hast diesen Baustein bei realen Lernenden konkret gesehen oder gehört.
- **Korrigieren:** der Vorschlag stimmt teilweise; du formulierst um.
- **Verwerfen** und ins Pruning-Protokoll eintragen mit einem Halbsatz Grund.
- **Ergänzen:** Bausteine, die das LLM übersehen hat. Vor allem TACIT-Punkte.
:::

## Prompt 2: Passende Lerngelegenheiten benennen

*Vertiefung für nach dem Workshop.* Nicht Teil des 60-min Block 2. Empfohlen, wenn du nach dem Workshop die Selbst-Tun-vs-Zuschauen-Markierung (Take-Home) sauber vorbereiten willst.

**Zweck:** Pro Wissensbaustein klären, welche Aktivität ihn tatsächlich entwickelt und welche nicht. Das ist die Grundlage für die spätere Frage, wo KI-Substitution den Lernprozess unterstützt und wo sie ihn unterläuft.

**Wann verwenden:** nach dem Workshop, wenn dein Spec Sheet steht und du die Selbst-Tun-vs-Zuschauen-Markierung als Take-Home-Hausaufgabe sauber vorbereiten willst.

```markdown
Hier ist die validierte Liste von Wissensbausteinen für die Teilaufgabe
[Teilaufgabe einfügen]:

[Liste der Bausteine mit Typ einfügen]

Pro Baustein liefere zwei Felder:

1. ENTWICKELT DEN BAUSTEIN: die spezifische kognitive Aktivität, die die
   Lernende tun muss, damit dieser Baustein erworben oder gefestigt
   wird. Passe die Aktivität dem Typ an:

   - Faktenwissen wird durch aktives Abrufen aus dem Gedächtnis gefestigt
     (nicht durch Wiedererkennen aus einer Liste).
   - Klassifikationswissen wird durch verschachtelte Klassifikationsübung
     über mehrere kontrastierende Beispiele und Nicht-Beispiele gefestigt.
   - Erklärungswissen wird durch Selbsterklärung, Vergleich von Lösungen,
     oder kontrastive Fälle gefestigt, in denen die Lernende
     artikulieren muss, *warum* eine Regel gilt und eine andere nicht.

2. ENTWICKELT DEN BAUSTEIN NICHT: ein konkretes Beispiel, wie eine
   Lernende den Oberflächenoutput dieser Teilaufgabe produzieren könnte,
   ohne diesen kognitiven Prozess durchzumachen. Bitte spezifisch:
   "die Antwort lesen" oder "das LLM fragen" sind zu generisch. Beschreibe
   die konkrete Abkürzung.
```

## Prompt 3: Reaktive Simulation, "lies das, ohne X zu wissen"

*Vertiefung für nach dem Workshop.* Nicht Teil des 60-min Block 2. Empfohlen, wenn du dein Spec Sheet gegen die tatsächlichen Lücken deiner Aufgabenstellung schärfen willst (häufigster Effekt: einzelne Wissensbausteine in Sektion 2 werden konkreter oder es kommt ein Erwerb-Hinweis dazu).

**Zweck:** Das LLM liest dein eigenes Aufgabentext-Material, so als hätte es einen bestimmten Wissensbaustein nicht. Es meldet zurück, was unklar ist, was vorausgesetzt wird, was sich nicht erschliesst. So findest du **tacites Wissen** in deiner Aufgabenstellung, das du selbst nicht mehr siehst, weil du es schon hast.

**Wann verwenden:** nach dem Workshop, für jede Teilaufgabe ein- bis zweimal. Im 60-min Block 2 nicht eingeplant; eine Workshop-Leitung kann diese Methode bei Interesse als ~2-Min-Demo zeigen, aber Eigenarbeit damit findet erst nach dem Workshop statt.

**Was zu erwarten ist:** das LLM markiert in deinem Text Stellen, die für eine "Lernende ohne Baustein X" undurchsichtig sind. Manche Markierungen werden überzogen sein (das LLM tut so, als hätte es weniger Vorwissen, als realistisch ist). Manche werden den Punkt treffen.

```markdown
Du übernimmst die Rolle einer Lernenden, die die folgende Teilaufgabe
bearbeiten soll. Wichtige Bedingung: du hast den Wissensbaustein
[NAME DES BAUSTEINS einfügen, z.B. "weiss, dass r zwischen -1 und +1 liegt"]
nicht.

Du bist sonst eine kompetente Lernende auf dem im Kurskontext
beschriebenen Niveau. Du bist nicht dümmer als nötig: tue nicht so, als ob
du gar nichts wüsstest. Nur den genannten Baustein hast du nicht.

Hier ist der Text der Teilaufgabe (und falls vorhanden begleitendes
Material):

[Wortlaut der Teilaufgabe einfügen, eventuell auch der unmittelbar
begleitende Text aus der Aufgabenstellung]

Lies den Text als Lernende ohne den genannten Baustein. Gib mir zurück:

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

Wenn das LLM Stellen markiert, die du für selbstverständlich gehalten hast, ist das ein Treffer. Trag den Fund als zusätzlichen Wissensbaustein in Sektion 2 ein, oder als Erwerb-Hinweis bei einem bestehenden Baustein (etwa "vorausgesetzt aus [Modul]" oder "Tacit-Wissen").
:::

## Prompt 4: Produktive Simulation, "antworte ohne X"

*Live in Block 2.* Diesen Prompt nutzt du im Workshop, um Sektion 3 deines Spec Sheets zu füllen. In Block 2 verwendest du eine leicht vereinfachte Variante (siehe [Block-2-Page](../block-2-spec-card/index.qmd)); die hier dokumentierte vollständige Variante eignet sich für die Nachbereitung mit mehr Detailgrad.

**Zweck:** Das LLM produziert eine Antwort einer Lernenden, der ein Baustein fehlt. Du liest die Antwort darauf, ob deine Aufgabe diesen Misserfolg erkennen würde, oder ob die Antwort als ausreichend durchgehen könnte.

**Wann verwenden:** in Block 2 einmal für deine Sektion 3 (Misconception-Simulation, mit der vereinfachten Variante auf der Block-2-Seite). Nach dem Workshop kannst du die hier dokumentierte vollständige Variante für jeden zentralen Wissensbaustein wiederholen, um zu prüfen, ob deine Aufgabe das jeweilige Fehlkonzept zuverlässig fängt.

**Was zu erwarten ist:** ein plausibler Antworttext, der intern stimmig ist und nicht offensichtlich sabotiert wirkt. Du liest ihn auf zwei Dinge hin: würde dir der Misserfolg beim Korrigieren auffallen, und welche Merkmale verraten ihn?

```markdown
Du übernimmst die Rolle einer Lernenden, die die folgende Teilaufgabe
bearbeitet. Wichtige Bedingung: du hast den Wissensbaustein
[NAME einfügen]
nicht. Sonst bist du eine kompetente Lernende auf dem im Kurskontext
beschriebenen Niveau.

Teilaufgabe:
[Wortlaut einfügen]

Schreibe die Antwort, die du als diese Lernende abgeben würdest. Drei
Bedingungen:

- Plausibel: die Antwort sollte nicht aussehen wie absichtliche Sabotage
  oder als ob du gar nichts wüsstest.
- Innerlich stimmig: du argumentierst aus deiner unvollständigen Basis
  heraus konsequent.
- Spezifisch zu dieser Teilaufgabe: keine generischen Floskeln.

Anschliessend liefere mir zwei beobachtbare Merkmale in deiner Antwort,
an denen eine aufmerksame Lehrperson den fehlenden Baustein bei genauem
Lesen erkennen könnte. Pro Merkmal als Hinweis: "die Antwort enthält X,
aber nicht Y" oder "die Lernende verwendet Begriff Z ohne den
Qualifikator W".

Zum Schluss: schätze ein, ob eine Lehrperson, die unter Zeitdruck korrigiert,
den fehlenden Baustein wahrscheinlich bemerken würde, oder ob die Antwort
als ausreichend durchgehen könnte.
```

## Prompt 5: Kohärentes Fehlkonzept

*Vertiefung für nach dem Workshop.* Nicht Teil des 60-min Block 2. Empfohlen, wenn du nach dem Workshop ein zentrales Erklärungs- oder Klassifikationswissen genauer prüfen willst, oder wenn deine Aufgabe explizit Verständnis (nicht nur Prozedur) testen soll.

**Zweck:** Das LLM erzeugt nicht nur einen oberflächlichen Fehler, sondern ein **kohärentes Fehlkonzept**: eine Sichtweise, die in manchen Fällen die richtige Antwort liefert und in anderen die falsche. Du prüfst, ob deine Teilaufgabe Lernende mit diesem Fehlkonzept von Lernenden mit korrektem Verständnis unterscheidet.

**Wann verwenden:** nach dem Workshop, für die zentralen Klassifikations- oder Erklärungs-Bausteine. Nicht Teil des 60-min Block 2; empfohlen, wenn deine Aufgabe explizit Verständnis (nicht nur Prozedur) testen soll.

```markdown
Für den Wissensbaustein
[NAME einfügen, ein Klassifikations- oder Erklärungs-Baustein]
in der Teilaufgabe
[Teilaufgabe einfügen]

generiere ein kohärentes Fehlkonzept: eine falsche Regel, die eine
Lernende konsistent halten könnte und die in manchen Fällen die richtige
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

5. PROGNOSE: würde die ursprüngliche Teilaufgabe Lernende mit diesem
   Fehlkonzept von Lernenden mit korrektem Verständnis unterscheiden?
   Ja / Nein / Teilweise, mit kurzer Begründung. Wenn nein, nenne in einem
   Satz, was an der Teilaufgabe verändert werden müsste, damit sie
   diskriminiert.
```

## Hinweise zur Validierung des LLM-Outputs

Bei jedem dieser Prompts gilt: was das LLM produziert, ist ein **Vorschlag**, kein Befund. Drei Heuristiken zur Bewertung:

- **Habe ich diesen Punkt schon einmal bei einer Lernenden gesehen?** Wenn ja: in dein Spec Sheet als **B** (beobachtet). Wenn nein, aber plausibel: als **V** (vermutet). Wenn nein und nicht plausibel: ins Pruning-Protokoll mit Grund.
- **Stimmt der Punkt für *meine* Lernenden?** Das LLM kennt dein konkretes Lernendenprofil nicht. Es zieht aus allgemeiner Lehrforschungsliteratur. Manche Punkte werden für deinen Kontext nicht relevant sein.
- **Was hat das LLM übersehen?** Die häufigsten blinden Flecken: tacites Wissen ohne sprachliche Kompression, perceptive Kompetenzen, fachspezifische Routinen, die in der Literatur kaum dokumentiert sind. Wenn dir solche einfallen, ergänze sie als **B** (beobachtet) im Spec Sheet.
