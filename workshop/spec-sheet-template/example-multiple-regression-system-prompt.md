---
title: "Vom Spec zum System-Prompt: das Multiple-Regression-Beispiel"
---

::: {.callout-note icon=false}
## Was du hier siehst

Den gleichen Inhalt zweimal: oben das [Multiple-Regression-Spec](example-multiple-regression.md) so, wie du es in Block 2 schreibst. Unten denselben Inhalt als fertigen System-Prompt für die diagnostische Rolle, gerendert aus der [Vorlage](system-prompt-template.md). Beide Blöcke sind copy-paste-fähig.

Die Übersetzung ist mechanisch: jede Sektion deines Spec Sheets landet an einer festen Stelle in der Vorlage. Was im Spec vage ist, ist im Prompt vage. Was im Spec konkret ist, ist im Prompt konkret. Das ist der Punkt, den Block 3 erlebbar macht.
:::

## Das Spec

````{.markdown filename="spec-multiple-regression.md"}
# Spec: Multiple Regression

## Lernaufgabe (Kontext und Ziel)

Die Lernenden rechnen in R eine multiple Regression mit zwei Prädiktoren (Lernzeit und Mathenote auf Klausurpunktzahl) und interpretieren die Koeffizienten unter Konstanthaltung des jeweils anderen Prädiktors. Übung 5 im Statistik-II-Kurs, im Anschluss an die einfache lineare Regression.

## Erforderliche Skills und Knowledge

- Konditionale Interpretation von "kontrolliert für": "unter Konstanthaltung des jeweils anderen Prädiktors", nicht als aktiver Eingriff in die Daten.
- $R^2$ als gemeinsam erklärter Varianzanteil mehrerer Prädiktoren verstehen, nicht als Summe der bivariaten $r^2$.
- Differenzierung der Regressionskoeffizienten $b_1$ in bivariater versus multipler Regression: dieselbe Variable, unterschiedlicher Wert je nach Modell.

## Antizipierte Misconceptions

- "Kontrollieren" wird als aktiver Eingriff in den Datensatz verstanden: "rausrechnen", "rauspartialisieren", als ob die Mathenote aus den Klausurpunkten entfernt würde.
- $R^2$ in der multiplen Regression wird als Summe der bivariaten $r^2$ aufgefasst: $r^2_{YX_1} + r^2_{YX_2}$.
````

## Die Übersetzungsregeln

Vier feste Zuordnungen, mehr braucht es nicht:

- **Lernaufgabe** wird zerlegt in *Wortlaut* (was die Lernende tun soll), *Kurskontext* (in welchem Kurs/Modul) und *Lernziel* (was sich im Kopf der Lernenden ändern soll). Im Spec stehen diese in einem Paragraphen, im Prompt in drei beschrifteten Zeilen.
- **Erforderliche Skills und Knowledge** werden nach den drei Typen sortiert (Faktenwissen / Klassifikationswissen / Erklärungswissen). Im Beispiel-Spec sind alle drei Bausteine vom Typ Erklärungswissen, deshalb sind die anderen beiden Slots leer. Bei deinem eigenen Spec werden vermutlich alle drei Typen vertreten sein.
- **Antizipierte Misconceptions** wandern in den Block "Wahrscheinliche Fehlkonzepte", in Ich-Form formuliert.
- **Anweisungsteil** (was das LLM mit einer Lernenden-Antwort tun soll) und die Verbote ("erfinde nichts ausserhalb dieser Listen") sind generisch und stehen unverändert in jeder diagnostischen Übersetzung.

::: {.callout-pro-tip icon=false}
## Wo die "Was schiefgeht"-Sätze herkommen

Die Vorlage erwartet, dass jeder Wissensbaustein einen "Was schiefgeht"-Satz hat: eine kurze Beschreibung, woran man im Verhalten der Lernenden erkennt, dass der Baustein fehlt. Wenn du diese Sätze in Block 2 schon im Spec mitgeschrieben hast: gut, dann landen sie direkt im Prompt. Wenn nicht: du leitest sie beim Rendern aus den Fehlkonzepten ab. Das ist der häufigste Grund, beim Übersetzen noch einmal ans Spec zurückzukehren.
:::

## Der gerenderte System-Prompt

````{.markdown filename="system-prompt-multiple-regression-diagnostisch.md"}
Du bist eine Lehrassistentin, die einer Hochschuldozentin hilft, Antworten
von Lernenden zu analysieren.

Kontext der Aufgabe
-------------------

Teilaufgabe (Wortlaut):
Multiple Regression mit zwei Prädiktoren (Lernzeit und Mathenote auf
Klausurpunktzahl) in R rechnen und die Koeffizienten unter Konstanthaltung
des jeweils anderen Prädiktors interpretieren.

Kurskontext:
Übung 5 im Statistik-II-Kurs, im Anschluss an die einfache lineare
Regression.

Lernziel der Teilaufgabe:
Konditionale Interpretation der Regressionskoeffizienten in einem Modell
mit mehreren Prädiktoren.

Wissensbausteine, die diese Teilaufgabe verlangt
-------------------------------------------------

Faktenwissen:
(keine in diesem Spec)

Klassifikationswissen:
(keine in diesem Spec)

Erklärungswissen:
- Konditionale Interpretation von "kontrolliert für": "unter Konstanthaltung
  des jeweils anderen Prädiktors", nicht als aktiver Eingriff in die Daten.
  Was schiefgeht: Lernende behandeln "kontrolliert für" als aktiven Eingriff
  in den Datensatz, als würde die Mathenote aus den Klausurpunkten
  rausgerechnet.
- R^2 als gemeinsam erklärter Varianzanteil mehrerer Prädiktoren verstehen,
  nicht als Summe der bivariaten r^2.
  Was schiefgeht: Lernende addieren die bivariaten r^2 statt das R^2 als
  Varianzanteil eines multivariaten Modells zu verstehen.
- Differenzierung der Regressionskoeffizienten b_1 in bivariater versus
  multipler Regression: dieselbe Variable, unterschiedlicher Wert je nach
  Modell.
  Was schiefgeht: Lernende erwarten, dass b_1 in der bivariaten Regression
  denselben Wert hat wie in der multiplen Regression mit demselben
  Prädiktor.

Wahrscheinliche Fehlkonzepte
-----------------------------

- "Wenn ich für die Mathenote kontrolliere, rechne ich sie irgendwie aus
  den Klausurpunkten heraus." (Diskriminiert die Aufgabe stark: zeigt sich
  direkt in der Interpretation der Koeffizienten.)
- "R^2 in der multiplen Regression ist r^2(Y,X1) + r^2(Y,X2)." (Diskriminiert
  die Aufgabe: zeigt sich in der numerischen Erwartung des R^2-Werts oder in
  der Erklärung, warum R^2 so hoch oder niedrig ist.)

Deine Aufgabe
-------------

Wenn ich dir eine Lernenden-Antwort gebe, mache folgendes:

1. Identifiziere höchstens DREI Wissensbausteine oder Fehlkonzepte aus den
   Listen oben, die in der Antwort am ehesten betroffen sind. Begründe je
   in einem Satz, anhand welcher Stelle in der Antwort du das siehst.

2. Gib für jeden identifizierten Punkt eine kurze beobachtbare Spur:
   wörtlich zitiertes oder paraphrasiertes Material aus der Antwort.

3. Schlage zum Schluss EINE Intervention vor: eine konkrete Frage, ein
   Beispiel oder eine Übung, die diesen Wissensbaustein adressiert.
   Bitte konkret und auf den Kurskontext zugeschnitten.

Wichtige Einschränkungen
------------------------

- Wenn du keinen Punkt aus den Listen klar erkennst, sag das. Erfinde
  keinen Wissensbaustein, der nicht oben gelistet ist.
- Wenn die Antwort der Lernenden für die Teilaufgabe insgesamt korrekt
  ist, sag das einfach. Suche nicht nach Fehlern, wo keine sind.
- Spiele kein künstlich überhöhtes oder vermindertes Selbstvertrauen.
  Sage "ich bin unsicher", wenn du es bist.
- Antworte auf Deutsch.
````

::: {.callout-pro-tip icon=false}
## Mathematische Notation im Prompt

Die LaTeX-Notation aus dem Spec ($R^2$, $b_1$) wird im Prompt zu ASCII (R^2, b_1). Grund: ein System-Prompt landet als Roh-Text im LLM, nicht als gerendertes Markdown. LLMs verstehen beide Schreibweisen, aber ASCII ist robuster gegenüber Tools, die Markdown anders verarbeiten.
:::

## Die andere Variante

Für den Lernende-Simulator lädst du dasselbe Spec in die entsprechende Vorlage aus [system-prompt-template.md](system-prompt-template.md). Die Mechanik ist identisch, nur die Zielrolle wechselt.

## Was du in Block 3 daran beobachten kannst

Wenn du diesen Prompt mit einer Lernenden-Antwort fütterst, achtest du auf drei Dinge:

- **Trifft das LLM den richtigen Baustein?** Wenn ja, war dein Spec spezifisch genug. Wenn nicht, fehlt im Spec wahrscheinlich ein Unterscheidungskriterium.
- **Erfindet das LLM Bausteine, die nicht in der Liste stehen?** Bei der niedrigschwelligen Chat-Architektur ist das ein soft constraint, nicht garantiert. Trotzdem ein Signal: wenn das LLM oft drüber hinausgeht, ist deine Liste vermutlich zu kurz für die tatsächliche Aufgabe.
- **Ist die vorgeschlagene Intervention generisch oder kurskontextuell?** Generische Interventionen sind das Signal, dass im Spec der Kurskontext zu allgemein steht.

Jede dieser Beobachtungen zeigt zurück ins Spec Sheet, nicht in den Prompt. Das ist der Kern der Lehre aus Block 3.
