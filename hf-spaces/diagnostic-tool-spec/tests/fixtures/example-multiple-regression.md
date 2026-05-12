---
title: "Beispiel-Spec: Multiple Regression"
---

Ein knappes Beispiel-Spec zur Übung "Multiple Regression mit zwei Prädiktoren" aus Block 1. Es zeigt die Form, nicht die Vollständigkeit: für deine eigene Aufgabe würdest du vermutlich weitere Skills und Misconceptions ergänzen. Du kannst dieses Beispiel als Vorlage verwenden und in Block 3 in das laufende Werkzeug einfügen.

## Lernaufgabe (Kontext und Ziel)

Die Lernenden rechnen in R eine multiple Regression mit zwei Prädiktoren (Lernzeit und Mathenote auf Klausurpunktzahl) und interpretieren die Koeffizienten unter Konstanthaltung des jeweils anderen Prädiktors. Übung 5 im Statistik-II-Kurs, im Anschluss an die einfache lineare Regression.

## Erforderliche Skills und Knowledge

- Konditionale Interpretation von "kontrolliert für": "unter Konstanthaltung des jeweils anderen Prädiktors", nicht als aktiver Eingriff in die Daten.
- $R^2$ als gemeinsam erklärter Varianzanteil mehrerer Prädiktoren verstehen, nicht als Summe der bivariaten $r^2$.
- Differenzierung der Regressionskoeffizienten $b_1$ in bivariater versus multipler Regression: dieselbe Variable, unterschiedlicher Wert je nach Modell.

## Antizipierte Misconceptions

- "Kontrollieren" wird als aktiver Eingriff in den Datensatz verstanden: "rausrechnen", "rauspartialisieren", als ob die Mathenote aus den Klausurpunkten entfernt würde.
- $R^2$ in der multiplen Regression wird als Summe der bivariaten $r^2$ aufgefasst: $r^2_{YX_1} + r^2_{YX_2}$.

## Hinweis

Dieses Spec ist absichtlich knapp gehalten, damit die Form deutlich wird. Für eine echte Lehrplanung würden weitere Skills (Einheit der Koeffizienten, $t$-Test pro Koeffizient, Partial-/Semipartialkorrelation) und weitere Misconceptions (bivariate Signifikanz garantiert multiple Signifikanz, Additivität der Effekte) ergänzt.
