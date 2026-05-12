"""Bundled example spec + student answer for the marimo app's "Beispiel laden" button.

Kept in-tree so the deployed HF Space is self-contained (it does not have
access to the surrounding workshop site). The spec mirrors
``workshop/spec-sheet-template/example-multiple-regression.md`` (without YAML
front matter). The student answer is a plausible mid-quality response that
exhibits one of the spec's misconceptions, so the diagnostic call returns a
non-trivial result.
"""

EXAMPLE_SPEC_MD = """## Lernaufgabe (Kontext und Ziel)

Die Lernenden rechnen in R eine multiple Regression mit zwei Prädiktoren (Lernzeit und Mathenote auf Klausurpunktzahl) und interpretieren die Koeffizienten unter Konstanthaltung des jeweils anderen Prädiktors. Übung 5 im Statistik-II-Kurs, im Anschluss an die einfache lineare Regression.

## Erforderliche Skills und Knowledge

- Konditionale Interpretation von "kontrolliert für": "unter Konstanthaltung des jeweils anderen Prädiktors", nicht als aktiver Eingriff in die Daten.
- $R^2$ als gemeinsam erklärter Varianzanteil mehrerer Prädiktoren verstehen, nicht als Summe der bivariaten $r^2$.
- Differenzierung der Regressionskoeffizienten $b_1$ in bivariater versus multipler Regression: dieselbe Variable, unterschiedlicher Wert je nach Modell.

## Antizipierte Misconceptions

- "Kontrollieren" wird als aktiver Eingriff in den Datensatz verstanden: "rausrechnen", "rauspartialisieren", als ob die Mathenote aus den Klausurpunkten entfernt würde.
- $R^2$ in der multiplen Regression wird als Summe der bivariaten $r^2$ aufgefasst: $r^2_{YX_1} + r^2_{YX_2}$.
"""

EXAMPLE_STUDENT_ANSWER = """Ich habe `lm(klausur ~ lernzeit + mathenote)` in R gerechnet. Der Koeffizient für Lernzeit ist $b_1 = 1{,}8$.

Interpretation: Wenn die Lernzeit um eine Stunde steigt, steigen die Klausurpunkte um 1,8 Punkte, weil wir den Effekt der Mathenote rausgerechnet haben. Das $R^2$ ist 0,42; das ist die Summe der einzelnen $r^2$-Werte ($r^2_{YX_1} + r^2_{YX_2}$).
"""
