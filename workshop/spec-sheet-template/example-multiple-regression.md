---
title: "Beispiel-Spec: Multiple Regression"
---

Ein knappes Beispiel-Spec zur Übung "Multiple Regression mit zwei Prädiktoren" aus Block 1. Du siehst es als Markdown-Quelltext, damit du es per Copy-Button direkt in dein Chat-Werkzeug einfügen oder als .md-Datei speichern kannst.

::: {.callout-note icon=false}
## Was dieses Beispiel ist (und was nicht)

Was du hier liest, ist **nicht** der Rohoutput des Hypothesengenerators, sondern das *kuratierte Ergebnis* der Workshop-Methode. Drei Schichten unterscheiden:

1. **Hypothesengenerator-Rohliste:** rund fünfzehn Punkte, ungefiltert. Wie diese Liste aussieht, siehst du im [Worked Example](../block-1-theorie-und-beispiel/worked-example-statistics.qmd) unter "Was das LLM enumeriert".
2. **Validierung gegen die Lehrerfahrung:** behalten, korrigieren, verwerfen, plus tacite Ergänzungen der Lehrperson, die das LLM nicht enumerieren konnte.
3. **Lernende-Simulator für die Misconceptions:** ebenfalls validiert, bevor sie in Sektion 3 wandern.

Das fertige Spec hat etwa ein Viertel der Länge der Rohliste plus die nicht-LLM-Ergänzungen. Es zeigt die Form, nicht die Vollständigkeit: für deine eigene Aufgabe würdest du vermutlich weitere Skills und Misconceptions ergänzen.
:::

````{.markdown filename="beispiel-spec-multiple-regression.md"}
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

## Hinweis zum Umfang

Dieses Spec ist absichtlich knapp gehalten, damit die Form deutlich wird. Für eine echte Lehrplanung würden weitere Skills (Einheit der Koeffizienten, $t$-Test pro Koeffizient, Partial-/Semipartialkorrelation) und weitere Misconceptions (bivariate Signifikanz garantiert multiple Signifikanz, Additivität der Effekte) ergänzt.
